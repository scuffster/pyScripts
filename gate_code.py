import wifi
import socketpool
import ssl
import adafruit_requests
import time
from adafruit_minimqtt.adafruit_minimqtt import MQTT
import board
from adafruit_motorkit import MotorKit
import microcontroller
import storage
from secrets import secrets  # Import credentials from secrets.py

# Wi-Fi credentials and Adafruit IO keys from secrets.py
WIFI_SSID = secrets["ssid"]
WIFI_PASSWORD = secrets["password"]
AIO_USERNAME = secrets["aio_username"]
AIO_KEY = secrets["aio_key"]

# OTA URL to fetch updated code
FIRMWARE_URL = "https://raw.githubusercontent.com/scuffster/pyScripts/refs/heads/master/gate_code.py"  # Direct raw file URL

# Connect to Wi-Fi
def connect_wifi():
    print("Connecting to Wi-Fi...")
    wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
    print(f"Connected to {WIFI_SSID}!")

# Initialize MQTT
def initialize_mqtt():
    global mqtt_client
    pool = socketpool.SocketPool(wifi.radio)
    ssl_context = ssl.create_default_context()

    mqtt_client = MQTT(
        broker="io.adafruit.com",
        port=1883,
        username=AIO_USERNAME,
        password=AIO_KEY,
        socket_pool=pool,
        ssl_context=ssl_context,
        keep_alive=60,
        socket_timeout=15,
        recv_timeout=20
    )

# Publish logs to Adafruit IO
def publish_log(message):
    """Publish log messages to the 'gate_console_log' feed."""
    try:
        mqtt_client.publish(f"{AIO_USERNAME}/feeds/gate_console_log", message)
    except Exception as e:
        print(f"Failed to publish log: {e}")

# OTA Update Functionality
def check_and_update_firmware():
    print("Checking for updates...")
    try:
        pool = socketpool.SocketPool(wifi.radio)
        ssl_context = ssl.create_default_context()
        requests = adafruit_requests.Session(pool, ssl_context)

        response = requests.get(FIRMWARE_URL)
        if response.status_code == 200:
            print("Update found! Downloading...")
            publish_log("OTA update: Downloading new firmware")

            # Save new code to /code.py
            storage.remount("/", readonly=False)
            with open("/code.py", "wb") as f:
                f.write(response.content)
            print("Update complete. Rebooting...")
            publish_log("OTA update: Completed, rebooting")

            # Reboot to apply update
            microcontroller.reset()
        else:
            print("No update found.")
            publish_log("OTA update: No new updates available")

    except Exception as e:
        print(f"Error during OTA update: {e}")
        publish_log(f"OTA update failed: {e}")

# Motor Control Logic
def on_message(client, feed_id, message):
    publish_log(f"Received {message} on {feed_id}")
    if feed_id == f"{AIO_USERNAME}/feeds/shield_feed":
        if message == "extend":
            publish_log("Extending actuator")
            motor.throttle = 1.0
            time.sleep(9)
            motor.throttle = 0
        elif message == "retract":
            publish_log("Retracting actuator")
            motor.throttle = -1.0
            time.sleep(9)
            motor.throttle = 0
        else:
            publish_log("Stopping actuator")
            motor.throttle = 0

# Main program
try:
    # Connect to Wi-Fi
    connect_wifi()

    # Initialize motor
    kit = MotorKit(i2c=board.I2C())
    motor = kit.motor4

    # Check for OTA updates
    check_and_update_firmware()

    # Initialize MQTT
    initialize_mqtt()
    mqtt_client.connect()
    publish_log("Connected to Adafruit IO!")
    mqtt_client.on_message = on_message
    mqtt_client.subscribe(f"{AIO_USERNAME}/feeds/shield_feed")

    # Main loop
    while True:
        try:
            mqtt_client.loop(timeout=20)
            time.sleep(0.5)
        except Exception as e:
            publish_log(f"Error in loop: {e}")

except Exception as e:
    publish_log(f"Startup Error: {e}")
