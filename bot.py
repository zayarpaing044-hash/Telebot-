import json,urllib.request
from telegram import Update
from telegram.ext import Application,CommandHandler,MessageHandler,filters,ContextTypes

TELEGRAM_TOKEN='8837627590:AAFKV8PFZ4p8Ne0R2qeUgQZiizh-TeSGsYE'
GROQ_KEY='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'

async def start(u,c):
    await u.message.reply_text('မင်္ဂလာပါ! ဘာများ ကူညီပေးရမလဲ?')

async def handle(u,c):
    m=u.message.text
    url='https://api.groq.com/openai/v1/chat/completions'
    h={'Authorization':'Bearer '+GROQ_KEY,'Content-Type':'application/json','User-Agent':'python-urllib/3.13'}
    d={'messages':[{'role':'user','content':m}],'model':'llama3-8b-8192'}
    try:
        req=urllib.request.Request(url,data=json.dumps(d).encode(),headers=h,method='POST')
        with urllib.request.urlopen(req) as r:
            rep=json.loads(r.read().decode())['choices'][0]['message']['content']
    except Exception as e:
        rep='Error:'+str(e)
    await u.message.reply_text(rep)

def main():
    app=Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler('start',start))
    app.add_handler(MessageHandler(filters.TEXT&~filters.COMMAND,handle))
    print('Bot started!')
    app.run_polling()

if __name__=='__main__':
    main()
