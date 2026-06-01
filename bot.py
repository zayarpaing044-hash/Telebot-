import logging
import urllib.request
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = '8890575246:AAEoQ1YuJVK2g2WlmcDfHN4DJJQk-mdIQkk'
GEMINI_KEY = 'AIzaSyAb8RN6JhRanwBeLt95oz02lm3N33iQQxd9PKdbfsHJd7Z3u0gA'

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('မငဂလာပါ! ဘာများ ကူညီရမလဲ?')

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message.text
    url = f'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_KEY}'
    h = {'Content-Type': 'application/json'}
    d
