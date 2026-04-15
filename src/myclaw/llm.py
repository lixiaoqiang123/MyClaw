"""LLM 交互模块 - 封装 LangChain ChatModel"""

from typing import List, Optional
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI

from .config import config


class LLMClient:
    """LLM 客户端封装"""
    
    def __init__(self, model_name: Optional[str] = None, temperature: Optional[float] = None):
        """初始化 LLM 客户端"""
        self.model_name = model_name or config.model_name
        self.temperature = temperature or config.temperature
        
        self.chat_model = ChatOpenAI(
            model=self.model_name,
            temperature=self.temperature,
            api_key=config.api_key
        )
    
    def invoke(self, messages: List[BaseMessage]) -> AIMessage:
        """调用 LLM 获取响应"""
        return self.chat_model.invoke(messages)
    
    def stream(self, messages: List[BaseMessage]):
        """流式调用 LLM"""
        return self.chat_model.stream(messages)
