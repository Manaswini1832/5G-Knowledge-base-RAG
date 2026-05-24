## v1
- Takes in a user input URL and LlamaIndex chunks it and stores them in an in-memory SummaryIndex variable
- User query is sent to the OpenAI LLM configured inside LlamaIndex
  - Uses the chunks from SummaryIndex to respond to query
- Display response mardown in colab notebook
