from datetime import datetime

from langchain_core.prompts import PromptTemplate


def _get_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y, %H:%M:%S")

prompt = PromptTemplate(
      template="Tell me a {adjective} joke about the day {date}",
      input_variables=["adjective", "date"]
)
partial_prompt = prompt.partial(date=_get_datetime)
print(partial_prompt.format(adjective="funny"))

# 除上述方法，部分函数声明和普通的prompt一样，也可以直接用partial_variables去声明
prompt = PromptTemplate(
template="Tell me a {adjective} joke about the day {date}",
input_variables=["adjective"],
partial_variables={"date": _get_datetime})