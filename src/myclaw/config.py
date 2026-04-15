"""配置管理模块 - API Key、模型等配置"""

import os
from typing import Optional


class Config:
    """配置类"""
    
    def __init__(self):
        self.api_key: Optional[str] = os.getenv("OPENAI_API_KEY")
        self.model_name: str = os.getenv("MODEL_NAME", "gpt-4")
        self.temperature: float = float(os.getenv("TEMPERATURE", "0.7"))
        self.max_tokens: int = int(os.getenv("MAX_TOKENS", "2000"))
    
    def validate(self) -> bool:
        """验证配置是否完整"""
        if not self.api_key:
            raise ValueError("API Key 未设置，请设置环境变量 OPENAI_API_KEY")
        return True


# 全局配置实例
config = Config()
