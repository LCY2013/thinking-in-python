text = """客户：您好，我想咨询一下信用卡的问题。\n客服：您好，欢迎咨询建行信用卡，我是客服小李，请问有什么问题我可以帮您解答吗？\n客户：我想了解一下信用卡的年费如何收取？\n客服：关于信用卡年费的收取，我们会在每年的固定日期为您的信用卡收取年费。当然，如果您在一年内的消费达到一定金额，年费会自动免除。具体的免年费标准，请您查看信用卡合同条款或登录我们的网站查询。\n客户：好的，谢谢。那我还想问一下，如何提高信用卡的额度？\n客服：关于提高信用卡额度，您可以通过以下途径操作：1. 登录建行信用卡官方网站或手机APP，提交在线提额申请；2. 拨打我们的客服热线，按语音提示进行提额申请；3. 您还可以前往附近的建行网点，提交提额申请。在您提交申请后，我们会根据您的信用状况进行审核，审核通过后，您的信用卡额度将会相应提高。\n客户：明白了，非常感谢您的解答。\n客服：您太客气了，很高兴能够帮到您。如果您还有其他问题，请随时联系我们。祝您生活愉快！"""
list_text = text.split('\n')

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

db = FAISS.from_texts(list_text, OpenAIEmbeddings())

query = "信用卡的额度可以提高吗"
docs = db.similarity_search(query)
print(docs[0].page_content)

embedding_vector = OpenAIEmbeddings().embed_query(query)
print(f'embedding_vector：{embedding_vector}')
docs = db.similarity_search_by_vector(embedding_vector)
print(docs[0].page_content)
