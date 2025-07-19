Dondurma Satış Analizi

Bu proje, sıcaklık verileri ile dondurma satışları arasındaki ilişkiyi analiz etmek için bir Python betiği sağlar. Betik, verileri görselleştirmek, korelasyonu hesaplamak ve temel istatistikleri belirlemek için çeşitli işlevler içerir.

--------Özellikler-------

**Veri Yükleme ve Ön İşleme:** Bir CSV dosyasından dondurma satış verilerini yükler ve analiz için hazırlar.

- **Aylık Ortalama Grafiği:** Aylık ortalama sıcaklık ve dondurma satışlarını karşılaştıran bir çubuk grafik oluşturur.

- **Zaman Serisi Grafiği:** Zaman içindeki günlük sıcaklık ve dondurma satışlarını gösteren bir çizgi grafik çizer.

- **Korelasyon Analizi:** Sıcaklık ve dondurma satışları arasındaki Pearson korelasyon katsayısını hesaplar.

- **Regresyon Grafiği:** Sıcaklık ile dondurma satışları arasındaki ilişkiyi gösteren bir regresyon grafiği oluşturur.

- **En Yüksek ve En Düşük Günler:** En sıcak/soğuk günleri ve en yüksek/düşük satış günlerini belirler.

- **Haftalık Toplam Satışlar:** Haftalık toplam dondurma satışlarını özetleyen bir çubuk grafik sunar.

Konsol Çıktısı--------------------------

Sıcaklık ile Dondurma Satışı arasındaki korelasyon değeri.

En sıcak/soğuk günler ve en çok/az satış yapılan günler hakkında bilgiler.

Kaydedilen Grafikler (proje dizininize kaydedilir)----------------------

aylik_ortalama.png: Aylık ortalama sıcaklık ve dondurma satışlarını gösteren çubuk grafik.

zaman_serisi.png: Günlük sıcaklık ve dondurma satışlarının zaman serisi grafiği.

regresyon_grafik.png: Sıcaklık ve dondurma satışları arasındaki regresyon grafiği.

haftalik_toplam_satis.png: Haftalık toplam dondurma satışlarını gösteren çubuk grafik.

Kod Yapısı-------------------------------------------

load_data(): Veri dosyasını yükler, 'Tarih' sütununu datetime nesnesine dönüştürür ve 'Ay' ile 'Hafta' sütunlarını ekler.

aylik_ortalama_grafik(df): Aylık sıcaklık ve satış ortalamalarını görselleştirir.

zaman_serisi_grafik(df): Zaman içindeki günlük sıcaklık ve satış trendlerini gösterir.

korelasyon_analizi(df): Sıcaklık ve satış arasındaki korelasyonu hesaplar ve yazdırır.

regresyon_grafik(df): Sıcaklık ile satış arasındaki doğrusal ilişkiyi bir dağılım grafiği ile gösterir.

en_ve_az_gunler(df): Veri kümesindeki aşırı noktaları (en sıcak, en soğuk, en yüksek/düşük satış) tanımlar.

haftalik_toplam_satis(df): Haftalık satış performansını özetler.

main(): Tüm analiz fonksiyonlarını çağıran ana fonksiyondur.
