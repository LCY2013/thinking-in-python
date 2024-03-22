# 导入DirectoryLoader类
from langchain.document_loaders import DirectoryLoader

# 创建DirectoryLoader实例，指定要加载的文件夹路径、要加载的文件类型和是否使用多线程
loader = DirectoryLoader('./LLM/documentstore', glob='**/*.md', use_multithreading=True)

# 使用load方法加载所有文档并将其存储在docs变量中
docs = loader.load()

# 打印加载的文档数量
print(len(docs))

# 导入UnstructuredHTMLLoader类
from langchain.document_loaders import UnstructuredHTMLLoader

# 创建UnstructuredHTMLLoader实例，指定要加载的HTML文件路径
loader = UnstructuredHTMLLoader("./index.html")

# 使用load方法加载HTML文件内容并将其存储在data变量中
data = loader.load()

# 导入BSHTMLLoader类
from langchain.document_loaders import BSHTMLLoader

# 创建BSHTMLLoader实例，指定要加载的HTML文件路径
loader = BSHTMLLoader("./index.html")

# 使用load方法加载HTML文件内容并将其存储在data变量中
data = loader.load()
