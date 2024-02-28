from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from scripts.vector_store import create_vector_store
from scripts.data_source import data_source_text
from scripts.promp_template import create_prompt_template
from scripts.embedding import create_embedding
from scripts.llm import create_llm
from scripts.refine_data import refine_text_data
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles

load_dotenv()

# Initialize the app
app = FastAPI()

# Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def chat_with_bot(query="", model='gpt-3.5-turbo'):
    try:
        # Create the embedding
        embedding = create_embedding()

        # Get the data
        data = data_source_text()

        # Refine the data
        data = refine_text_data(data)

        # Create the vector store
        vector = create_vector_store(data=data, embedding=embedding)

        # Create the language model
        llm = create_llm(model)

        # Create the prompt template
        promptTemplate = create_prompt_template()

        # Create the document chain
        document_chain = create_stuff_documents_chain(llm=llm, prompt=promptTemplate)

        # Obtain the retriever
        retriever = vector.as_retriever()

        # Create the retrieval chain
        retrieval_chain = create_retrieval_chain(retriever, document_chain)

        # Ask the bot
        response = retrieval_chain.invoke({"input": query})

        answer = response['answer']

        return answer

    except Exception as e:
        return f"An error occurred: {e}"



# Define the chat endpoint
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    print(body)
    query = body.get('query')
    model = body.get('model')
    answer = chat_with_bot(query, model=model)
    return {"answer": answer}

# Serve the static files
app.mount("/", StaticFiles(directory="static", html = True), name="static")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)