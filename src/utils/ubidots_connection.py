import urequests as requests
import utils.keys as keys

#UBIDOTS 


DEVICE_LABEL = "YOUR_DEVICE_LABEL" # Ubidots device label
TEMPERATURE_VARIABLE_LABEL = "YOUR_TEMP_VARIABLE"  # Ubidots variable label
HUMIDITY_VARIABLE_LABEL = "YOUR_HUM_VARIABLE"  # Ubidots variable label

# Sending data to Ubidots Restful Webserice
def sendData(device, data):
    try:
        url = "https://industrial.api.ubidots.com/"
        url = url + "api/v1.6/devices/" + device
        headers = {"X-Auth-Token": keys.TOKEN, "Content-Type": "application/json"}

        if data is not None:
            print(data)
            req = requests.post(url=url, headers=headers, json=data)
            return req.json()
        else:
            print("No data to send")
            return None
    except Exception as e:
        print("Error sending data: ", e)
        return None


# Builds the json to send the request
def build_json(temp_var, temp_value, hum_var, hum_value):
    try:
        data = {
            temp_var: {"value": temp_value},
            hum_var: {"value": hum_value}
        }        
        return data
    except:
        return None

