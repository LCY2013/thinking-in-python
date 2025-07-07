import os
import openai
import asyncio
from langchain_openai import OpenAI

# 设置代理
openai.proxy = os.getenv('https_proxy')


# 定义一个同步方式生成文本的函数
def generate_serially():
    llm = OpenAI(temperature=0.9)  # 创建OpenAI对象，并设置temperature参数为0.9
    for _ in range(10):  # 循环10次
        resp = llm.generate(["Hello, how are you?"])  # 调用generate方法生成文本
        print(resp.generations[0][0].text)  # 打印生成的文本


# 定义一个异步生成文本的函数
async def async_generate(llm):
    resp = await llm.agenerate(["Hello, how are you?"])  # 异步调用agenerate方法生成文本
    print(resp.generations[0][0].text)  # 打印生成的文本


# 定义一个并发（异步）方式生成文本的函数
async def generate_concurrently():
    llm = OpenAI(temperature=0.9)  # 创建OpenAI对象，并设置temperature参数为0.9
    tasks = [async_generate(llm) for _ in range(10)]  # 创建10个异步任务
    await asyncio.gather(*tasks)  # 使用asyncio.gather等待所有异步任务完成
