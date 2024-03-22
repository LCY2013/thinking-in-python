from langchain.prompts import PromptTemplate #用于 PromptTemplate 为字符串提示创建模板。
#默认情况下， PromptTemplate 使用 Python 的 str.format 语法进行模板化;但是可以使用其他模板语法（例如， jinja2 ）
prompt_template = PromptTemplate.from_template("Tell me a {adjective} joke about {content}.")
print(prompt_template.format(adjxective="funny", content="chickens"))