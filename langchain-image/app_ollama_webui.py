from flask import Flask, request, jsonify
import json
import os
from langchain.llms import Ollama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Create a prompt template
template = """
You are a helpful assistant. Please answer the following question:

{question}
"""


app = Flask(__name__)

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        # Get the prompt from the Open WebUI request
        data = request.get_json()
        question = data.get('prompt', '')
        print(question)
        model = data.get('model', 'llama3:8b-instruct-q8_0') # Default model
        print(model)

        olama_llm = Ollama(model=model, base_url="http://10.1.1.9:11434")
        prompt = PromptTemplate(template=template,input_variables=["question"])
        llm_chain = LLMChain(llm=olama_llm, prompt=prompt)
        print("------------------------------------------------------")

        answer = llm_chain.invoke(question)
        print(answer)
        return jsonify({"a": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

