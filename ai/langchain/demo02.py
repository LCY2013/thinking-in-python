#使用 Python f 字符串模板：
from langchain.prompts import PromptTemplate
fstring_template = """Tell me a {adjective} joke about {content}"""
prompt = PromptTemplate.from_template(fstring_template)
print(prompt.format(adjective="funny", content="chickens"))
# Output: Tell me a funny joke about chickens.