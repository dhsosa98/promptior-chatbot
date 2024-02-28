from langchain_community.vectorstores import faiss
from typing import List


# This is a function that creates a vector store from a list of strings.
# It uses the faiss library to create the vector store.
# The vector store is used to store the embeddings of the strings.
def create_vector_store(data: List[str], embedding):
    vector = faiss.FAISS.from_texts(texts=data, embedding=embedding)
    return vector