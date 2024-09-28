import os

import PyPDF2
from llama_index.core import VectorStoreIndex, Document
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
import streamlit as st


# Initialize Ollama
ollama_embedding = OllamaEmbedding(model_name="nomic-embed-text")
ollama_llm = Ollama(model="llama3.2")


def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def save_uploaded_file(uploaded_file):
    with open(os.path.join("uploads", uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return os.path.join("uploads", uploaded_file.name)


# ... (previous imports and function definitions)

def main():
    st.title("PDF Chatbot")

    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        try:
            # Save the uploaded file
            file_path = save_uploaded_file(uploaded_file)

            # Extract text from PDF
            pdf_text = extract_text_from_pdf(file_path)

            # Create a Document object
            document = Document(text=pdf_text)

            # Create a VectorStoreIndex
            with st.spinner("Processing PDF..."):
                index = VectorStoreIndex.from_documents([document], embed_model=ollama_embedding)

            # Create a query engine
            query_engine = index.as_query_engine(llm=ollama_llm)

            # Chat interface
            st.subheader("Ask a question about the PDF:")
            user_question = st.text_input("Your question:")
            if user_question:
                with st.spinner("Generating answer..."):
                    response = query_engine.query(user_question)
                st.write("Answer:", response.response)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
