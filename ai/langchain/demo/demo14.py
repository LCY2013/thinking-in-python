from langchain.llms import OpenAI

llm = OpenAI()
print(llm('你是谁'))

llm_result = llm.generate(["给我背诵一首古诗", "给我讲个100字小故事"]*10)
print(llm_result)



