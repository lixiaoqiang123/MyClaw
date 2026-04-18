"""工具定义与注册模块"""

import ast
import operator

from langchain_core.tools import BaseTool, tool


_BINARY_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPERATORS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _evaluate_expression(node: ast.AST) -> int | float:
    if isinstance(node, ast.Expression):
        return _evaluate_expression(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            raise ValueError("只支持数字")
        return node.value

    if isinstance(node, ast.BinOp):
        operator_func = _BINARY_OPERATORS.get(type(node.op))
        if operator_func is None:
            raise ValueError("不支持的运算符")
        return operator_func(_evaluate_expression(node.left), _evaluate_expression(node.right))

    if isinstance(node, ast.UnaryOp):
        operator_func = _UNARY_OPERATORS.get(type(node.op))
        if operator_func is None:
            raise ValueError("不支持的运算符")
        return operator_func(_evaluate_expression(node.operand))

    raise ValueError("只支持基础数学表达式")


@tool
def calculator(expression: str) -> str:
    """计算数学表达式

    Args:
        expression: 要计算的数学表达式，例如 "2 + 3 * 4"

    Returns:
        计算结果
    """
    try:
        parsed_expression = ast.parse(expression, mode="eval")
        result = _evaluate_expression(parsed_expression)
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
        "深圳": "阴天，温度 22-30°C",
    }

    return weather_data.get(city, f"{city} 的天气信息暂不可用")


def get_all_tools() -> list[BaseTool]:
    """获取所有可用工具"""
    return [calculator, get_weather]
