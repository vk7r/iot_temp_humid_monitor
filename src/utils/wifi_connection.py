import network
from time import sleep
import utils.keys as keys


WIFI_SSID = keys.WIFI_SSID # Assign your the SSID of your network
WIFI_PASS = keys.WIFI_PASS # Assign your the password of your network

# Connect to WIFI
def connect():
    wlan = network.WLAN(network.STA_IF)     # Put modem on Station mode

    if not wlan.isconnected():                  
        print('connecting to network...')
        wlan.active(True)                   # Activate network interface
        wlan.config(pm = 0xa11140)
        wlan.connect(WIFI_SSID, WIFI_PASS)  # Your WiFi Credentials
        print('Waiting for connection...', end='')
        
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    
    # Print the IP
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip