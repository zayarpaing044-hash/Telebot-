import logging
import json
import urllib.request
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TELEGRAM_TOKEN='8837627590:AAFKV8PFZ4p8Ne0R2qeUgQZiizh-TeSGsYE'
GROQ_KEY='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'

logging.basicConfig(level=logging.INFO)

def start(update, context):
    update.message.reply_text('မင်္ဂလာပါ! ဘာများ ကူညီပေးရမလဲ?')

def handle(update, context):
    m = update.message.text
    url = 'https://api.groq.com/openai/v1/chat/completions'
    h = {'Authorization':'Bearer '+GROQ_KEY,'Content-Type':'application/json','User-Agent':'python-urllib/3.13'}
    d = {'messages':[{'role':'user','content':m}],'model':'llama3-8b-8192'}
    try:
        req = urllib.request.Request(url,data=json.dumps(d).encode(),headers=h,method='POST')
        with urllib.request.urlopen(req) as r:
            rep = json.loads(r.read().decode())['choices'][0]['message']['content']
    except Exception as e:
        rep = 'Error:'+str(e)
    update.message.reply_text(rep)

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle))
    print('Bot started!')
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
