#使用 jinja2 模板：
from langchain.prompts import PromptTemplate
jinja2_template = "Tell me a {{ adjective }} joke about {{ content }}"
prompt = PromptTemplate.from_template(jinja2_template, template_format="jinja2")
print(prompt.format(adjective="funny", content="chickens"))
# Output: Tell me a funny joke about chickens.