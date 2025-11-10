from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df= pd.read_csv("data.csv")
embeddings=OllamaEmbeddings(model="nomic-embed-text")

db_location="./chroma_langchain_db"
add_documents=not os.path.exists(db_location)

if add_documents:
    documents=[]
    ids=[]

    for i,row in df.iterrows():
        document=Document(
            page_content=row["Title"]+ " " + row["Description"],
            metadata={"source":row["Source"]},
            id=str(i)
        )
        documents.append(document)
        ids.append(str(i))

vector_store=Chroma(
    collection_name="AI_Trends_RAG",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents,ids=ids)

retriever=vector_store.as_retriever(
    search_kwargs={"k":4}
)