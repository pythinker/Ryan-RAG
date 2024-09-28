# RyanRag

## Introduction
This is a fully dockerized RAG system using Ollama and Streamlit which you can use to upload a PDF file and ask questions about it.

## Ollama
Create a network for the containers to communicate with each other
```bash
docker network create ollama-network
```
Run Ollama on a separate container
```bash
docker run -d --name ollama --network ollama-network -p 11434:11434 ollama/ollama
```
Pull the LLM and the embedding model
```bash
docker exec -it -d ollama ollama run llama3.2:1b
docker exec -it -d ollama ollama run nomic-embed-text
```


## RAG App
Installs the required libraries and runs the streamlit app
```bash
docker build -t ryan_rag .
docker run -d --name ryan_rag -p 8501:8501 --network ollama-network ryan_rag
```
Then, you'll see your app running on http://localhost:8501
