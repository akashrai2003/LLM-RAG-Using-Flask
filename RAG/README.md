The repository shows an example of performing Retrieval Augmented Generation (RAG) on a Mistral-7B model using the Langchain Toolkit. While there are various ways to implement RAG, such as using Hugging Face or Haystack, I chose Langchain for its customization options and fine-tuning capabilities.

### Hugging Face Transformers:
**Pros:**
- Large community support and a wide range of pre-trained language models.
- Easy-to-use interfaces for working with state-of-the-art models.
- Provides a RAG model that combines retrieval and generation (RagTokenizer, RagRetriever, etc.).

**Cons:**
- Limited customization compared to building your own pipeline.

### Haystack:
**Pros:**
- Designed specifically for Question Answering (QA) systems with retrievers.
- Supports various retrieval models, including Elasticsearch, FAISS, and more.
- Can be integrated with different language models for generation.

**Cons:**
- Specific focus on QA systems, may require adaptation for broader applications.
- Learning curve for setting up and configuring the components.

### Langchain:
**Pros:**
- Specialized in combining language models and retrieval systems.
- Provides tools for building custom retrieval and generation pipelines.
- Allows fine-grained control over the components used in the system.

**Cons:**
- Smaller community compared to Hugging Face.
- May require more manual setup and configuration.

To customize parameters and facilitate easy retrieval of information from PDFs, I opted for Langchain. Another approach, a step closer to RAG, involves creating a vectorDB using FAISS and performing semantic search to find the closest matches. This can then be passed to a text generation model to provide more information about the similar found texts. An example of this approach can be found in [Semantic-Search-Engine-With-Summarizer](https://github.com/college-akashrai/SemanticSearchForPatents).

To reproduce this code, clone the directory, delete the `stores` directory (contains embeddings), remove any documents in the `Docs` directory, and insert your own documents. The `research` directory contains code tests, while the `templates` directory has the `index.html` files for UI. Flask is used for backend integration (see `app.py`). To create the vector store, run `ingest.py` after placing documents in the correct directory.

Download any LLM model (here I used Mistral7B) from HuggingFace onto your local machine. Provide the path or complete info of the model from HuggingFace, like `TheBloke/Mistral-7B-Instruct-v0.1-GGUF`. Running `python3 app.py` will spin off the Flask server, load the model, and the chat UI can be used to provide queries based on the docs with accurate responses and sourcing information.

Note: The chat interface might need improvement in terms of UI, but the functionality is intact. Frontend knowledge can be acquired as needed.

