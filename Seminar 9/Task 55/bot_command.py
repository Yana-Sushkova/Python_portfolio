from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import emoji
import datetime
from random import choice

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Здравствуйте, {update.effective_user.first_name} {emoji.emojize(":red_heart:")}. \nЭто бот-предсказатель. \nОн может дать ответ на Ваш вопрос.  \nЗадайте про себя или вслух вопрос и нажмите на /fortune_telling , чтобы получить ответ: "Да", "Нет" или "Спросите позже". \nНажмите /help, чтобы увидеть все команды.')
  
async def fortune_telling (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(choice(['Да' , 'Нет', "Спросите позже"]))
    
async def help (update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'All commands:  \n /start {emoji.emojize(":red_heart:")} \n /fortune_telling {emoji.emojize(":red_heart:")} \n  /help {emoji.emojize(":red_heart:")}')

