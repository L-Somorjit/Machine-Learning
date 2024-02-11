from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import faiss
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain_core.messages import AIMessage, HumanMessage

llm = ChatOpenAI(openai_api_key="Your key")
"""
1) Simple direct call
"""
# result = llm.invoke("how can langsmith help with testing?")
# print(result) content='Langsmith can help with testing in several ways:\n\n1. Automated Testing:

"""
2) Chain llm with input template to specify specific info
"""
# prompt = ChatPromptTemplate.from_messages([('system', 'Act as arogant grumpy father'),
#                                            ('user', '{input}')])
# chain = prompt | llm
# result = chain.invoke({"input": "How was your day?"})
# print(result) content="Don't ask me about my day, it's none of your business. I'm sure it was just as uneventful and
# insignificant as every other day

"""
3) add output structure to get proper string
"""
output_parser = StrOutputParser()
# chain = prompt | llm | output_parser
# result = chain.invoke({"input": "How was your day?"})
# print(result)  # Oh, the day was just splendid. Absolutely marvelous. I mean, who wouldn't want to spend their

"""
4) Use document to get specific information, which is not general
we will use web page, using beautifulsoup to get web page data
"""
loader = WebBaseLoader("https://techsophy.com/")
doc = loader.load()

"""
5) Use a data retriever to retrieve only a section and use it
here vectorstore is used (SQL, cloud, mongodb, etc.) to create vector store index embedding is needed
openai is used for embedding and faiss for vector store"""
embeddings = OpenAIEmbeddings(openai_api_key="Your key")

text_splitter = RecursiveCharacterTextSplitter()
document = text_splitter.split_documents(doc)

vector_index = faiss.FAISS.from_documents(document, embeddings)

"""
6) create prompt using template and combine with llm to create chain
"""
# prompt = ChatPromptTemplate.from_template("""
# You are a world renowned mathematics scholar. Using the context specified within the tag, you need to evaluate and
# understand the paper thoroughly, and answer the question that follows:
# <context>
# {context}
# </context>
#
# Question: {input}
# """)

# prompt = ChatPromptTemplate.from_template("""
# Based on the context provided inside the tag, answer the question the follows, if anything outside the context
# is asked response as "That is out of context you dumb head":
# <context>
# {context}
# </context>
#
# Question: {input}
# """)

# prompt_chain = create_stuff_documents_chain(llm, prompt)
retriever = vector_index.as_retriever()

# chain = create_retrieval_chain(retriever, prompt_chain)
#
#
# response = chain.invoke({'input': 'what is the company name, what are the solutions it provides'})
# print(response['answer'])

"""
7) Chatbot with chat history, need to change retriever with retriever chain for chat history and retrieving
relevant data from chat history, also need to change prompt to consider chat history
"""
retrieve_prompt = ChatPromptTemplate.from_messages([MessagesPlaceholder('chat_history'),
                                                    ("user", "{input}"),
                                                    ("user", "Using the given conversation generate search query"
                                                             "to look up and get relevant information about the"
                                                             "conversation.")])
retriever_chain = create_history_aware_retriever(llm, retriever, retrieve_prompt)
prompt = ChatPromptTemplate.from_messages([("system", "Answer question based on following context: {context}"),
                                           MessagesPlaceholder("chat_history"),
                                           ("user", "{input}")])

document_chain = create_stuff_documents_chain(llm, prompt)
retrival_chain = create_retrieval_chain(retriever_chain, document_chain)

chat_history = [HumanMessage(content="My name is somorjit"), AIMessage(content="Hello Somorjit, how can I help you")]
result = retrival_chain.invoke({'chat_history': chat_history,
                                'input': 'what is my name?'})
print(result['answer'])
