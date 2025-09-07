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
  👉 *(https://www.kaggle.com/models/yarenbi/apple-corn-grape-insect-potato-models)*

---

## 📸 Uygulama Ekran Görüntüleri
<h2>📸 Uygulama Ekran Görüntüleri</h2>

<table border="1" cellpadding="10">
  <thead>
    <tr>
      <th>Özellik</th>
      <th>Görsel</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Ana Sayfa</td>
      <td><img src="ana-ekrann.png" alt="Ana Sayfa" width="300"></td>
    </tr>
    <tr>
      <td>Hastalık Modeli Seçme</td>
      <td><img src="bitki-detection-ana-ekran.png" alt="Bitki Modelleri" width="300"></td>
    </tr>
    <tr>
      <td>Hastalık Tespiti Sonucu</td>
      <td><img src="bitki-tahmin.png" alt="Hastalık Tespiti" width="300"></td>
    </tr>
    <tr>
      <td>Böcek Algılama</td>
      <td><img src="böcek-detection.png" alt="Böcek Tespiti" width="300"></td>
    </tr>
    <tr>
      <td>Bilgilendirici İçerikler Ana Sayfa</td>
      <td><img src="öneriler-ana-ekran.png" alt="İçerikler" width="300"></td>
    </tr>
    <tr>
      <td>Bilgilendirici İçerik Sayfası</td>
      <td><img src="öneriler.png" alt="İçerikler" width="300"></td>
    </tr>
  </tbody>
</table>










