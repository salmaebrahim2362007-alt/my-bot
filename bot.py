from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "9257392120:AAH7WM3KlZsSw-a6C7eih2lD_6bC3-7WIKc"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("السلام عليكم ورحمة الله وبركاته💗\nأهلاً بيك يا صديقي..\nمحاولتك اليومية لتكون أقرب إلى الله.\n\nمتنساش تصلي على النبي، وتدعي لأخواتنا في فلسطين 💗")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("البوت اشتغل 💗")
    app.run_polling()

if __name__ == "__main__":
    main()