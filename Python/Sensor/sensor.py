class Sensor (object):
    sensorType = ""
    measurement = 0
    gridNumber = 0  

    def __init__(self, sensorType, measurement, gridNumber):
        self.sensorType = sensorType
        self.measurement = measurement
        self.gridNumber = gridNumber

def makeSensor(sensorType, measurement, gridNumber): 
    sensor = Sensor(sensorType, measurement, gridNumber)
    return sensor