"""工具定义与注册模块"""

from typing import List
from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """计算数学表达式
    
    Args:
        expression: 要计算的数学表达式，例如 "2 + 3 * 4"
    
    Returns:
        计算结果
    """
    try:
        result = eval(expression)
        return f"计算结果: {result}"
    except Exception as e:
        return f"计算错误: {str(e)}"


@tool
def get_weather(city: str) -> str:
    """查询城市天气（模拟）
    
    Args:
        city: 城市名称
    
    Returns:
        天气信息
    """
    # 这里是模拟数据，实际应该调用天气 API
    weather_data = {
        "北京": "晴天，温度 15-25°C",
        "上海": "多云，温度 18-28°C",
        "深圳": "阴天，温度 22-30°C"
    }
    
    return weather_data.get(city, f"{city} 的天气信息暂不可用")


def get_all_tools() -> List:
    """获取所有可用工具"""
    return [calculator, get_weather]
