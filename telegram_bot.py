#!/usr/bin/env python3
"""
Telegram Bot Implementation
A feature-rich Telegram bot with various commands and functionality.
"""

import logging
import os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, 
    CommandHandler, 
    MessageHandler, 
    filters, 
    ContextTypes,
    CallbackQueryHandler
)
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN')

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found in environment variables!")

class TelegramBot:
    def __init__(self):
        self.application = Application.builder().token(BOT_TOKEN).build()
        self.setup_handlers()
    
    def setup_handlers(self):
        """Set up all command and message handlers"""
        # Command handlers
        self.application.add_handler(CommandHandler("start", self.start_command))
        self.application.add_handler(CommandHandler("help", self.help_command))
        self.application.add_handler(CommandHandler("about", self.about_command))
        self.application.add_handler(CommandHandler("time", self.time_command))
        self.application.add_handler(CommandHandler("echo", self.echo_command))
        self.application.add_handler(CommandHandler("menu", self.menu_command))
        
        # Callback query handler for inline buttons
        self.application.add_handler(CallbackQueryHandler(self.button_callback))
        
        # Message handler for regular text messages
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        
        # Handler for photos
        self.application.add_handler(MessageHandler(filters.PHOTO, self.handle_photo))
        
        # Handler for documents
        self.application.add_handler(MessageHandler(filters.Document.ALL, self.handle_document))
    
    async def start_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /start command"""
        user = update.effective_user
        welcome_message = f"""
🤖 **Welcome to the Bot, {user.first_name}!**

I'm a feature-rich Telegram bot ready to assist you!

**Available Commands:**
• /help - Show all available commands
• /about - Learn more about this bot
• /time - Get current time
• /echo [message] - Echo your message
• /menu - Show interactive menu

