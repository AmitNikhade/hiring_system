



################################ compress text ############################


from langchain.chains.summarize import load_summarize_chain
from langchain import OpenAI
from langchain.document_loaders import UnstructuredFileLoader


# llm = OpenAI(openai_api_key="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")

# loader = UnstructuredFileLoader('try/resume_parsed.txt')
# document = loader.load()

# from langchain.text_splitter import RecursiveCharacterTextSplitter
# char_text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0) 
# docs = char_text_splitter.split_documents(document)



# model = load_summarize_chain(llm=llm, chain_type="refine")
# print(model.run(docs))




##################################### Prompting ####################


import os


from langchain.schema import (
    HumanMessage,
    SystemMessage,
)
from langchain_openai import ChatOpenAI
import os
os.environ['OPENAI_API_KEY'] = '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'

# token = os.environ["CONTEXT_API_TOKEN"]

chat = ChatOpenAI(
   
)

messages = [
    SystemMessage(
        content="You are a friendly bot."
    ),
    HumanMessage(content="Tell me about yourself?"),
]

print(chat(messages))



################################## document loader ########################


# from langchain.document_loaders.pdf import PyPDFLoader

# loader = PyPDFLoader("resumes/Shreyas Kale CV.pdf")
# print(loader.load())


########################## 