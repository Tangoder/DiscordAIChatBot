from dataclasses import dataclass
from typing import Optional

@dataclass
class BotConfig:
    # Discord 設定
    discord_token: str
    command_prefix: str = "!"
    
    # API Keys
    claude_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    deepseek_api_key: Optional[str] = None
    
    # 聊天設定
    max_history: int = 10  # 保留的對話歷史數量
    timeout: int = 30      # API 超時時間(秒)
    
    # 模型設定
    default_model: str = "deepseek"  # 預設使用的模型
    fallback_model: str = "gemini" # 備用模型 