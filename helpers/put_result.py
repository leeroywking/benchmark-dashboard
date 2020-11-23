import pymongo
from helpers.env import dbpass

def put_result(result):
    client = pymongo.MongoClient(
        f"mongodb+srv://dbuser:{db_pass()}@cluster0.rpgzo.mongodb.net/benchmark_data?retryWrites=true&w=majority"
    )
    db = client["benchmark_data"]
    col = db["results"]
    response = col.insert_one(result)
    print(col)
    print(response)


if __name__ == "__main__":
    put_result({"hello": "world"})
