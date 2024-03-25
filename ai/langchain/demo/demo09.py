import inspect

from langchain.prompts import StringPromptTemplate
from pydantic.v1 import BaseModel, validator


# 该函数将返回给定其名称的函数的源代码。 inspect作用就是获取源代码
def get_source_code(function_name):
    # Get the source code of the function
    return inspect.getsource(function_name)


# 测试函数
def add_test():
    return 1 + 1


# 初始化字符串prompt
PROMPT = """\
提供一个函数名和源代码并给出函数的相应解释
函数名: {function_name}
源代码:
{source_code}
解释:
"""


class FunctionExplainerPromptTemplate(StringPromptTemplate, BaseModel):
    """一个自定义提示模板，以函数名作为输入，并格式化提示模板以提供函数的源代码。 """
    @validator("input_variables")
    def validate_input_variables(self, v, values, config, field):
        """验证输入变量是否正确。"""
        if len(v) != 1 or "function_name" not in v:
            raise ValueError("函数名必须是唯一的输入变量。")
        return v

    def format(self, **kwargs) -> str:
        # 获取源代码
        source_code = get_source_code(kwargs["function_name"])
        # 源代码+名字提供给prompt
        prompt = PROMPT.format(
            function_name=kwargs["function_name"].__name__, source_code=source_code)
        return prompt

    def _prompt_type(self):
        return "function-explainer"


# 初始化prompt实例
fn_explainer = FunctionExplainerPromptTemplate(input_variables=["function_name"])


# 定义函数 test_add
def add():
    return 1 + 1


# Generate a prompt for the function "test_add"
prompt_1 = fn_explainer.format(function_name=add)
print(prompt_1)
