

from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


# This is the second intent. I will use the data from the promptior.txt file.
def data_source_text():
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'promptior.txt')
    with open(data_path, 'r', encoding='utf-8') as file:
        data = file.read()
        return data
    

# This was the first intent. But the promptior page doesnt let me scrape it.
def data_source_scapping(urls):

    loader = WebBaseLoader(urls)

    docs = loader.load()

    text_splitter = RecursiveCharacterTextSplitter()

    documents = text_splitter.split_documents(docs)

    return documents