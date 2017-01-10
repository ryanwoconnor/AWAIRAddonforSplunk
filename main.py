import requests

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiNjkxNiJ9.Iijdoo8oORm7r3VOvFhaWYHhbDilS9GoZ05gtsLjtxQ"

headers = {
    "Authorization": "Bearer %s" % token,
}

info = requests.get('https://beta-api.awair.is/v1/users/self/devices', headers=headers, stream=True)
response = requests.get('https://beta-api.awair.is/v1/devices/10823/events/15min-avg', headers=headers, stream=True)

events = response.json()
device = info.json()

def getDeviceinfo(access_tokern):
    for info in device["data"]:
        lines = str(info)
        print("Device ID: " + str(info["device_id"]))
        print("Location: " + str(info["location_name"]))
        print("Device Name: " + str(info["device_name"]))
        print("Longitude: " + str(info["longitude"]))
        print("Latitude: " + str(info["latitude"]))
        print("Room Type: " + str(info["room_type"]))
        print("Owner Type: " + str(info["owner_type"]))
        print("\n")

def get15minData(access_token):
    for data in events["data"]:
        lines = str(data)
        sensor = (data["sensor"])
        timestamp = (data["timestamp"])
        score = (data["score"])
        print("Timestamp: " + str(timestamp))
        print("Score: " + str(score))
        print("Sensor Data")
        print("CO2: " + str(sensor["co2"]) + " | " + "Dust: " + str(sensor["dust"]) + " | " + "Temperature: " + str(sensor["temp"]) + " | "  + "Humid: "  + str(sensor["humid"]) + " | " + "VOC: " + str(sensor["voc"]))
        index = (data["index"])
        print("Index Data")
        print("CO2: " + str(index["co2"]) + " | " + "Dust: " + str(index["dust"]) + " | " + "Temperature: " + str(index["temp"]) + " | " + "Humid: " + str(index["humid"]) + " | " + "VOC: " + str(index["voc"]) + "\n")

#getDeviceinfo(token)
get15minData(token)