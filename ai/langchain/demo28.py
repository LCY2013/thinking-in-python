# 导入所需的库和模块
from langchain.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from typing import List


# 定义一个表示演员的数据结构，包括他们的名字和他们出演的电影列表
class Actor(BaseModel):
    name: str = Field(description="name of an actor")  # 演员的名字
    film_names: List[str] = Field(description="list of names of films they starred in")  # 他们出演的电影列表


# 定义一个查询，用于提示生成随机演员的电影作品列表
actor_query = "Generate the filmography for a random actor."

# 使用`Actor`模型初始化解析器
parser = PydanticOutputParser(pydantic_object=Actor)

# 定义一个格式错误的字符串数据
misformatted = "{'name': 'Tom Hanks', 'film_names': ['Forrest Gump']}"

# 使用解析器尝试解析上述数据
try:
    parsed_data = parser.parse(misformatted)
except Exception as e:
    print(f"Error: {e}")
