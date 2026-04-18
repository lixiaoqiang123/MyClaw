"""工具模块测试。"""

from myclaw.tools import calculator, get_all_tools, get_weather


def test_calculator_evaluates_basic_math_expression():
    assert calculator.invoke({"expression": "2 + 3 * 4"}) == "计算结果: 14"


def test_calculator_rejects_non_math_expression():
    result = calculator.invoke({"expression": "__import__('os').system('echo unsafe')"})

    assert result.startswith("计算错误:")


def test_get_weather_returns_known_city_weather():
    assert get_weather.invoke({"city": "北京"}) == "晴天，温度 15-25°C"


def test_get_all_tools_returns_registered_tools():
    assert [tool.name for tool in get_all_tools()] == ["calculator", "get_weather"]
