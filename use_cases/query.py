import pprint
from time import time

from driver.connection import DriverConnection
from driver.nested_object_driver import MongoNestedObjectDriver
from generator.random_obj import RandomObjGenerator


class QueryUseCase:

    def do(self):
        connection = DriverConnection()
        driver = MongoNestedObjectDriver(connection)

        s_time = time()
        res = driver.query_by_fixed_and_number_prop()
        count = driver.count_documents_in_collection_by_label()
        for item in res:
            pprint.pprint(item)


        print(f'found {res.count()} out of {count} nested obj by tag in: {time() - s_time}')
