from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.utils.request import Request

TOKEN = "توکن_ربات"

PROXY = {
    "proxy_url": "socks5://127.0.0.1:1080",  # آدرس پروکسی
    "urllib3_proxy_kwargs": {
        "username": "user",  # اگه لازم نداره خالی بذار
        "password": "pass"
    }
}

def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! ربات از طریق پروکسی وصله 🚀")

def main():
    request = Request(con_pool_size=8)
    updater = Updater(TOKEN, request_kwargs=PROXY)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
