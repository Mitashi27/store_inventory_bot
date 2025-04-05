from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import utils1 as utils
import os

BOT_TOKEN = os.getenv('7980192962:AAEat2-RxF9NJrJ2Cyf37abHCNIPM_mS1JI')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to StoreTrackerBot!\nUse /additem, /updateitem, /checkstock, /stocksummary, or /log.")

async def additem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        item = context.args[0]
        qty = int(context.args[1])
        response = utils.add_item(item, qty, update.effective_user.first_name)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("Usage: /additem [ItemName] [Quantity]")

async def updateitem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        item = context.args[0]
        qty = int(context.args[1])
        response = utils.update_item(item, qty, update.effective_user.first_name)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("Usage: /updateitem [ItemName] [+/-Quantity]")

async def checkstock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        item = context.args[0]
        response = utils.check_stock(item)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("Usage: /checkstock [ItemName]")

async def stocksummary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = utils.stock_summary()
    await update.message.reply_text(response)

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        item = context.args[0]
        response = utils.get_log(item)
        await update.message.reply_text(response)
    except:
        await update.message.reply_text("Usage: /log [ItemName]")

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("additem", additem))
    app.add_handler(CommandHandler("updateitem", updateitem))
    app.add_handler(CommandHandler("checkstock", checkstock))
    app.add_handler(CommandHandler("stocksummary", stocksummary))
    app.add_handler(CommandHandler("log", log))

    app.run_polling()
