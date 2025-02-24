from abc import ABC, abstractmethod
from typing import List, Dict

class BaseAIModel(ABC):
    """AI 模型的基礎類別"""
    
    @abstractmethod
    async def generate_response(self, 
                              message: str,
                              chat_history: List[Dict[str, str]] = None) -> str:
        """生成回應"""
        pass
    
    @abstractmethod
    async def is_available(self) -> bool:
        """檢查服務是否可用"""
        pass 