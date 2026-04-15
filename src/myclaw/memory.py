"""对话历史管理模块"""

from typing import List, Optional
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage


class ConversationMemory:
    """对话记忆管理"""
    
    def __init__(self, system_message: Optional[str] = None, max_history: int = 10):
        """初始化对话记忆
        
        Args:
            system_message: 系统提示词
            max_history: 最大保留的历史消息数量
        """
        self.messages: List[BaseMessage] = []
        self.max_history = max_history
        
        if system_message:
            self.messages.append(SystemMessage(content=system_message))
    
    def add_user_message(self, content: str):
        """添加用户消息"""
        self.messages.append(HumanMessage(content=content))
        self._trim_history()
    
    def add_ai_message(self, content: str):
        """添加 AI 消息"""
        self.messages.append(AIMessage(content=content))
        self._trim_history()
    
    def add_message(self, message: BaseMessage):
        """添加任意类型消息"""
        self.messages.append(message)
        self._trim_history()
    
    def get_messages(self) -> List[BaseMessage]:
        """获取所有消息"""
        return self.messages
    
    def clear(self):
        """清空历史（保留系统消息）"""
        system_messages = [msg for msg in self.messages if isinstance(msg, SystemMessage)]
        self.messages = system_messages
    
    def _trim_history(self):
        """修剪历史消息，保持在最大数量内"""
        if len(self.messages) > self.max_history:
            # 保留系统消息和最近的消息
            system_messages = [msg for msg in self.messages if isinstance(msg, SystemMessage)]
            other_messages = [msg for msg in self.messages if not isinstance(msg, SystemMessage)]
            
            if len(other_messages) > self.max_history - len(system_messages):
                other_messages = other_messages[-(self.max_history - len(system_messages)):]
            
            self.messages = system_messages + other_messages
