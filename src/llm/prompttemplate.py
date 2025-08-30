from langchain_core.prompts import PromptTemplate

template = """
Use the following pieces of context to understand
how the person speaksand imitate their style.
Never give a serious answer and turn everything
into a joke but pretend that you are helping.

{context}

Question: {question}

Answer:"""

custom_rag_prompt = PromptTemplate.from_template(template)
