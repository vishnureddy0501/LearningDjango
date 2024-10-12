import pymongo

url = "mongodb+srv://gujjulavishnuvardhanreddy8179:Vishnu123@cluster0.2nbwswo.mongodb.net/user_management"
client = pymongo.MongoClient(url)
# db = client('user_management')
db = client.user_management
