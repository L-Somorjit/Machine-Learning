from langchain_core.messages import AIMessage, HumanMessage
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import faiss
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.document_loaders import PyPDFLoader

# initialize chat model
llm = ChatOpenAI(openai_api_key="your key")

# load document
loader = PyPDFLoader("attention_is_all_you_need.pdf")
doc = loader.load()

# create retriever with embedding
embeddings = OpenAIEmbeddings(openai_api_key="your key")

text_splitter = RecursiveCharacterTextSplitter()
document = text_splitter.split_documents(doc)

vector_index = faiss.FAISS.from_documents(document, embeddings)
retriever = vector_index.as_retriever()


# build the chat

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

# chat_history = [HumanMessage(content="Hi"), AIMessage(content="Hi, how can I help you?")]
# result = retrival_chain.invoke({'chat_history': chat_history,
#                                 'input': 'what is my name?'})
# print(result['answer'])
chat_history = []
while True:
    user_text = input("User:")
    if user_text == 'quit':
        break
    response = retrival_chain.invoke({'chat_history': chat_history,
                                      'input': str(user_text)})
    print(f"Bot: {response['answer']}")
    chat_history.extend([HumanMessage(content=str(user_text)), AIMessage(content=str(response['answer']))])
