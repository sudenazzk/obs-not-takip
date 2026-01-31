import requests
from bs4 import BeautifulSoup
import os

print("KONTROL.PY ÇALIŞTI")


# =====================
# ORTAM DEĞİŞKENLERİ
# =====================
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
OBS_USERNAME = os.getenv("OBS_USERNAME")
OBS_PASSWORD = os.getenv("OBS_PASSWORD")

# =====================
# SABİTLER
# =====================
OBS_BASE_URL = "https://obs.kkude.edu.tr"
DERS_ADI = "Bitirme Projesi 1"

# =====================
# TELEGRAM FONKSİYONU
# =====================
def telegram(mesaj):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mesaj
    }
    r = requests.post(url, data=data)
    print("Telegram response:", r.text)

# =====================
# ANA İŞLEM
# =====================
def main():
    session = requests.Session()

    # OBS login
    login_url = OBS_BASE_URL + "/login"
    login_data = {
        "username": OBS_USERNAME,
        "password": OBS_PASSWORD
    }

    login_response = session.post(login_url, data=login_data)

    # Notlar sayfası
    notlar_url = OBS_BASE_URL + "/notlar"
    r = session.get(notlar_url)

    soup = BeautifulSoup(r.text, "html.parser")
    sayfa = soup.get_text(separator=" ")

    if DERS_ADI in sayfa:
        # Not henüz girilmediyse genelde — veya boş olur
        if "—" not in sayfa and "--" not in sayfa:
            telegram("🎉 Bitirme Projesi notun OBS'ye girildi!")
        else:
            print("Bitirme Projesi var ama not yok.")
    else:
        print("Bitirme Projesi dersi bulunamadı.")

# =====================
# ÇALIŞTIR
# =====================
if __name__ == "__main__":
    main()
