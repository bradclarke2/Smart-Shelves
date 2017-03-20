class Sensor (object):
    sensorType = ""
    distance = 0
    gridNumber = 0
    
    
    

    def __init__(self, sensorType, distance, gridNumber):
        self.sensorType = sensorType
        self.distance = distance
        self.gridNumber = gridNumber

def makeSensor(sensorType, distance, gridNumber): 
    sensor = Sensor(sensorType, distance, gridNumber)
    return sensor