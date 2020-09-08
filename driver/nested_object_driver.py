import json
from typing import List

from driver.connection import DriverConnection


class MongoNestedObjectDriver:
    connection:DriverConnection

    def __init__(self,conn:DriverConnection):
        self.connection = conn

    def add_one(self,obj_dict:dict):
        self.connection.db_collection.insert_one(obj_dict)

    def bulk_add(self,objects:List[dict]):
        self.connection.db_collection.insert_many(objects)

    def clear_collection(self):
        self.connection.db_collection.delete_many({})

    def query_by_tag(self):
        return self.connection.db_collection.find( { 'Tags.tag_name_8': "girl drives merrily. odd" } )

    def query_by_fixed_label_and_tag(self):
        return self.connection.db_collection.find( {
            'fixed_label_0':'label_value_6 and label_value_9 and label_value_1',
            'fixed_label_1': 'label_value_3 and label_value_3 and label_value_1',
            'Tags.tag_name_8': "girl drives merrily. odd" } )

    def query_by_fixed_and_number_prop(self):
        return self.connection.db_collection.find( {
            'fixed_label_0':'label_value_6 and label_value_9 and label_value_1',
            'number_prop': { "$gte": 20 }} )

    def count_documents_in_collection_by_label(self):
        return self.connection.db_collection.count_documents({'fixed_label_0':'label_value_6 and label_value_9 and label_value_1'})
