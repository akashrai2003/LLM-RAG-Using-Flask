# Import necessary modules
from flask import Flask, request, jsonify, render_template
import os
from langchain import PromptTemplate, LLMChain
from langchain.llms.ctransformers import CTransformers
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.document_loaders import PyPDFLoader

# Initialize Flask app
app = Flask(__name__)

# Initialize LLM and other components as in the original code
local_llm = "TheBloke/Mistral-7B-Instruct-v0.1-GGUF"
config = {
    'max_new_tokens': 2048,
    'repeat_penalty': 1.1,
    'temperature': 0.4,
    'top_k': 50,
    'top_p': 0.9,
    'stream': True,
    'threads': int(os.cpu_count() / 2)
}

llm = CTransformers(
    model=local_llm,
    model_type="mistral",
    lib="avx2",
    **config
)

print("LLM Initialized....")

prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

model_name = "BAAI/bge-large-en"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceBgeEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

load_vector_store = Chroma(persist_directory="stores/pet_cosine", embedding_function=embeddings)

retriever = load_vector_store.as_retriever(search_kwargs={"k": 1})

# Define the routes
@app.route('/')
def indexx():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    query = request.form.get('query')

    # Your logic to handle the query
    chain_type_kwargs = {"prompt": prompt}
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs,
        verbose=True
    )

    if query is None:
        # Handle the case when query is None
        return jsonify({"answer": "Invalid query", "source_document": "", "doc": ""})

    response = qa(query)

    if response['source_documents']:
        source_document = response['source_documents'][0].page_content
        doc = response['source_documents'][0].metadata['source']
    else:
        source_document = "No source document found."
        doc = "Unknown"

    answer = response['result']
    response_data = {"answer": answer, "source_document": source_document, "doc": doc}

    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
