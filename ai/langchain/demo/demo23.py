from langchain.llms.loading import load_llm

llm = load_llm("llm.json")

llm.save("llmsave.json")
