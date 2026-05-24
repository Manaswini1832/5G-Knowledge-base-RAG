# install python packages
# !pip install -q llama-index
# !pip install -q llama-index-readers-web
# !pip install -q openai

import os
# from google.colab import userdata

# OPENAI_API_KEY_DEV = userdata.get('OPENAI_API_KEY_DEV')
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY_DEV # put api key here

from llama_index.core import SummaryIndex
from llama_index.readers.web import SimpleWebPageReader
from IPython.display import Markdown, display

# global variable
index = None

# get knowledge
def getKnowledge() :
  global index

  inputUrl = input("Enter url : ")

  documents = SimpleWebPageReader(html_to_text=True).load_data(
      [inputUrl]
  )

  index = SummaryIndex.from_documents(documents)

  print("Knowledge loaded successfully!")

# ask query
def askQuery() :
  global index

  if index is None:
        print("Please load knowledge first.")
        return

  query_engine = index.as_query_engine()
  query = input("\nAsk your question (type DONE to exit): ")

  print(f"\nFetching results for query : {query}")
  response = query_engine.query(query)

  display(Markdown(f"## Response\n\n{response}"))

# ask for user input
print("What do you want to do?")
print("Press 1 to input knowledge")
print("Press 2 to ask a query")
todo = input("Your input : ")

if todo == "1" :
  getKnowledge()

elif todo == "2" :
  askQuery()

else :
  print("Unsupported input")