# Local RAG Chatbot
A privacy-focused local RAG chatbot powered by Ollama LLM and ChromaDB vector storage. Chat with your documents offline without sending data to external APIs.

## Key Features

- **Complete Privacy**: All processing happens locally - no data leaves your system 
- **Offline Capability**: Works without internet connectivity once models are downloaded 
- **Customizable LLM**: Leverages Ollama for flexible model selection and local inference
- **Efficient Vector Search**: Uses ChromaDB for fast semantic similarity search and document retrieval 
- **Document Ingestion**: Process and embed CSV files
- **Context-Aware Responses**: Retrieves relevant document chunks to provide accurate, grounded answers 

## Tech Stack

- **Ollama**: Local LLM inference engine for text generation and embeddings 
- **ChromaDB**: Vector database for storing and retrieving document embeddings 
- **LangChain**: Framework for orchestrating the RAG pipeline
- **Python**: Core programming language

## Architecture

The chatbot implements a standard RAG pipeline 
1. **Document Processing**: Ingests and chunks documents into manageable segments
2. **Embedding Generation**: Converts text chunks into vector embeddings using Ollama
3. **Vector Storage**: Stores embeddings in ChromaDB for efficient retrieval
4. **Query Processing**: Embeds user queries and retrieves relevant context
5. **Response Generation**: Augments prompts with retrieved context and generates responses

## Getting Started

### Prerequisites
- Python 3.8+
- Ollama installed locally
- 8GB+ RAM recommended

