from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

# 这是一个聊天提示词模板，它将输入变量作为输入，并将其格式化为包含示例的提示词。
examples = [{"input": "2+2", "output": "4"}, {"input": "2+3", "output": "5"},]

# 提示词模板，用于格式化每个单独的示例。
example_prompt = ChatPromptTemplate.from_messages(
    [("human", "{input}"),
     ("ai", "{output}"),])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples)

print(few_shot_prompt.format())