import paho.mqtt.client as mqtt
import ssl
import time
from gpiozero import Servo, LED


servo = Servo(21)
green_led = LED(23)
red_led = LED(24)
yellow_led = LED(25)

# MQTT Broker Configuration
MQTT_HOST = "f7559e3e38f94eb7bfc2906b6be26633.s1.eu.hivemq.cloud" 
MQTT_PORT = 8883
MQTT_TOPIC = "SIC/support"
USERNAME = "sherrymegally"
PASSWORD = "********"

def execute_command(text):
    text_lower = text.lower()
    
    if "entering" in text_lower:
        print("Entering...")
        servo.mid()
        time.sleep(5)
        servo.detach()
        
    elif "getting out" in text_lower:
        print("Getting out...")
        servo.mid()
        time.sleep(5)
        servo.detach()
        green_led.off()
        red_led.off()
        yellow_led.off()

    elif "lights on" in text_lower:
        green_led.on()
        red_led.on()
        yellow_led.on()
        print("Lights are on.")

    elif "area 1" in text_lower:
        green_led.on()
        red_led.off()
        yellow_led.off()
        print("Area 1 lights are on.")

    elif "area 2" in text_lower:
        green_led.off()
        red_led.on()
        yellow_led.off()
        print("Area 2 lights are on.")

    elif "area 3" in text_lower:
        green_led.off()
        red_led.off()
        yellow_led.on()
        print("Area 3 lights are on.")

    else:
        print("Command not recognized.")

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    print(f"\n[Received from MQTT Broker]: '{payload}' on topic '{msg.topic}'")
    execute_command(payload)

# Initialize MQTT Client
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

client.on_message = on_message

print(f"Connecting to MQTT Broker {MQTT_HOST}...")
client.connect(MQTT_HOST, MQTT_PORT, 60)
client.subscribe(MQTT_TOPIC)

print("MQTT Subscriber is running and waiting for messages...")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("\nDisconnecting...")
    client.disconnect()
