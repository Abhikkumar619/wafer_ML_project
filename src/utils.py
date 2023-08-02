from pymongo import MongoClient
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from src.exception import CustomException
import os
import pandas as pd
import numpy as np
import sys
import dill


def export_collection_as_dataframe(collection_name, db_name):
    try:
        Mongo_client=MongoClient(os.getenv("MONGO_DB_URL"))
        
        collection=Mongo_client[db_name][collection_name]
        
        df=pd.DataFrame(list(collection.find()))
        
        if "_id" in df.columns.to_list():
            df=df.drop(columns=["_id"], axis=1)
        
        df.replace({"np":np.nan}, inplace=True)
        
        return df
    
    except Exception as e:
        raise CustomException(e, sys)
        
def save_object(file_path, obj):
    try:
        dir_path=os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)
    
def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    
    except Exception as e:
        raise CustomException(e, sys)