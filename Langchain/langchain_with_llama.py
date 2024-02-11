from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

llm = Ollama(model="llama2")
"""
Calling the llm model directly
"""
# result = llm.invoke('how can langsmith help in building chatbot')
# Langsmith is a tool that helps you generate and optimize natural language content, including chatbots. Here are some
# ways Langsmith can help in building a c
prompt = ChatPromptTemplate.from_messages([("system", "you are a hindi translator, that understand the question"
                                                      "if asked in english but answers in hindi"),
                                           ("user", "{input}")])

# forming chain with a message template and the llm modeln
chain = prompt | llm
result = chain.invoke({'input': 'How to plan a holiday in Kolkatta'})
print(result)
