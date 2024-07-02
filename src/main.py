import machine
import dht
from time import sleep
from machine import Pin

import utils.functions as fn
import utils.ubidots_connection as vis
import utils.wifi_connection as wifi


# Set up
sensor = dht.DHT11(machine.Pin(27))  # DHT11 Constructor, Temperature & Humidity Sensor 

on_board_led = Pin("LED", Pin.OUT)

green_led = Pin(22, Pin.OUT)
red_led = Pin(21, Pin.OUT)


DEVICE_LABEL = "YOUR_DEVICE_LABEL" # Ubidots device label
TEMPERATURE_VARIABLE_LABEL = "YOUR_TEMP_VARIABLE"  # Ubidots variable label
HUMIDITY_VARIABLE_LABEL = "YOUR_HUM_VARIABLE"  # Ubidots variable label


i = 1 # Counter variable
DELAY = 5  # Delay in seconds

temp_threshold = 25 # prefered temperature limit, value in celcius

# Connect to the WiFi
wifi.connect()

while True:
    on_board_led.on()

    try:
        sensor.measure()
        temperature = sensor.temperature()
        humidity = sensor.humidity()
        print(i)
        i += 1
        print("Temperature is {} degrees Celsius and Humidity is {}%".format(temperature, humidity))
    except Exception as error:
        print("Exception occurred", error)

    temperature_val = temperature
    humidity_val = humidity

    
    data = vis.build_json(TEMPERATURE_VARIABLE_LABEL, temperature, HUMIDITY_VARIABLE_LABEL, humidity)
    returnVal = vis.sendData(DEVICE_LABEL, data)

    if fn.is_too_cold(temperature, temp_threshold):
        green_led.off()
        red_led.on()
    else:
        red_led.off()
        green_led.on()

    on_board_led.off()
    sleep(DELAY)