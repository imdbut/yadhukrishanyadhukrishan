#!/usr/bin/env python3
"""
Simple script to run the Telegram bot
"""

import subprocess
import sys
import os

def check_requirements():
    """Check if required packages are installed"""
    try:
        import telegram
        import dotenv
        print("✅ All required packages are installed!")
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("📦 Installing requirements...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Requirements installed successfully!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install requirements. Please install manually:")
            print("pip install -r requirements.txt")
            return False

def check_token():
    """Check if bot token is configured"""
    from dotenv import load_dotenv
    load_dotenv()
    
    token = os.getenv('BOT_TOKEN')
    if not token:
        print("❌ Bot token not found!")
        print("📝 Please make sure your .env file contains:")
        print("BOT_TOKEN=your_bot_token_here")
        return False
    
    print(f"✅ Bot token configured: {token[:10]}...")
    return True

def main():
    """Main function to run the bot with checks"""
    print("🚀 Starting Telegram Bot...")
    print("=" * 50)
    
    # Check requirements
    if not check_requirements():
        return
    
    # Check token
    if not check_token():
        return
    
    # Run the bot
    print("\n🤖 Launching bot...")
    try:
        from telegram_bot import main as run_bot
        run_bot()
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped by user")
    except Exception as e:
        print(f"❌ Error running bot: {e}")

if __name__ == "__main__":
    main()