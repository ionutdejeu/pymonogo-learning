from time import time

from driver.connection import DriverConnection
from driver.nested_object_driver import MongoNestedObjectDriver
from generator.random_obj import RandomObjGenerator


class BulkAddUseCase:

    def do(self):

        connection = DriverConnection()
        driver = MongoNestedObjectDriver(connection)
        generator = RandomObjGenerator()

        #add 200 000 000 documents
        for i in range(0,1000):
            objects = generator.get_set_random_obj_with_id(200000)
            s_time = time()
            driver.bulk_add(objects)
            print(f'duration to insert 20000 items: {time()-s_time}')
