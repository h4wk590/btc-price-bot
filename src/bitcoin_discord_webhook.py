"""
Author: Aidan Brown 
Description: Sends daily price of bitcoin to my Discord server.

"""

import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import discord
import os

# Importing webhook secret from env
WEBHOOK_URL = os.getenv("WEBHOOK")

# Define function to get BTC price from Binance
def get_bitcoin_price():
    url = 'https://www.binance.com/en/markets/overview'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    price_element = soup.find('div', class_='html body div#__APP div.css-ph4aey div.css-tq0shg main.css-1wr4jig div.css-9jfzzo div.css-194m5n4')
    if price_element:
        return price_element.text.strip()
    else:
        return 'Unable to fetch the bitcoin price.' # Error handling - css issues

# Define function to send webhook
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

# Send message from parsed HTML/CSS
if __name__ == '__main__':
    bitcoin_price = get_bitcoin_price()
    send_discord_webhook(f"Today's Bitcoin price: {bitcoin_price}")
