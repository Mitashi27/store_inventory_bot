from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import utils1 as utils
import os

BOT_TOKEN = os.getenv('BOT_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to StoreTrackerBot!\nUse /additem, /updateitem, /checkstock, /stocksummary, or /log.")

async def additem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Usage: /additem [ItemName] [Quantity]")
        return

    item = context.args[0]
    try:
        qty = int(context.args[1])
    except ValueError:
        await update.message.reply_text("Quantity must be a number.")
        return

    response = utils.add_item(item, qty, update.effective_user.first_name)
    await update.message.reply_text(response)


async def updateitem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 2:
        await update.message.reply_text("Usage: /updateitem [ItemName] [+/-Quantity]")
        return

    item = context.args[0]
    try:
        qty = int(context.args[1])
    except ValueError:
        await update.message.reply_text("Quantity must be a number (positive or negative).")
        return

    response = utils.update_item(item, qty, update.effective_user.first_name)
    await update.message.reply_text(response)

async def checkstock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /checkstock [ItemName]")
        return

    item = context.args[0]
    response = utils.check_stock(item)
    await update.message.reply_text(response)


async def stocksummary(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = utils.stock_summary()
    await update.message.reply_text(response)

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /log [ItemName]")
        return

    item = context.args[0]
    response = utils.get_log(item)
    await update.message.reply_text(response)


if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("additem", additem))
    app.add_handler(CommandHandler("updateitem", updateitem))
    app.add_handler(CommandHandler("checkstock", checkstock))
    app.add_handler(CommandHandler("stocksummary", stocksummary))
    app.add_handler(CommandHandler("log", log))

    app.run_polling()
