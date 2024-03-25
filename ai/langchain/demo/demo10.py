from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate

examples = [
    {"question": "Who lived longer, Muhammad Ali or Alan Turing?",
    "answer":
    """
    Are follow up questions needed here: Yes.
    Follow up: How old was Muhammad Ali when he died?
    Intermediate answer: Muhammad Ali was 74 years old when he died.
    Follow up: How old was Alan Turing when he died?
    Intermediate answer: Alan Turing was 41 years old when he died.
    So the final answer is: Muhammad Ali
    """},
    {"question": "When was the founder of craigslist born?",
    "answer":
    """
    Are follow up questions needed here: Yes.
    Follow up: Who was the founder of craigslist?
    Intermediate answer: Craigslist was founded by Craig Newmark.
    Follow up: When was Craig Newmark born?
    Intermediate answer: Craig Newmark was born on December 6, 1952.
    So the final answer is: December 6, 1952
    """},
    {"question": "Who was the maternal grandfather of George Washington?",
    "answer":
    """
    Are follow up questions needed here: Yes.
    Follow up: Who was the mother of George Washington?
    Intermediate answer: The mother of George Washington was Mary Ball Washington.
    Follow up: Who was the father of Mary Ball Washington?
    Intermediate answer: The father of Mary Ball Washington was Joseph Ball.
    So the final answer is: Joseph Ball
    """},
    {"question": "Are both the directors of Jaws and Casino Royale from the same country?",
    "answer":
    """
    Are follow up questions needed here: Yes.
    Follow up: Who is the director of Jaws?
    Intermediate Answer: The director of Jaws is Steven Spielberg.
    Follow up: Where is Steven Spielberg from?
    Intermediate Answer: The United States.
    Follow up: Who is the director of Casino Royale?
    Intermediate Answer: The director of Casino Royale is Martin Campbell.
    Follow up: Where is Martin Campbell from?
    Intermediate Answer: New Zealand.
    So the final answer is: No
    """}
]

# 配置一个格式化程序，该格式化程序将prompt格式化为字符串。此格式化程序应该是一个 PromptTemplate 对象。
example_prompt = PromptTemplate(input_variables=["question", "answer"], template="Question: {question}\n{answer}")
print(example_prompt.format(**examples[0]))

# 创建一个选择器来选择最相似的例子
example_selector = SemanticSimilarityExampleSelector(
    examples=examples,
    vector_store=Chroma(),
    embeddings_model=OpenAIEmbeddings(),
    example_prompt=example_prompt
)

# 最后用FewShotPromptTemplate 来创建一个提示词模板，该模板将输入变量作为输入，并将其格式化为包含示例的提示词。
prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"]
)
print(prompt)