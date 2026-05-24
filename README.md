# v1
- Takes in a user input URL and LlamaIndex chunks it and stores them in an in-memory SummaryIndex variable
- User query is sent to the OpenAI LLM configured inside LlamaIndex
  - Uses the chunks from SummaryIndex to respond to query
- Display response mardown in colab notebook

# Todos
- [ ]  Use an embedding model to chunk input urls
- [ ]  put chunks in persistenct vector store not just in memory
- [ ]  Embed user query using same embedding model
- [ ]  Do cosine similarity search for topK chunks
- [ ]  Send chunks to LLM for a response
- [ ]  Replace default embedding model + LLM with models/llms from hugging face and self host(?)
