from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
class DriverConnection:
    server_connection_str:str
    collection_name:str
    db_client:MongoClient
    db_obj:Database
    db_collection:Collection
    def __init__(self):
        self.server_connection_str= 'localhost'
        self.collection_name ='nested_items'
        self.db_client = MongoClient(self.server_connection_str,27017)
        self.db_obj = self.db_client['performance_test_db']
        self.db_collection= self.db_obj[self.collection_name]
