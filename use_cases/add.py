from driver.connection import DriverConnection
from driver.nested_object_driver import MongoNestedObjectDriver


class AddUseCase:

    def do(self):

        connection = DriverConnection()
        driver = MongoNestedObjectDriver(connection)


        driver.add_one(obj_normal)
