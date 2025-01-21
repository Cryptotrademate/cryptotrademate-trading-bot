# CryptoTradeMate Crypto Trading Bot

Welcome to **CryptoTradeMate**, a free, open-source advanced crypto trading bot designed to automate your trading strategies, simplify portfolio management, and provide insightful analytics. With CryptoTradeMate, you can easily execute trading strategies like Grid and Dollar-Cost Averaging (DCA), monitor your portfolio in real time, and make informed trading decisions—all within a user-friendly interface. It is designed to support all major exchanges and be controlled via Telegram or webUI.

   <div align="center">
  <img src="https://github.com/user-attachments/assets/b707fdde-5fd2-4d39-b86c-5d0784b40b93" alt="CTM crypto trading bot">
</div>

## 🚀 Features
1. **Automated Trading Strategies**:
   - **Grid Trading**: Automates buying and selling within predefined price ranges for maximum profit.
   - **Dollar-Cost Averaging (DCA)**: Gradually invests in a cryptocurrency to reduce the impact of market volatility.

2. **Portfolio Management**:
   - View balances for specific assets.
   - Check your total portfolio value in USDT.

3. **Real-Time Analytics**:
   - Fetch live balances and asset prices from your exchange.
   - Monitor total portfolio performance seamlessly.

4. **User-Friendly Interface**:
   - Intuitive Telegram bot interface with guided commands.
   - Inline menu for quick access to features and help.
  
5. **Multi-Exchange Support**:
   - Trade on multiple exchanges like Binance, KuCoin, Coinbase, and more.

6. **Strategy Backtesting**:
   - [Test your strategies](https://github.com/Cryptotrademate/cryptotrademate-backtesting-tool) with historical data before deploying live.
     
## 🔧 Commands
1. **Start**: `/start`  
   Get an overview of available features and commands.

2. **Grid Trading**: `/grid symbol grid_levels lower_price upper_price`  
   Example: `/grid BTC/USDT 5 25000 30000`  
   Place grid trading orders for the specified symbol.

3. **Dollar-Cost Averaging (DCA)**: `/dca symbol dca_intervals total_investment`  
   Example: `/dca ETH/USDT 5 500`  
   Automate gradual investments in your chosen cryptocurrency.

4. **Check Balance**: `/balance symbol`  
   Example: `/balance USDT`  
   View your available and total balance for a specific asset.

5. **Portfolio Value**: `/portfolio`  
   Get the total value of your portfolio in USDT, including all assets.

## 🛠️ How It Works
1. **Setup**:
   - Link your exchange account (e.g., Binance) using API keys.
   - Configure strategies like Grid or DCA based on your trading plan.

2. **Execute Trades**:
   - Use Telegram commands to deploy strategies directly to the exchange.
   - Monitor your balance and portfolio in real-time.

3. **Analyze Performance**:
   - Review portfolio performance with live updates.
   - Refine strategies as needed for better results.

## 📦 Installation
Follow these steps to set up CryptoTradeMate on your system:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Cryptotrademate/cryptotrademate-trading-bot.git
   cd cryptotrademate-trading-bot
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your credentials:
   ```
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   BINANCE_API_KEY=your-binance-api-key
   BINANCE_API_SECRET=your-binance-api-secret
   ```

5. **Run the Bot**:
   ```bash
   python bot.py
   ```
   
## 🤖 Usage Guide
- Open your Telegram app and start the bot using the `/start` command.
- Follow the inline menu or type commands directly for trading, balance checks, and portfolio monitoring.
- Ensure sufficient funds are available in your exchange account before placing orders.

## 🔒 Security
- Your API keys are securely stored locally and are not shared with any third party.
- Ensure you use restricted API keys (e.g., trading and balance read-only permissions).

## 🛡️ Disclaimer
Crypto trading involves risk, and past performance does not indicate future results. CryptoTradeMate is designed to assist traders with decision-making but does not offer financial advice. Please trade responsibly.

## 🌟 Contributions
Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit a pull request. 

## 📧 Customization and Contact Us
Want a customized trading bot tailored to your unique requirements? We offer:

Custom strategy integration.
Private exchange support.
White-label solutions for businesses.

Contact Us
For any inquiries or support, please reach out to us:
- 🌐 Website: [CryptoTradeMate](https://cryptotrademate.com)
- 📧 Email: support@cryptotrademate.com

## **Support the Project**

Your support helps us improve and expand this tool:
- ⭐ **Star this repository** to show your appreciation!

## **License**

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

Happy trading!
