import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "YOUR_TOKEN_HERE"

jokes = 

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    if update.effective_chat.type not in ["group", "supergroup"]:
        return

    text = update.message.text.lower()

    # теперь реагирует НА КАЖДОЕ сообщение
    if "смех" in text:
        await update.message.reply_text("Смех уже тут, и ему не до шуток 😏")
    elif "бус" in text:
        await update.message.reply_text("🚐 Подъехал быстро, ты даже понять не успел")
    elif "полиция" in text:
        await update.message.reply_text("Полиция? Я вообще не при делах 😶")
    elif "тцк" in text:
        await update.message.reply_text("Тцк? Не слышал, не видел, не участвовал 👀")
    else:
        # всегда отвечает, даже если нет ключевых слов
        await update.message.reply_text(random.choice(jokes))


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))
app.run_polling()
