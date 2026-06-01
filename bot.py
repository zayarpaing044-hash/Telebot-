import logging
import urllib.request
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = '8890575246:AAGfsKU8l5v7t4mt6fmwIbiqjz0uYiXXoA4'
OPENROUTER_KEY = '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'

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('မငဂလာပါ! ဘာများ ကူညီရမလဲ?')

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message.text
    url = 'https://openrouter.ai/api/v1/chat/completions'
    h = {'Authorization': 'Bearer ' + OPENROUTER_KEY, 'Content-Type': 'application/json'}
    d = {'model': 'meta-llama/llama-3.1-8b-instruct:free', 'messages': [{'role': 'user', 'content': m}]}
    try:
        req = urllib.request.Request(url, data=json.dumps(d).encode(), headers=h)
        with urllib.request.urlopen(req) as r:
            rep = json.loads(r.read().decode())['choices'][0]['message']['content']
    except Exception as e:
        rep = 'Error: ' + str(e)
