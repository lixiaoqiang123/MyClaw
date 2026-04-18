<div align="center">
  <img src="assets/icon.jpg" alt="MyClaw" width="128" height="128">
  <h1>MyClaw</h1>
  <p>AI Agent 学习练手项目</p>
</div>

---

## 关于

MyClaw 是我学习 AI Agent 开发的练手项目，通过动手实践来理解和掌握 LLM 交互与工具调用的核心原理。

## 🎯 第一阶段：LLM 交互 + Tool 调用

### 学习目标

- 理解 LLM API 的调用方式和消息机制
- 掌握 Tool Calling 的原理与实现
- 实现一个能思考、调用工具、再根据结果继续推理的 Agent

### 项目结构

```
MyClaw/
├── assets/                  # 项目资源
├── src/
│   └── myclaw/
│       ├── __init__.py
│       ├── llm.py           # LLM 交互（LangChain ChatModel）
│       ├── tools.py         # 工具定义与注册（@tool）
│       ├── memory.py        # 对话历史管理
│       ├── agent.py         # Agent 执行循环（ReAct）
│       └── config.py        # 配置管理（API Key、模型等）
├── tests/                   # 测试
├── pyproject.toml
├── LICENSE
└── README.md
```

### 学习路线

| 步骤 | 内容 | 学到什么 |
|------|------|----------|
| 1 | 项目初始化 + 配置管理 | Python 项目工程化基础 |
| 2 | 封装 LLM 调用（llm.py） | LangChain ChatModel、消息类型、流式输出 |
| 3 | 定义工具（tools.py） | @tool 装饰器、工具注册、参数 schema |
| 4 | 对话记忆（memory.py） | 消息历史管理、上下文窗口 |
| 5 | Agent 执行循环（agent.py） | ReAct 模式：思考→调用工具→观察结果→继续推理 |
| 6 | 端到端联调测试 | 完整链路跑通，验证学习和实践成果 |

### 练手示例工具

- **计算器** — 验证 Tool Calling 基本链路
- **天气查询** — 验证外部 API 调用能力

### 技术栈

- Python 3.12+
- LangChain + langchain-core
- OpenAI API / Anthropic API
- pytest

### 验收标准

- [ ] 能与 LLM 进行多轮对话，保持上下文
- [ ] LLM 能自动判断何时调用工具并正确传参
- [ ] 工具执行结果能回传给 LLM 继续推理
- [ ] 至少实现 2 个示例工具

## 许可证

MIT License
