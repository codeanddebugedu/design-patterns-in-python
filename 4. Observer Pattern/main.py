from weather_station import WeatherStation
from tv import TVDisplay
from mobile import MobileDisplay

ws = WeatherStation()
tv = TVDisplay()

ws.add_observer(tv)
ws.update_temprature(30)

mobile = MobileDisplay()
ws.add_observer(mobile)
ws.update_temprature(35)

ws.remove_observer(tv)
ws.update_temprature(40)
