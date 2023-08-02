from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource indentifier.
url = "mongodb+srv://datascience:datascience@cluster0.4vt0cq9.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(url)


# create database name and collection name
DATABASE_NAME="ML_project"
COLLECTION_NAME="waferfault"


# Read the data as a dataframe.
df=pd.read_csv(r"C:\TheBritishCollege\DataScience\sensor_project\notebook\wafer_23012020_041211.csv")
df=df.drop('Unnamed: 0', axis=1)

# convert the dataframe into json formate.
json_record=list(json.loads(df.T.to_json()).values())


# now dunp the data into database.
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

