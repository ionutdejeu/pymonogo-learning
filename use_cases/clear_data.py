from driver.connection import DriverConnection
from driver.nested_object_driver import MongoNestedObjectDriver
from generator.random_obj import RandomObjGenerator


class ClearUseCase:

    def do(self):

        connection = DriverConnection()
        driver = MongoNestedObjectDriver(connection)
        driver.clear_collection()
