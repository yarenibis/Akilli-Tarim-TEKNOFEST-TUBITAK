from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import os

app = FastAPI()



# ✅ Model yolları (bitki türüne göre)
MODEL_PATHS = {
    "apple": "models/best_apple_mobilenet_model.h5",
    "corn": "models/best_corn_model.h5",
    "grape": "models/best_grape_mobilenet_model.h5",
    "potato": "models/best_potato2_model.h5",
    "insect":"models/best_insect_mobilenet_model.h5"
}

# ✅ Etiketler (bitki türüne göre)
CLASS_LABELS = {
    "apple": ['Apple Scab', 'Black Rot', 'Cedar Apple Rust', 'Healthy'],
    "corn": ['Blight', 'Common_Rust', 'Gray_Leaf_Spot', 'Healthy'],
    "grape": [
        'Black rot','ESCA','Healthy','Leaf Blight'
    ],
    "potato": ['Early_Blight', 'Healthy', 'Late_Blight'],
    "insect": [
        'Boxelder Bugs','Cabbage Looper','Cutworm','Epilachna vigintioctopunctata','Flea Beetles',
    'Mediterranean fruit fly','Riptortus','Squash Bug'
    ]
}

# ✅ Model önbelleği
model_cache = {}

def load_model_cached(model_type: str):
    if model_type in model_cache:
        return model_cache[model_type]

    model_path = MODEL_PATHS.get(model_type)
    if not model_path or not os.path.exists(model_path):
        return None

    model = load_model(model_path, compile=False)
    model_cache[model_type] = model
    return model

def run_prediction(model, image_path, class_labels):
    try:
        input_shape = model.input_shape  # (None, H, W, 3)
        target_size = (input_shape[1], input_shape[2])

        img = load_img(image_path, target_size=target_size)
        img_array = img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        predicted_index = np.argmax(prediction)
        predicted_class = class_labels[predicted_index]
        confidence = float(np.max(prediction)) * 100

        return predicted_class, confidence

    except Exception as e:
        print(f"❌ Tahmin hatası: {e}")
        return None, None

# ✅ /predict endpoint
@app.post("/predict")
async def predict_endpoint(
    file: UploadFile = File(...),
    model_type: str = Form(...)
):
    if model_type not in MODEL_PATHS:
        return JSONResponse(content={"error": f"'{model_type}' türü desteklenmiyor."}, status_code=400)

    model = load_model_cached(model_type)
    class_labels = CLASS_LABELS.get(model_type)

    if not model or not class_labels:
        return JSONResponse(content={"error": "Model veya sınıf etiketleri yüklenemedi."}, status_code=500)

    # 📷 Görseli geçici kaydet
    contents = await file.read()
    temp_path = "temp.jpg"
    with open(temp_path, "wb") as f:
        f.write(contents)

    predicted_class, confidence = run_prediction(model, temp_path, class_labels)

    if predicted_class is None:
        return JSONResponse(content={"error": "Tahmin sırasında hata oluştu."}, status_code=500)

    return {
        "model_type": model_type,
        "prediction": predicted_class,
        "confidence": round(confidence, 2)
    }