import os
import requests
from bs4 import BeautifulSoup

OBS_URL = "https://obs.kkude.edu.tr"

USERNAME = os.getenv("OBS_USER")
PASSWORD = os.getenv("OBS_PASS")

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

DERS_ADI = "Bitirme Projesi"

def telegram(mesaj):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": mesaj})

session = requests.Session()

login_data = {
    "username": USERNAME,
    "password": PASSWORD
}

session.post(OBS_URL + "/login", data=login_data)

r = session.get(OBS_URL + "/notlar")
soup = BeautifulSoup(r.text, "html.parser")

if DERS_ADI in soup.text:
    if "—" not in soup.text:
        telegram("🎉 Bitirme Projesi notun girildi!")
