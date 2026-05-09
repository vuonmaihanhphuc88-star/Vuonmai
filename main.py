import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Chào chủ nhân! Bot Cánh Tay đã sẵn sàng trên Render.")

if __name__ == '__main__':
    # Lấy Token từ môi trường hoặc dán trực tiếp vào đây
    TOKEN = "8753096816:AAFzeZXgnR4nNf4FQ8JpsZRLQuYfRYKruRc"
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot đang chạy...")
    app.run_polling()
