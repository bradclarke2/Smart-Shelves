# a list of class objects to mimic a C type array of structures
# tested with Python24       vegaseat       30sep2005
class Person(object):
    """__init__() functions as the class constructor"""
    def __init__(self, name=None, trig_pin = None, echo_pin = None, distance=None):
        self.name = name
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.distance = distance
        

# make a list of class Person(s)
personList = []
personList.append(Person("Sensor1",53, 52, 0.00))
personList.append(Person("Sensor2",51, 50,0.00))
personList.append(Person("Sensor3",49, 48, 0.00))

sum = float(100) 
for person in personList:
    sum = sum + person.trig_pin
    print(type(person.distance))
    print(sum)