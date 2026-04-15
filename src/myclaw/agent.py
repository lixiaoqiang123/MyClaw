"""Agent 执行循环模块 - ReAct 模式实现"""

from typing import List, Optional
from langchain_core.messages import BaseMessage, ToolMessage

from .llm import LLMClient
from .memory import ConversationMemory
from .tools import get_all_tools


class ReActAgent:
    """ReAct 模式 Agent - 思考→行动→观察循环"""
    
    def __init__(
        self,
        llm_client: Optional[LLMClient] = None,
        system_message: Optional[str] = None,
        max_iterations: int = 5
    ):
        """初始化 Agent
        
        Args:
            llm_client: LLM 客户端
            system_message: 系统提示词
            max_iterations: 最大迭代次数
        """
        self.llm_client = llm_client or LLMClient()
        self.memory = ConversationMemory(system_message=system_message)
        self.tools = get_all_tools()
        self.max_iterations = max_iterations
        
        # 绑定工具到 LLM
        self.llm_with_tools = self.llm_client.chat_model.bind_tools(self.tools)
    
    def run(self, user_input: str) -> str:
        """执行 Agent 循环
        
        Args:
            user_input: 用户输入
        
        Returns:
            Agent 的最终响应
        """
        # 添加用户消息
        self.memory.add_user_message(user_input)
        
        # ReAct 循环
        for iteration in range(self.max_iterations):
            # 调用 LLM
            response = self.llm_with_tools.invoke(self.memory.get_messages())
            self.memory.add_message(response)
            
            # 检查是否有工具调用
            if not response.tool_calls:
                # 没有工具调用，返回最终响应
                return response.content
            
            # 执行工具调用
            for tool_call in response.tool_calls:
                tool_result = self._execute_tool(tool_call)
                
                # 添加工具执行结果
                tool_message = ToolMessage(
                    content=tool_result,
                    tool_call_id=tool_call["id"]
                )
                self.memory.add_message(tool_message)
        
        # 达到最大迭代次数，返回最后的响应
        final_response = self.llm_client.invoke(self.memory.get_messages())
        return final_response.content
    
    def _execute_tool(self, tool_call: dict) -> str:
        """执行工具调用
        
        Args:
            tool_call: 工具调用信息
        
        Returns:
            工具执行结果
        """
        tool_name = tool_call["name"]
        tool_args = tool_call["args"]
        
        # 查找对应的工具
        for tool in self.tools:
            if tool.name == tool_name:
                try:
                    result = tool.invoke(tool_args)
                    return str(result)
                except Exception as e:
                    return f"工具执行错误: {str(e)}"
        
        return f"未找到工具: {tool_name}"
    
    def clear_history(self):
        """清空对话历史"""
        self.memory.clear()
