import pywhatkit
import time
import csv

# Kodun içinde sabit numaralar ve opsiyonel mesajlar
sabit_numaralar = [
    ("+905340526866", None),
    ("+905312413907", None),  # None ise varsayılan mesaj kullanılır
]

# isletme_telefonlari.csv dosyasından numaraları oku
isletme_csv = "isletme_telefonlari.csv"
isletme_numaralar = []
try:
    with open(isletme_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tel = row.get('Telefon')
            if tel:
                temiz_tel = ''.join(filter(str.isdigit, tel))
                if temiz_tel.startswith('0'):
                    temiz_tel = '+9' + temiz_tel
                elif not temiz_tel.startswith('90'):
                    temiz_tel = '+90' + temiz_tel
                else:
                    temiz_tel = '+' + temiz_tel
                isletme_numaralar.append((temiz_tel, None))
except FileNotFoundError:
    print(f"{isletme_csv} bulunamadı, sadece kod içindeki numaralar kullanılacak.")

varsayilan_mesaj = (
    "🔊 Yeni Müşteriler Sizi Arasın!\n"
    "İşitme cihazı satışlarınızı artırmak için özel bir dijital çözüm geliştirdik:\n"
    "👉 isitmetesti.izygrow.com\n\n"
    "Bu sayfayı işletmenizin web sitesine entegre ederek ziyaretçilerinize\n"
    "✅ İşitme testi yapma\n"
    "✅ İletişim bilgisi bırakma\n"
    "✅ Size ulaşma\n"
    "imkanı sunuyorsunuz. Böylece sizi aktif olarak arayan, ilgilenmiş müşterilere ulaşıyorsunuz.\n\n"
    "📈 Normal fiyatı: 65.000 TL\n"
    "⚡ Bu mesaja 2 gün içinde dönen işletmelere özel kampanya: 25.000 TL + KDV\n\n"
    "Hemen size özel sayfayı hazırlayalım, yeni müşteriler kazanmaya başlayın!\n"
    "👉 Kurumsal sitemiz: izygrow.com\n"
    "📲 Instagram: instagram.com/izygrowagency"
)
gecikme_saniye = 60  # Her mesajdan sonra 1 dakika bekle

# Kullanıcıdan onay al
def onay_al():
    cevap = input(f"{isletme_csv} dosyasındaki {len(isletme_numaralar)} numaraya mesaj göndermek istiyor musunuz? (evet/hayır): ")
    return cevap.strip().lower() == 'evet'

# Önce isletme_numaralar listesindekilere mesaj gönder
if isletme_numaralar and onay_al():
    for i, (numara, _) in enumerate(isletme_numaralar):
        mesaj = varsayilan_mesaj
        print(f"{numara} numarasına anında mesaj gönderiliyor...")
        try:
            pywhatkit.sendwhatmsg_instantly(numara, mesaj, wait_time=10, tab_close=True)
            print("✅ Mesaj gönderildi.")
        except Exception as e:
            print(f"❌ Hata oluştu: {e}")
        if i != 0:
            time.sleep(gecikme_saniye)
elif isletme_numaralar:
    print(f"{isletme_csv} dosyasındaki numaralara mesaj gönderilmedi.")

# Sonra sabit numaralara mesaj gönder
saat = time.localtime().tm_hour
ilk_dakika = time.localtime().tm_min + 1
for i, (numara, mesaj_row) in enumerate(sabit_numaralar):
    mesaj = mesaj_row if mesaj_row else varsayilan_mesaj
    print(f"{numara} numarasına anında mesaj gönderiliyor...")
    try:
        pywhatkit.sendwhatmsg_instantly(numara, mesaj, wait_time=10, tab_close=True)
        print("✅ Mesaj gönderildi.")
    except Exception as e:
        print(f"❌ Hata oluştu: {e}")
    if i != 0:
        time.sleep(gecikme_saniye)

