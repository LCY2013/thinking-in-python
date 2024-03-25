from langchain.prompts import load_prompt

prompt = load_prompt("./simple_prompt.json")
print(prompt.format(adjective="funny", content="chickens"))