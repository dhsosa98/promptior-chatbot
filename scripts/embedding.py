from langchain_openai import OpenAIEmbeddings
import os 

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


# A function to create an instance of OpenAIEmbeddings
def create_embedding():
    embedding = OpenAIEmbeddings(
        openai_api_key=OPENAI_API_KEY,
    )
    return embedding
