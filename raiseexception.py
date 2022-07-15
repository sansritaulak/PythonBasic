#user defined exception
class Accident(Exception):
    def __init__(self,msg):
        self.msg = msg
    def print_exception(self):
        print("User defined exception : ",self.msg)

try:
    raise Accident ('Accident between two cars')
    # raise MemoryError ('memory error')          #python buildin exception in google.
except Accident  as e:
    e.print_exception()

