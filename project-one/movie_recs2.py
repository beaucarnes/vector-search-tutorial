import pymongo
import openai

# Set your OpenAI API key
openai.api_key = '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'

client = pymongo.MongoClient("mongodb+srv://beau:n9KkbZz60mfMPhWM@cluster0.svcxhgj.mongodb.net/?retryWrites=true&w=majority")
db = client.sample_mflix
collection = db.embedded_movies

def generate_embedding(text: str) -> list[float]:

    response = openai.Embedding.create(
        model="text-embedding-ada-002", 
        input=text
    )
    return response['data'][0]['embedding']

query = "imaginary characters from outer space at war"

results = collection.aggregate([
  {"$vectorSearch": {
    "queryVector": generate_embedding(query),
    "path": "plot_embedding",
    "numCandidates": 100,
    "limit": 4,
    "index": "PlotSemanticSearch",
      }}
]);

for document in results:
    print(f'Movie Name: {document["title"]},\nMovie Plot: {document["plot"]}\n')