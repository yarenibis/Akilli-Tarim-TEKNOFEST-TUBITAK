# 🌱 Akıllı Tarım: Yapay Zeka Destekli Bitki Hastalık ve Zararlı Tespiti

Bu proje, tarım alanında bitki sağlığını korumak ve üretkenliği artırmak amacıyla geliştirilen bir **yapay zeka destekli mobil uygulamadır**.  
Sistem, çeşitli bitki türlerinin yapraklarındaki hastalıkları ve zararlıları tespit ederek kullanıcıya hızlı, doğru ve öneri odaklı bilgiler sunar.  
Aynı zamanda sürdürülebilir tarım konusunda bilgilendirmeyi hedefler.  

---

## 📱 Proje Özellikleri
- 🌱 **5 farklı bitki için hastalık tespiti**: Üzüm, mısır, patates, elma  
- 🐞 **Zararlı (böcek) tespiti**: Görüntü üzerinden böcek algılama modeli  
- 🔗 **Mobil uygulama ile API iletişimi**  
- 📚 **Sürdürülebilir tarım içerikleri**: Bilgilendirici yazılar, görseller ve videolar  
- 🌍 **Kullanıcı dostu arayüz**: Bilgilendirici ve pratik kullanım  
- 🔗 **Veritabanı**: Firebase  

---

## 🧠 Kullanılan Modeller

| Model No | Bitki Türü | Açıklama |
|----------|------------|----------|
| 1 | Üzüm    | Yaprak hastalık tespiti |
| 2 | Mısır   | Hastalık sınıflandırma |
| 3 | Patates | Erken ve geç yanıklık tespiti |
| 4 | Elma    | Yaprak lekesi ve mantar hastalıkları |
| 5 | Böcek Tespiti | Böcek detection modeli |

> Modellerin bazıları **CNN tabanlı (ResNet vb.)** hazır mimarilerle, bazıları ise **kendi tasarladığım özel mimarilerle** eğitilmiştir.

---

## 🔌 API Entegrasyonu

1. 📷 Görüntü mobil uygulama üzerinden **API'ye gönderilir**  
2. 🧠 Model sonucu işler ve **sınıflandırma/detection yapar**  
3. 📝 **Tespit sonucu ve öneriler** mobil uygulama ekranında gösterilir  

---

## 📊 Dataset & Modeller

- 📂 Datasetler ve eğitilmiş modeller **Kaggle üzerinde paylaşılmıştır**:  
  👉 [Dataset ve Modeller için Link](#) *(https://www.kaggle.com/models/yarenbi/apple-corn-grape-insect-potato-models)*

---

## 📸 Uygulama Ekran Görüntüleri

| Özellik | Görsel |
|---------|--------|
| Ana Sayfa | ![Ana Sayfa](images/home.png) |
| Hastalık Tespiti Sonucu | ![Hastalık Tespiti](images/disease_detection.png) |
| Böcek Algılama | ![Böcek Tespiti](images/bug_detection.png) |
| Bilgilendirici İçerikler | ![İçerikler](images/info.png) |






