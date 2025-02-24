import asyncio
from discord_ai_bot.config.config import BotConfig
from discord_ai_bot.bot.bot import AIBot
import os
from dotenv import load_dotenv

def main():
    # 檢查 .env 檔案
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
    print(f"Looking for .env at: {env_path}")
    print(f"File exists: {os.path.exists(env_path)}")
    
    # 載入環境變數
    load_dotenv()
    
    # 調試輸出
    print("Environment variables:")
    print(f"DISCORD_TOKEN: {bool(os.getenv('DISCORD_TOKEN'))}")
    print(f"CLAUDE_API_KEY: {bool(os.getenv('CLAUDE_API_KEY'))}")
    print(f"GEMINI_API_KEY: {bool(os.getenv('GEMINI_API_KEY'))}")
    print(f"DEEPSEEK_API_KEY: {bool(os.getenv('DEEPSEEK_API_KEY'))}")
    
    # 建立設定
    config = BotConfig(
        discord_token=os.getenv("DISCORD_TOKEN"),
        claude_api_key=os.getenv("CLAUDE_API_KEY"),
        gemini_api_key=os.getenv("GEMINI_API_KEY"),
        deepseek_api_key=os.getenv("DEEPSEEK_API_KEY")
    )
    
    # 建立並啟動bot
    bot = AIBot(config)
    bot.run(config.discord_token)

if __name__ == "__main__":
    main() 