Just type a command or send me a message to get started! 🚀
        """
        
        # Create inline keyboard
        keyboard = [
            [InlineKeyboardButton("📚 Help", callback_data="help")],
            [InlineKeyboardButton("ℹ️ About", callback_data="about")],
            [InlineKeyboardButton("🕒 Current Time", callback_data="time")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            welcome_message, 
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /help command"""
        help_text = """
📋 **Available Commands:**

🔸 **/start** - Welcome message and bot introduction
🔸 **/help** - Show this help message
🔸 **/about** - Information about the bot
🔸 **/time** - Get current date and time
🔸 **/echo [message]** - Echo back your message
🔸 **/menu** - Show interactive menu

📝 **Other Features:**
• Send me any text message and I'll respond
• Send photos and I'll tell you about them
• Send documents and I'll provide info
• Use inline buttons for quick actions

💡 **Tips:**
- All commands work in private chats and groups
- Bot responds to mentions in groups
- Use /echo followed by text to make me repeat it
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')
    
    async def about_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /about command"""
        about_text = """
🤖 **About This Bot**

**Name:** Advanced Telegram Bot
**Version:** 1.0.0
**Language:** Python 3.x
**Framework:** python-telegram-bot

**Features:**
✅ Command handling
✅ Inline keyboards
✅ Message processing
✅ File handling
✅ Error handling
✅ Logging system

**Developer:** Your Bot Team
**Created:** 2024

This bot demonstrates various Telegram Bot API features and serves as a foundation for more advanced functionality.

🔗 **Useful Links:**
• [Telegram Bot API](https://core.telegram.org/bots/api)
• [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
        """
        await update.message.reply_text(about_text, parse_mode='Markdown')
    
    async def time_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /time command"""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time_message = f"🕒 **Current Time:** `{current_time}`"
        await update.message.reply_text(time_message, parse_mode='Markdown')
    
    async def echo_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /echo command"""
        if context.args:
            echo_text = ' '.join(context.args)
            await update.message.reply_text(f"🔄 **Echo:** {echo_text}")
        else:
            await update.message.reply_text("Please provide a message to echo. Usage: `/echo your message here`", parse_mode='Markdown')
    
    async def menu_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle the /menu command with inline keyboard"""
        keyboard = [
            [InlineKeyboardButton("🕒 Time", callback_data="time"), InlineKeyboardButton("📚 Help", callback_data="help")],
            [InlineKeyboardButton("ℹ️ About", callback_data="about"), InlineKeyboardButton("👋 Greet", callback_data="greet")],
            [InlineKeyboardButton("🎲 Random Fact", callback_data="fact")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            "🎯 **Bot Menu**\n\nChoose an option from the menu below:",
            parse_mode='Markdown',
            reply_markup=reply_markup
        )
    
    async def button_callback(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle inline button callbacks"""
        query = update.callback_query
        await query.answer()
        
        user = query.from_user
        
        if query.data == "help":
            help_text = """
📋 **Quick Help:**
• Use /start to begin
• Send any message for a response
• Try /menu for interactive options
• Use /echo to repeat messages
            """
            await query.edit_message_text(help_text, parse_mode='Markdown')
        
        elif query.data == "about":
            about_text = """
🤖 **Bot Information:**
This is a demonstration Telegram bot built with Python and the python-telegram-bot library. It showcases various bot features and capabilities.
            """
            await query.edit_message_text(about_text, parse_mode='Markdown')
        
        elif query.data == "time":
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            await query.edit_message_text(f"🕒 **Current Time:** `{current_time}`", parse_mode='Markdown')
        
        elif query.data == "greet":
            greeting = f"👋 Hello {user.first_name}! Thanks for using the bot!"
            await query.edit_message_text(greeting)
        
        elif query.data == "fact":
            facts = [
                "🎯 The first computer bug was an actual bug - a moth trapped in a Harvard computer in 1947!",
                "🌐 The Internet was originally called ARPANET.",
                "💾 The first 1GB hard drive cost $40,000 in 1980.",
                "🤖 The term 'robot' comes from the Czech word 'robota' meaning forced labor.",
                "📱 There are more mobile devices than people on Earth!"
            ]
            import random
            fact = random.choice(facts)
            await query.edit_message_text(f"🎲 **Random Tech Fact:**\n\n{fact}")
    
    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle regular text messages"""
        user_message = update.message.text.lower()
        user = update.effective_user
        
        # Simple response logic
        if "hello" in user_message or "hi" in user_message:
            response = f"👋 Hello {user.first_name}! How can I help you today?"
        elif "how are you" in user_message:
            response = "🤖 I'm doing great! Thanks for asking. How are you?"
        elif "thank" in user_message:
            response = "😊 You're welcome! Happy to help!"
        elif "bye" in user_message or "goodbye" in user_message:
            response = "👋 Goodbye! Feel free to come back anytime!"
        elif "help" in user_message:
            response = "📚 Use /help to see all available commands, or /menu for interactive options!"
        else:
            response = f"💬 I received your message: '{update.message.text}'\n\nTry using /help to see what I can do!"
        
        await update.message.reply_text(response)
    
    async def handle_photo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle photo messages"""
        await update.message.reply_text("📸 Nice photo! I can see you sent me an image. Photo processing features can be added here!")
    
    async def handle_document(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle document messages"""
        file_name = update.message.document.file_name
        file_size = update.message.document.file_size
        await update.message.reply_text(f"📄 Document received!\n\n**File:** {file_name}\n**Size:** {file_size} bytes")
    
    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        logger.warning(f'Update {update} caused error {context.error}')
    
    def run(self):
        """Start the bot"""
        # Add error handler
        self.application.add_error_handler(self.error_handler)
        
        print("🤖 Bot is starting...")
        print(f"📋 Bot Token: {BOT_TOKEN[:10]}...")
        print("✅ Bot is running! Press Ctrl+C to stop.")
        
        # Start the bot
        self.application.run_polling(drop_pending_updates=True)

def main():
    """Main function to run the bot"""
    try:
        bot = TelegramBot()
        bot.run()
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Error: {e}")
        logger.error(f"Bot error: {e}")

if __name__ == "__main__":
    main()