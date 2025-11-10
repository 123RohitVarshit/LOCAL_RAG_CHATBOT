from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

# Model Instance
model=OllamaLLM(model="llama3.2")

template="""
You are expert in answering questions about the content of the provided documents.You are also expert in handling PDF and CSV files and can
extract relevant and insightful information from them.You will be mostly handling PDF and CSV files regarding latest technology trends 
and advancements.

Here is the content of the document:{content}

Here is the query to answer based on the content:{query}
"""

prompt=ChatPromptTemplate.from_template(template)

chain=prompt | model

while True:
    print("\n\n----------------------------")
    user_query=input("Enter your query (or type 'q' to quit):")
    print("\n\n")
    if user_query.lower()=='q':
        break
    relevant_content=retriever.invoke(user_query)
    result=chain.invoke({"content":[],"query":user_query})
    print(result)