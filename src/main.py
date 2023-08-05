import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import discord
import os


# Your Discord webhook URL
WEBHOOK_URL = os.getenv("WEBHOOK")

def get_bitcoin_price():
    url = 'https://www.binance.com/en/markets/overview'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find('div', class_='html body div#__APP div.css-ph4aey div.css-tq0shg main.css-1wr4jig div.css-9jfzzo div.css-194m5n4 div.css-1m4ys10 div#tabContainer.css-6g4rnu div.css-72ldqd div.css-dfdqsv div.css-1y8kib5 div.css-vurnku div.css-1pysja1 div.css-vlibs4 div.css-1iegfwm div.css-hwo5f4 div.css-ovtrou')
    if price_element:
        return price_element.text.strip()
    else:
        return 'Unable to fetch the bitcoin price.'

def send_discord_webhook(message):
    data = {
        'content': message
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(WEBHOOK_URL, json=data, headers=headers)
    if response.status_code == 204:
        print("Webhook sent successfully.")
    else:
        print(f"Failed to send webhook. Status code: {response.status_code}")

if __name__ == '__main__':
    bitcoin_price = get_bitcoin_price()
    send_discord_webhook(f"Today's Bitcoin price: {bitcoin_price}")
