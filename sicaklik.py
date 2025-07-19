import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    df = pd.read_csv("C:\\Users\\Sinem\\Desktop\\yaz_dondurma_verisi.csv")
    df['Tarih'] = pd.to_datetime(df['Tarih'])
    df['Ay'] = df['Tarih'].dt.month
    df['Hafta'] = df['Tarih'].dt.isocalendar().week
    return df

def aylik_ortalama_grafik(df):
    aylik_ortalama = df.groupby('Ay')[['Sıcaklık (°C)', 'Dondurma Satışı (adet)']].mean().round(1)
    aylik_ortalama.index = aylik_ortalama.index.map({6: "Haziran", 7: "Temmuz", 8: "Ağustos"})
    aylar = aylik_ortalama.index.tolist()
    sicaklik = aylik_ortalama['Sıcaklık (°C)']
    satis = aylik_ortalama['Dondurma Satışı (adet)']

    bar_width = 0.35
    index = np.arange(len(aylar))

    fig, ax1 = plt.subplots(figsize=(8,5))
    bar1 = ax1.bar(index, sicaklik, bar_width, color='tomato', label='Ortalama Sıcaklık (°C)')
    ax1.set_xlabel('Aylar')
    ax1.set_ylabel('Sıcaklık (°C)', color='tomato')
    ax1.set_xticks(index)
    ax1.set_xticklabels(aylar)
    ax1.tick_params(axis='y', labelcolor='tomato')

    ax2 = ax1.twinx()
    bar2 = ax2.bar(index + bar_width, satis, bar_width, color='skyblue', label='Ortalama Dondurma Satışı (adet)')
    ax2.set_ylabel('Dondurma Satışı (adet)', color='skyblue')
    ax2.tick_params(axis='y', labelcolor='skyblue')

    plt.title('Aylık Ortalama Sıcaklık ve Dondurma Satışı')
    fig.tight_layout()
    fig.legend(loc='center', bbox_to_anchor=(0.5, 0.5))
    plt.savefig("aylik_ortalama.png", dpi=300, bbox_inches='tight')
    plt.show()

def zaman_serisi_grafik(df):
    plt.figure(figsize=(12,5))
    plt.plot(df['Tarih'], df['Sıcaklık (°C)'], label='Sıcaklık (°C)', color='orange')
    plt.plot(df['Tarih'], df['Dondurma Satışı (adet)'], label='Dondurma Satışı (adet)', color='blue')
    plt.xlabel('Tarih')
    plt.ylabel('Değer')
    plt.title('Günlük Sıcaklık ve Dondurma Satışı')
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("zaman_serisi.png", dpi=300, bbox_inches='tight')
    plt.show()

def korelasyon_analizi(df):
    corr = df['Sıcaklık (°C)'].corr(df['Dondurma Satışı (adet)'])
    print(f"Sıcaklık ile Dondurma Satışı arasındaki korelasyon: {corr:.2f}")

def regresyon_grafik(df):
    g = sns.lmplot(x='Sıcaklık (°C)', y='Dondurma Satışı (adet)', data=df, height=6, aspect=1.5)
    g.fig.subplots_adjust(top=0.9)
    g.fig.suptitle('Sıcaklık ve Dondurma Satışı Arasındaki İlişki')
    g.fig.savefig("regresyon_grafik.png", dpi=300, bbox_inches='tight')
    plt.show()

def en_ve_az_gunler(df):
    en_sicak = df.loc[df['Sıcaklık (°C)'].idxmax()]
    en_soguk = df.loc[df['Sıcaklık (°C)'].idxmin()]
    en_cok_satis = df.loc[df['Dondurma Satışı (adet)'].idxmax()]
    en_az_satis = df.loc[df['Dondurma Satışı (adet)'].idxmin()]

    print("En sıcak gün:", en_sicak['Tarih'].date(), " - Sıcaklık:", en_sicak['Sıcaklık (°C)'])
    print("En soğuk gün:", en_soguk['Tarih'].date(), " - Sıcaklık:", en_soguk['Sıcaklık (°C)'])
    print("En çok satış yapılan gün:", en_cok_satis['Tarih'].date(), " - Satış:", en_cok_satis['Dondurma Satışı (adet)'])
    print("En az satış yapılan gün:", en_az_satis['Tarih'].date(), " - Satış:", en_az_satis['Dondurma Satışı (adet)'])

def haftalik_toplam_satis(df):
    haftalik_satis = df.groupby('Hafta')['Dondurma Satışı (adet)'].sum()
    haftalik_satis.plot(kind='bar', figsize=(12,5), color='green')
    plt.title('Haftalık Toplam Dondurma Satışı')
    plt.xlabel('Hafta Numarası')
    plt.ylabel('Toplam Satış')
    plt.savefig("haftalik_toplam_satis.png", dpi=300, bbox_inches='tight')
    plt.show()

def main():
    df = load_data()
    aylik_ortalama_grafik(df)
    zaman_serisi_grafik(df)
    korelasyon_analizi(df)
    regresyon_grafik(df)
    en_ve_az_gunler(df)
    haftalik_toplam_satis(df)

if __name__ == "__main__":
    main()
