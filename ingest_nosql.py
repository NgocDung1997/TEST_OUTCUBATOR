import requests
from pymongo import MongoClient
import configparser

api_url = "https://api.covidtracking.com/v2/us/daily.json"

config = configparser.ConfigParser()
config.read('D:\\test\\TEST_OUTCUBATOR\\db_connector.properties')
NOSQL_HOST = config.get('NOSQL', 'NOSQL_HOST')
NOSQL_PORT = config.get('NOSQL', 'NOSQL_PORT')

# Kết nối đến MongoDB
client = MongoClient(f"mongodb://{NOSQL_HOST}:{NOSQL_PORT}/")
db = client["test_outcubator"]
collection = db["test"]

# Lấy dữ liệu từ API
response = requests.get(api_url)
data = response.json()
print(data)
collection.insert_many(data["data"])

client.close()

print("Data save to MongoDB")
