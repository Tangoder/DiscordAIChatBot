from typing import List, Dict, Optional
import anthropic
import asyncio
from .base import BaseAIModel
from ..utils.exceptions import AIModelException

class ClaudeAIModel(BaseAIModel):
    def __init__(self, api_key: str, model: str = "claude-3-opus-20240229"):
        self.client = anthropic.AsyncAnthropic(api_key=api_key)
        self.model = model
        
    async def generate_response(self, 
                              message: str,
                              chat_history: Optional[List[Dict[str, str]]] = None) -> str:
        try:
            # 構建完整的對話歷史
            messages = []
            if chat_history:
                for msg in chat_history:
                    role = "user" if msg["role"] == "user" else "assistant"
                    messages.append({"role": role, "content": msg["content"]})
            
            # 添加當前訊息
            messages.append({"role": "user", "content": message})
            
            # 呼叫API
            response = await self.client.messages.create(
                model=self.model,
                messages=messages,
                max_tokens=1024
            )
            
            return response.content
            
        except anthropic.APIError as e:
            raise AIModelException(f"Claude API error: {str(e)}")
        except Exception as e:
            raise AIModelException(f"Unexpected error: {str(e)}")
    
    async def is_available(self) -> bool:
        try:
            # 簡單的API測試
            await self.client.messages.create(
                model=self.model,
                messages=[{"role": "user", "content": "test"}],
                max_tokens=1
            )
            return True
        except:
            return False 