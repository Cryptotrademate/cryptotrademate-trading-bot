import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
from exchanges import ExchangeConnector
from strategies import GridBot, DCABot

# Initialize the bot and Binance connector
bot = telebot.TeleBot(config("TELEGRAM_BOT_TOKEN"))
binance = ExchangeConnector('binance')

# Inline menu for user interaction
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Grid Bot Setup", callback_data="grid_guide"),
        InlineKeyboardButton("DCA Bot Setup", callback_data="dca_guide"),
    )
    markup.add(
        InlineKeyboardButton("Check Balance", callback_data="check_balance"),
        InlineKeyboardButton("Portfolio Value", callback_data="portfolio_value"),
    )
    markup.add(
        InlineKeyboardButton("Help", callback_data="help")
    )
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message, 
        "👋 Welcome to the CryptoTradeMate Crypto Trading Bot!\n"
        "Use the inline menu below to explore features and get started.",
        reply_markup=main_menu()
    )

# Callback query handler for inline menu options
@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    if call.data == "grid_guide":
        bot.send_message(
            call.message.chat.id, 
            "🤖 Grid Bot Guide:\n"
            "1️⃣ Command format: /grid symbol grid_levels lower_price upper_price\n"
            "2️⃣ Example: /grid BTC/USDT 5 30000 35000\n"
            "3️⃣ This will place 5 grid orders between $30,000 and $35,000.\n\n"
            "Start now by typing the /grid command!"
        )
    elif call.data == "dca_guide":
        bot.send_message(
            call.message.chat.id, 
            "📊 DCA Bot Guide:\n"
            "1️⃣ Command format: /dca symbol dca_intervals total_investment\n"
            "2️⃣ Example: /dca BTC/USDT 10 1000\n"
            "3️⃣ This will split $1000 across 10 intervals for DCA.\n\n"
            "Start now by typing the /dca command!"
        )
    elif call.data == "check_balance":
        bot.send_message(
            call.message.chat.id, 
            "💰 To check your balance, type:\n"
            "/balance symbol\n\nExample: /balance USDT"
        )
    elif call.data == "portfolio_value":
        bot.send_message(
            call.message.chat.id, 
            "🪙 Fetching your total portfolio value...\nPlease type /portfolio to see your USDT-equivalent balance."
        )
    elif call.data == "help":
        bot.send_message(
            call.message.chat.id, 
            "🆘 Help Guide:\n"
            "1️⃣ /grid - Start a grid trading bot.\n"
            "2️⃣ /dca - Start a DCA bot.\n"
            "3️⃣ /balance - Check your asset balance.\n"
            "4️⃣ /portfolio - Get your total portfolio value in USDT.\n\n"
            "Use the inline menu to access guides or start commands directly!"
        )

@bot.message_handler(commands=['grid'])
def grid(message):
    args = message.text.split()
    if len(args) != 5:
        bot.reply_to(
            message, 
            "❌ Incorrect usage.\n"
            "Usage: /grid symbol grid_levels lower_price upper_price\n"
            "Example: /grid BTC/USDT 5 30000 35000"
        )
        return
    symbol, grid_levels, lower_price, upper_price = args[1:]
    grid_bot = GridBot(binance, symbol, int(grid_levels), float(lower_price), float(upper_price))
    grid_bot.execute_grid()
    bot.reply_to(message, "✅ Grid orders placed successfully!")

@bot.message_handler(commands=['dca'])
def dca(message):
    args = message.text.split()
    if len(args) != 4:
        bot.reply_to(
            message, 
            "❌ Incorrect usage.\n"
            "Usage: /dca symbol dca_intervals total_investment\n"
            "Example: /dca BTC/USDT 10 1000"
        )
        return
    symbol, dca_intervals, total_investment = args[1:]
    dca_bot = DCABot(binance, symbol, int(dca_intervals), float(total_investment))
    dca_bot.execute_dca()
    bot.reply_to(message, "✅ DCA orders placed successfully!")

@bot.message_handler(commands=['balance'])
def balance(message):
    args = message.text.split()
    if len(args) != 2:
        bot.reply_to(message, "❌ Usage: /balance symbol\nExample: /balance USDT")
        return
    symbol = args[1].upper()
    try:
        balance = binance.get_balance(symbol)
        bot.reply_to(
            message, 
            f"💰 Your balance for {symbol}:\n"
            f"Available: {balance['free']}\n"
            f"Total: {balance['total']}"
        )
    except Exception as e:
        bot.reply_to(message, f"❌ Error fetching balance: {str(e)}")

@bot.message_handler(commands=['portfolio'])
def portfolio(message):
    try:
        total_usdt = binance.get_total_balance_in_usdt()
        bot.reply_to(
            message, 
            f"💼 Your total portfolio balance is approximately {total_usdt:.2f} USDT."
        )
    except Exception as e:
        bot.reply_to(message, f"❌ Error fetching portfolio balance: {str(e)}")

# Start the bot polling
bot.polling()
