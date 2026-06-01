import logging
import json
import os
import urllib.request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = '8890575246:AAGfsKU8l5v7t4mt6fmwIbiqjz0uYiXXoA4'
GROQ_KEY = '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'
WEBHOOK_URL = 'https://telebot-production-1e1b.up.railway.app'

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('မင်္ဂလာပါ! ဘာများ ကူညီရမလဲ?')

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message.text
    url = 'https://api.groq.com/openai/v1/chat/completions'
    h = {'Authorization': 'Bearer ' + GROQ_KEY, 'Content-Type': 'application/json'}
    d = {'model': 'mixtral-8x7b-32768', 'messages': [{'role': 'user', 'content': m}]}
    try:
        req = urllib.request.Request(url, data=json.dumps(d).encode(), headers=h)
        with urllib.request.urlopen(req) as r:
            rep = json.loads(r.read().decode())['choices'][0]['message']['content']
    except Exception as e:
        rep = 'Error: ' + str(e)
    await update.message.reply_text(rep)

if __name__ == '__main__':
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler
