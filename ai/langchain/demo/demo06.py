from langchain.prompts import PromptTemplate
prompt = PromptTemplate(template="{foo}{bar}", input_variables=["foo", "bar"])

# 可以使用 PromptTemplate.partial() 方法创建部分提示模板。
partial_prompt = prompt.partial(foo="foo")
print(partial_prompt.format(bar="baz"))

#也可以只使用分部变量初始化提示。
prompt = PromptTemplate(template="{foo}{bar}", input_variables=["bar"], partial_variables={"foo": "foo"})
print(prompt.format(bar="baz"))