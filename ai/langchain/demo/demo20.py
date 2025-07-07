from langchain.cache import SQLiteCache
import langchain
from langchain_openai import OpenAI
import time

langchain.llm_cache = SQLiteCache(database_path=".langchain.db")

llm = OpenAI(model_name="text-davinci-002", n=2, best_of=2)

start_time = time.time()  # 记录开始时间
print(llm.predict("用中文讲个笑话"))
end_time = time.time()  # 记录结束时间
elapsed_time = end_time - start_time  # 计算总时间
print(f"Predict method took {elapsed_time:.4f} seconds to execute.")
