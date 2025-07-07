# 从langchain.llms.fake模块导入FakeListLLM类，此类可能用于模拟或伪造某种行为
# from langchain_community.llms import FakeListLLM
from langchain_community.llms import FakeListLLM
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

# 调用load_tools函数，加载"python_repl"的工具
tools = load_tools(["python_repl"])
# 定义一个响应列表，这些响应可能是模拟LLM的预期响应
responses = ["Action: Python REPL\nAction Input: print(2 + 2)", "Final Answer: 4"]
# 使用上面定义的responses初始化一个FakeListLLM对象
llm = FakeListLLM(responses=responses)
# 调用initialize_agent函数，使用上面的tools和llm，以及指定的代理类型和verbose参数来初始化一个代理
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)
# 调用代理的run方法，传递字符串"whats 2 + 2"作为输入，询问代理2加2的结果
agent.run("whats 2 + 2")
