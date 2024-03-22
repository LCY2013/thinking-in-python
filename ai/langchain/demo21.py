from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2, cache=None)

with get_openai_callback() as cb:
    result = llm("讲个笑话")
    print(cb)
