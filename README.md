# Dondurma Satış Analizi

Bu proje, sıcaklık verileri ile dondurma satışları arasındaki ilişkiyi analiz etmek için bir Python betiği sağlar. Betik, verileri görselleştirmek, korelasyonu hesaplamak ve temel istatistikleri belirlemek için çeşitli işlevler içerir.

## Özellikler
-------

**Veri Yükleme ve Ön İşleme:** Bir CSV dosyasından dondurma satış verilerini yükler ve analiz için hazırlar.

- **Aylık Ortalama Grafiği:** Aylık ortalama sıcaklık ve dondurma satışlarını karşılaştıran bir çubuk grafik oluşturur.
<img width="2370" height="1466" alt="aylik_ortalama" src="https://github.com/user-attachments/assets/6a10e7f8-cdec-459c-8dfd-7afca62ab675" />


- **Zaman Serisi Grafiği:** Zaman içindeki günlük sıcaklık ve dondurma satışlarını gösteren bir çizgi grafik çizer.
<img width="3570" height="1467" alt="zaman_serisi" src="https://github.com/user-attachments/assets/464820ee-bfc8-44ee-90b3-fdce8fc29253" />


- **Korelasyon Analizi:** Sıcaklık ve dondurma satışları arasındaki Pearson korelasyon katsayısını hesaplar.

- **Regresyon Grafiği:** Sıcaklık ile dondurma satışları arasındaki ilişkiyi gösteren bir regresyon grafiği oluşturur.
<img width="2670" height="1779" alt="regresyon_grafik" src="https://github.com/user-attachments/assets/b5b96185-4c15-4730-92eb-22b907974b9d" />


- **En Yüksek ve En Düşük Günler:** En sıcak/soğuk günleri ve en yüksek/düşük satış günlerini belirler.

- **Haftalık Toplam Satışlar:** Haftalık toplam dondurma satışlarını özetleyen bir çubuk grafik sunar.
<img width="3017" height="1419" alt="haftalik_toplam_satis" src="https://github.com/user-attachments/assets/087d6b91-674f-4ab1-8b4e-d594579166be" />


## Konsol Çıktısı
--------------------------

- Sıcaklık ile Dondurma Satışı arasındaki korelasyon değeri.

- En sıcak/soğuk günler ve en çok/az satış yapılan günler hakkında bilgiler.

- Kaydedilen Grafikler (proje dizininize kaydedilir)----------------------

- aylik_ortalama.png: Aylık ortalama sıcaklık ve dondurma satışlarını gösteren çubuk grafik.

- zaman_serisi.png: Günlük sıcaklık ve dondurma satışlarının zaman serisi grafiği.

- regresyon_grafik.png: Sıcaklık ve dondurma satışları arasındaki regresyon grafiği.

- haftalik_toplam_satis.png: Haftalık toplam dondurma satışlarını gösteren çubuk grafik.

## Kod Yapısı
-------------------------------------------

- load_data(): Veri dosyasını yükler, 'Tarih' sütununu datetime nesnesine dönüştürür ve 'Ay' ile 'Hafta' sütunlarını ekler.

- aylik_ortalama_grafik(df): Aylık sıcaklık ve satış ortalamalarını görselleştirir.

- zaman_serisi_grafik(df): Zaman içindeki günlük sıcaklık ve satış trendlerini gösterir.

- korelasyon_analizi(df): Sıcaklık ve satış arasındaki korelasyonu hesaplar ve yazdırır.

- regresyon_grafik(df): Sıcaklık ile satış arasındaki doğrusal ilişkiyi bir dağılım grafiği ile gösterir.

- en_ve_az_gunler(df): Veri kümesindeki aşırı noktaları (en sıcak, en soğuk, en yüksek/düşük satış) tanımlar.

- haftalik_toplam_satis(df): Haftalık satış performansını özetler.

- main(): Tüm analiz fonksiyonlarını çağıran ana fonksiyondur.
