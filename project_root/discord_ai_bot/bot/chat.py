from typing import Dict, List, Optional
from ..models.base import BaseAIModel
from ..utils.exceptions import ChatHistoryException

class ChatManager:
    """管理聊天相關功能的類別"""
    
    def __init__(self, max_history: int = 10):
        self.max_history = max_history
        self.histories: Dict[int, List[Dict[str, str]]] = {}
    
    def add_message(self, channel_id: int, role: str, content: str):
        """新增訊息到歷史記錄"""
        if channel_id not in self.histories:
            self.histories[channel_id] = []
            
        history = self.histories[channel_id]
        history.append({"role": role, "content": content})
        
        # 限制歷史記錄長度
        if len(history) > self.max_history * 2:
            history = history[-self.max_history * 2:]
            self.histories[channel_id] = history
    
    def get_history(self, channel_id: int) -> List[Dict[str, str]]:
        """取得特定頻道的對話歷史"""
        return self.histories.get(channel_id, [])
    
    def clear_history(self, channel_id: int):
        """清除特定頻道的對話歷史"""
        if channel_id in self.histories:
            del self.histories[channel_id] 