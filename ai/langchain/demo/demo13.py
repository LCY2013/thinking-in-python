from langchain.prompts import load_prompt

prompt = load_prompt("./simple_prompt_1.json")
print(prompt.format(adjective="funny", content="chickens"))