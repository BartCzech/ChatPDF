# pip install streamlit pypdf2 langchain python-dotenv faiss-cpu openai huggingface_hub
import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader:
            text += page.extract_text()
    return text 
    
def main():
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    openai_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    print(openai_api_key)
    # UI section
    st.set_page_config(page_title="Chat with multiple PDFs", page_icon=":books:")
    
    st.header("Chat with multiple PDFs")    
    st.text_input("Ask a question about the documents:")
    
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on Process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf
                raw_text = get_pdf_text(pdf_docs) 
                # get text chunks
                # create vector store (probably gonna need separate for both TAM and clientreqs)

if __name__ == '__main__':
    main()