from langchain_openai import ChatOpenAI
import os
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


# A function to create an instance of a language model
# I use the ChatOpenAI class to create the language model but it can be extended to use other language models.
def create_llm(model='gpt-3.5-turbo'):
    llm = ChatOpenAI(
        model=model,
        api_key=OPENAI_API_KEY,
    )
    return llm
    