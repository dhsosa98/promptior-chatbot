from langchain_core.prompts import ChatPromptTemplate



# This is a function to create a prompt template.
# The prompt template is used to generate prompts for the language model.
# This its a basic version of the prompt template.
def create_prompt_template():
    return ChatPromptTemplate.from_template("""
    Answer the following question based only on the provided context:
    <context>
    {context}
    </context>

    Question: {input}""")

