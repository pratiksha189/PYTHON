from calendar import error


class TemperatureError(Exception):
    pass

class TemperatureSensor:
    def __init__(self,temperature):
        self._temperature= temperature



    def check_temperature(self):
       if  self._temperature >50:
           raise TemperatureError("Temperature too high")
       else:
           print(f'current temperature{self._temperature}')

sensor=TemperatureSensor()
try:
    sensor.check_temperature(55)
except TemperatureError as e:
    print(f"warning : {e}")