from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
from bot_command import *
from random import choice

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("fortune_telling", fortune_telling))
app.add_handler(CommandHandler("help", help ))

app.run_polling()