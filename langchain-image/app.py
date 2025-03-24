import os
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

olama_llm = Ollama(model="llama3:8b-instruct-q8_0", base_url="http://10.1.1.9:11434")  # Replace "llama2" with the model you want to use

# Create a prompt template
template = """
You are a helpful assistant. Please answer the following question:

{question}
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["question"]
)

# Create an LLMChain
llm_chain = LLMChain(llm=olama_llm, prompt=prompt)

# Run the chain
question = "What is the capital of Taiwan?"
answer = llm_chain.run(question)

print(answer)

