# 🤖 Telegram Bot

A feature-rich Telegram bot built with Python and the `python-telegram-bot` library.

## 🚀 Features

- **Command Handling**: Multiple commands with comprehensive functionality
- **Inline Keyboards**: Interactive buttons for better user experience
- **Message Processing**: Intelligent responses to user messages
- **File Handling**: Support for photos and documents
- **Error Handling**: Robust error handling and logging
- **Modular Design**: Clean, organized code structure

## 📋 Available Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message and bot introduction |
| `/help` | Show all available commands |
| `/about` | Information about the bot |
| `/time` | Get current date and time |
| `/echo [message]` | Echo back your message |
| `/menu` | Show interactive menu with buttons |

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configuration

The bot token is already configured in the `.env` file:
```
BOT_TOKEN=5384719653:AAFQhoSt8G6d4SZoecKhOG3D5KrCtIr4JOk
```

### 3. Run the Bot

#### Option 1: Simple Run
```bash
python telegram_bot.py
```

#### Option 2: Using the Run Script (Recommended)
```bash
python run_bot.py
```

The run script will:
- Check if all requirements are installed
- Verify the bot token configuration
- Install missing dependencies automatically
- Launch the bot with proper error handling

## 📱 How to Use

1. **Start a conversation** with your bot on Telegram
2. **Send `/start`** to see the welcome message
3. **Use commands** like `/help`, `/time`, `/menu`
4. **Try interactive features** using the inline keyboards
5. **Send regular messages** and the bot will respond intelligently

## 🎯 Bot Capabilities

### Text Messages
- Responds to greetings, questions, and general messages
- Provides contextual responses based on message content
- Supports both private chats and group conversations

### Interactive Features
- **Inline Keyboards**: Quick access to common functions
- **Callback Handling**: Responsive button interactions
- **Menu System**: Organized command structure

### File Support
- **Photos**: Acknowledges and processes image uploads
- **Documents**: Provides information about uploaded files
- **Future Enhancement Ready**: Easy to extend for file processing

## 🔧 Technical Details

### Architecture
- **Framework**: python-telegram-bot v20.7
- **Language**: Python 3.x
- **Design Pattern**: Object-oriented with handler separation
- **Logging**: Comprehensive logging system for debugging

### Key Components
- `TelegramBot` class: Main bot logic and handler setup
- Command handlers: Individual functions for each command
- Message handlers: Processing different types of messages
- Error handling: Graceful error management and logging

### Dependencies
```
python-telegram-bot==20.7  # Main Telegram bot framework
python-dotenv==1.0.0       # Environment variable management
requests==2.31.0           # HTTP requests (for future features)
```

## 🔐 Security Notes

- **Token Protection**: Bot token is stored in `.env` file (excluded from git)
- **Environment Variables**: Secure configuration management
- **Error Handling**: No sensitive information exposed in error messages

## 📈 Extending the Bot

The bot is designed for easy extension. You can add new features by:

1. **Adding new commands**: Create new handler functions
2. **Enhancing message processing**: Modify the `handle_message` method
3. **Adding new file types**: Create handlers for specific file formats
4. **Database integration**: Add persistence for user data
5. **External APIs**: Integrate with third-party services

### Example: Adding a New Command

```python
async def weather_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /weather command"""
    # Your weather API integration here
    await update.message.reply_text("🌤️ Weather information feature coming soon!")

# Add to setup_handlers method:
self.application.add_handler(CommandHandler("weather", self.weather_command))
```

## 🐛 Troubleshooting

### Common Issues

1. **Bot not responding**:
   - Check if the bot token is correct
   - Ensure the bot is not already running elsewhere
   - Verify internet connection

2. **Import errors**:
   - Run `pip install -r requirements.txt`
   - Check Python version (3.7+ required)

3. **Token issues**:
   - Verify the token in the `.env` file
   - Ensure no extra spaces or characters

### Logs
The bot generates detailed logs to help with debugging. Check the console output for error messages and status updates.

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the logs for error details
3. Verify the bot configuration
4. Test with simple commands first

## 📄 License

This project is open source and available under the MIT License.

---

**Happy botting! 🤖✨**