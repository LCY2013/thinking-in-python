# 导入所需的类和枚举
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language

# 定义一个包含Python代码的字符串
PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""

# 使用from_language方法创建一个针对Python语言的RecursiveCharacterTextSplitter实例
python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50, chunk_overlap=0
)

# 使用create_documents方法创建文档并将其存储在python_docs变量中
python_docs = python_splitter.create_documents([PYTHON_CODE])

