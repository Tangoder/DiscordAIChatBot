from typing import List, Dict, Optional
import google.generativeai as genai
from .base import BaseAIModel
from ..utils.exceptions import AIModelException

class GeminiAIModel(BaseAIModel):
    def __init__(self, api_key: str, model: str = "gemini-pro"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
        
    async def generate_response(self,
                              message: str,
                              chat_history: Optional[List[Dict[str, str]]] = None) -> str:
        try:
            # 建立新的對話
            chat = self.model.start_chat()
            
            # 添加歷史對話
            if chat_history:
                for msg in chat_history:
                    role = msg["role"]
                    content = msg["content"]
                    if role == "user":
                        chat.send_message(content)
            
            # 發送當前訊息並取得回應
            response = chat.send_message(message)
            return response.text
            
        except Exception as e:
            raise AIModelException(f"Gemini API error: {str(e)}")
    
    async def is_available(self) -> bool:
        try:
            chat = self.model.start_chat()
            response = chat.send_message("test")
            return True
        except:
            return False 