# Yüz Tespiti ve Sayma Uygulaması 👤📷

Bu uygulama, OpenCV kütüphanesi kullanılarak gerçek zamanlı yüz tespiti ve sayma yetenekleri sunar. Uygulama, farklı kademelerde performansa sahip yüz tespit sınıflayıcılarını değerlendirir ve en iyi performansı gösterenini seçerek kullanır.

## Kullanılan Yöntemler ve Özellikler 🎇

- **Haar Cascade Sınıflayıcıları**: Uygulama, aşağıdaki Haar Cascade modellerini değerlendirir ve en uygununu seçer:
  - `haarcascade_frontalface_default.xml`
  - `haarcascade_frontalface_alt.xml`
  - `haarcascade_frontalface_alt2.xml`
  - `haarcascade_frontalface_alt_tree.xml`
  - `haarcascade_profileface.xml`

- **Performans Değerlendirmesi**: Her bir sınıflayıcı, başlangıçta bir örnekleme üzerinde test edilerek performansı ölçülür ve en iyi performans gösteren seçilir.

- **Gerçek Zamanlı Yüz Takibi**: Kameradan veya videodan alınan görüntüler üzerinde yüz tespiti yapılır ve her bir yüz takip edilir.

- **Görüntü İşleme ve Görselleştirme**: Yüzler çerçevelenir, takip edilen yüzlerin sayısı gösterilir ve kullanılan sınıflayıcı adı görüntülenir.

## Kullanım ✨

Uygulamayı çalıştırmak için:

1. **Gereksinimler**: Python 3.x ve OpenCV kütüphanesi gereklidir.
   
2. **Başlatma**: Terminal veya komut istemcisinde uygulama klasörüne gidin ve aşağıdaki komutu çalıştırın:

   ```
   python main2.py
   ```

3. **Seçenekler**: Program başlatıldığında, kameradan veya bir video dosyasından yüz tespiti yapmak için seçim yapabilirsiniz.

4. **Kapatma**: Çıkış için `q` tuşuna basın.

## Ekran Görüntüsü 📷

![image](https://github.com/fastuptime/Real_time_Face_Detection_and_Counting_Application/assets/63351166/5cb16480-5d26-4148-b863-8c3925c721ff)

