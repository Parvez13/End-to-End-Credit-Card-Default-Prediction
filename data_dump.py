import pymongo
import pandas as pd
import json
from creditcard.configuration.config import mongo_client
from creditcard.constant.training_pipeline import *

if __name__ == '__main__':
    df = pd.read_csv(DATA_FILE_PATH)
    df.reset_index(drop=True, inplace=True)
    json_records = list(json.loads(df.T.to_json()).values())
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)
    print("Insertion into Database done.")