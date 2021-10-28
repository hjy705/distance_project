from pyproj import Geod
import json


containerFloodSensorStation = {}
containerSewerStation = {}


with open('rain_station.json',encoding="utf-8") as f:
    a = json.load(f)
with open('flooding_sensor_layer.json', mode='r', encoding="utf-8") as f:
    b = json.load(f)
with open('sewer_layer.json', mode='r', encoding="utf-8") as f:
    c = json.load(f)


for key in b["features"]:
    thisFloodSensorStationId = key["properties"]["id"]
    containerFloodSensorStation[thisFloodSensorStationId]={"rain_station_distance": {},"sewer_station_distance": {}}
    for value in a:
        lats = [key["geometry"]["coordinates"][1],value["LAT"]]
        lons = [key["geometry"]["coordinates"][0],value["LON"]]
        geod = Geod(ellps="WGS84")
        total_length = geod.line_length(lons, lats)
        thisRainStationId = value["STID"]
        containerFloodSensorStation[thisFloodSensorStationId]["rain_station_distance"][thisRainStationId] = total_length
    for value in c["features"]:
        lats = [key["geometry"]["coordinates"][1],value["geometry"]["coordinates"][1]]
        lons = [key["geometry"]["coordinates"][0],value["geometry"]["coordinates"][0]]
        geod = Geod(ellps="WGS84")
        thisSewerStationIdvalue = str(value["properties"]["id"])
        total_length = geod.line_length(lons, lats)
        containerFloodSensorStation[thisFloodSensorStationId]["sewer_station_distance"][thisSewerStationIdvalue] = total_length


for key in c["features"]:
    thisSewerStationId = str(key["properties"]["id"])
    containerSewerStation[thisSewerStationId]={"rain_station_distance": {},"flooding_sensor_distance": {}}
    for value in a:
        lats = [key["geometry"]["coordinates"][1],value["LAT"]]
        lons = [key["geometry"]["coordinates"][0],value["LON"]]
        geod = Geod(ellps="WGS84")
        total_length = geod.line_length(lons, lats)
        thisRainStationId = value["STID"]
        containerSewerStation[thisSewerStationId]["rain_station_distance"][thisRainStationId] = total_length
    for value in b["features"]:
        lats = [key["geometry"]["coordinates"][1],value["geometry"]["coordinates"][1]]
        lons = [key["geometry"]["coordinates"][0],value["geometry"]["coordinates"][0]]
        geod = Geod(ellps="WGS84")
        thisFloodSensorIdvalue = str(value["properties"]["id"])
        total_length = geod.line_length(lons, lats)
        containerSewerStation[thisSewerStationId]["flooding_sensor_distance"][thisFloodSensorIdvalue] = total_length


print(containerFloodSensorStation)
print(containerSewerStation)

result = {
    "floodsensor": containerFloodSensorStation,
    "sewersensor": containerSewerStation
}

with open('distance.json', 'w', encoding='utf-8') as outfile:
    json.dump(result , outfile, ensure_ascii=False, indent=4)
