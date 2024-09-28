# RyanRag

## Introduction
This is a simple RAG system which you can use to upload a PDF file and ask questions about it.

## Ollama
Runs Ollama on a separate container and pulls the LLM
```bash
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
docker exec -it ollama ollama run llama3.2:1b
```

## Main App
Installs the required libraries and runs the streamlit app
```bash
docker build -t ryan_rag .
docker run -p 8501:8501 ryan_rag
```
Then, you'll see your app running on http://localhost:8501
