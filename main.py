"""MyClaw Agent 运行示例"""

import sys

from myclaw.agent import ReActAgent


def main():
    """主函数"""
    # 创建 Agent 实例
    try:
        agent = ReActAgent(
            system_message="你是一个 helpful 的 AI 助手，可以帮助用户进行计算和查询天气。",
            max_iterations=5,
        )
    except ValueError as e:
        print(f"配置错误: {e}")
        print("请在项目根目录创建 .env 文件，或设置系统环境变量，例如：")
        print("OPENAI_API_KEY=你的 API Key")
        print("可选配置: BASE_URL、MODEL_NAME、TEMPERATURE、MAX_TOKENS")
        return 1

    print("MyClaw Agent 已启动！")
    print("可用工具: 计算器、天气查询")
    print("输入 'quit' 或 'exit' 退出\n")

    # 交互循环
    while True:
        try:
            user_input = input("你: ").strip()

            if user_input.lower() in ["quit", "exit", "退出"]:
                print("再见！")
                break

            if not user_input:
                continue

            # 运行 Agent
            response = agent.run(user_input)
            print(f"\nAgent: {response}\n")

        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"\n错误: {str(e)}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
