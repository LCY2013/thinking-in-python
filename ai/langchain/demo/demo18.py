# 从langchain.llms.human模块导入HumanInputLLM类，此类可能允许人类输入或交互来模拟LLM的行为
from langchain.llms.human import HumanInputLLM
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType

# 调用load_tools函数，加载名为"wikipedia"的工具
tools = load_tools(["wikipedia"])

# 初始化一个HumanInputLLM对象，其中prompt_func是一个函数，用于打印提示信息
llm = HumanInputLLM(
    prompt_func=lambda prompt: print(f"\n===PROMPT====\n{prompt}\n=====END OF PROMPT======"))
# 调用initialize_agent函数，使用上面的tools和llm，以及指定的代理类型和verbose参数来初始化一个代理
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
# 调用代理的run方法，传递字符串"What is 'Bocchi the Rock!'?"作为输入，询问代理关于'Bocchi the Rock!'的信息
agent.run("What is 'Bocchi the Rock!'?")
