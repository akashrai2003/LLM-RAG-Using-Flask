The repository shows the example of performing Retrieval Augmented Generation on a Mistral-7B model. As there are many ways to perform RAG like using HuggingFace library, but here I've used the Langchain Toolkit in order to perform RAG on 2 documents i.e. `awsgsg-intro.pdf` and another pdf based on satellites. 

<h3>Hugging Face Transformers:</h3>
Pros:
- Large community support and a wide range of pre-trained language models.
- Easy-to-use interfaces for working with state-of-the-art models.
- Provides a RAG model that combines retrieval and generation (RagTokenizer, RagRetriever, etc.).
Cons:
- Limited customization compared to building your own pipeline.

<h3>Haystack:</h3>
Pros:
- Designed specifically for Question Answering (QA) systems with retrievers.
- Supports various retrieval models, including Elasticsearch, FAISS, and more.
- Can be integrated with different language models for generation.
Cons:
- Specific focus on QA systems, may require adaptation for broader applications.
- Learning curve for setting up and configuring the components.

<h3> Langchain: </h3>
Pros:
- Specialized in combining language models and retrieval systems.
- Provides tools for building custom retrieval and generation pipelines.
- Allows fine-grained control over the components used in the system.
Cons:
- Smaller community compared to Hugging Face.
- May require more manual setup and configuration.


So to make things and parameters more customized while fine tuning and easy retrieval of information coming from the PDFs I have picked Langchain.
Another step closer to RAG but not exactly RAG can be using a vectorDB made using FAISS and then performing semantic search to find closest searches and passing it to an text generation model in order to describe more about the similar found texts. I had made one which can be accessed here [Semantic-Search-Engine-With-Summarizer](https://github.com/college-akashrai/SemanticSearchForPatents)

This code can be reproduced by cloning the directory and thus deleting the `stores` directory as it contains the embeddings created and also removing any documents in the `Docs` directory and you can insert your own documnets here. The `research` directory contains the code tests and how I'd first used Jupyter notebook to generate results in a different way and then transforming it to a python script. The templates dir has the `index.html` files where I'd tried different UI but as I'm not too good/experienced at it so I tried to stick with a basic template. Flask is used for backend integration of the HTML file and is available in `app.py`. 
But in order to create the vector store first we have to run the `ingest.py` file while placing the documents in the correct directory.
Finally, downloading any LLM model (P.S. here I've used Mistral7B) from HuggingFace onto your local machine and provide the path or you can just give the complete info of the model from HuggingFace like: `TheBloke/Mistral-7B-Instruct-v0.1-GGUF`
And thus it will download the model temporarily in cache and can be used repeatedly if loaded once. So running the python script using:
`python3 app.py` would spin off the flask server and the model will be loaded and thus using the chat UI we can give queries based on the docs and accurate responses with the sourcing of the info too. The chat interface wasn't developed too well due to some time constraints and my lack of in-depth frontend knowledge. But I beleive learning frontend won't be a major part here as I was easily able to create endpoints and perform the app to run without major issues. 

