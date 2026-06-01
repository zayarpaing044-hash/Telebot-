import logging, json, urllib.request
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN='8837627590:AAFKV8PFZ4p8Ne0R2qeUGQZiizh6gMOiLbA'
GROQ_KEY='gsk_hYJgP7QESJ7az9IrWF7zWGdyb3FYRWj9Mp3hjx2f'

logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('မင်္ဂလာပါ!')

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m = update.message.text
    url = 'https://api.groq.com/openai/v1/chat/completions'
    h = {'Authorization':'Bearer '+GROQ_KEY,'Content-Type':'application/json'}
    d = {'model':'llama3-8b-8192','messages':[{'role':'user','content':m}]}
    try:
        req = urllib.request.Request(url,data=json.dumps(d).encode(),headers=h)
        with urllib.request.urlopen(req) as r:
            rep = json.loads(r.read().decode())['choices'][0]['message']['content']
    except Exception as e:
        rep = 'Error:'+str(e)
    await update.message.reply_text(rep)

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
    app.run_polling()

if __name__ == '__main__':
    main()
