hugging_face_token = "your token"
from langchain_community.llms import HuggingFaceHub
from langchain_community.chat_models.huggingface import ChatHuggingFace
from langchain.schema import (HumanMessage, SystemMessage)


"""
Model initialization using hugging face hub
"""
llm = HuggingFaceHub(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=hugging_face_token,
    model_kwargs={
        "max_new_tokens": 512,
        "top_k": 30,
        "temperature": 0.1,
        "repetition_penalty": 1.03,
    },
)

"""
Create a sample chat message
"""
message = [SystemMessage(content="You are friendly chat assistant with financial knowledge"),
           HumanMessage(content="Hey can you suggest some stock investment tips")]

"""
Initialize the chat model and invoke
"""
HF_TOKEN = hugging_face_token
chat_model = ChatHuggingFace(llm=llm)
response = chat_model.invoke(message)
print(response.content)
