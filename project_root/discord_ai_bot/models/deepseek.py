from typing import List, Dict, Optional
import requests
from .base import BaseAIModel
from ..utils.exceptions import AIModelException

class DeepseekAIModel(BaseAIModel):
    def __init__(self, api_key: str, model: str = "deepseek-chat"):
        self.api_key = api_key
        self.model = model
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        
    async def generate_response(self,
                              message: str,
                              chat_history: Optional[List[Dict[str, str]]] = None) -> str:
        try:
            # 構建請求標頭
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            # 構建訊息歷史
            messages = []
            if chat_history:
                for msg in chat_history:
                    role = "user" if msg["role"] == "user" else "assistant"
                    messages.append({"role": role, "content": msg["content"]})
            
            # 添加當前訊息
            messages.append({"role": "user", "content": message})
            
            # 構建請求內容
            data = {
                "model": self.model,
                "messages": messages,
                "max_tokens": 1000
            }
            
            # 發送請求
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            
            # 解析回應
            result = response.json()
            return result["choices"][0]["message"]["content"]
            
        except requests.exceptions.RequestException as e:
            raise AIModelException(f"Deepseek API error: {str(e)}")
        except Exception as e:
            raise AIModelException(f"Unexpected error: {str(e)}")
    
    async def is_available(self) -> bool:
        try:
            # 簡單的API測試
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": self.model,
                "messages": [{"role": "user", "content": "test"}],
                "max_tokens": 1
            }
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            return True
        except:
            return False 