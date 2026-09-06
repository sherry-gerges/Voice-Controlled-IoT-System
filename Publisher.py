import paho.mqtt.client as mqtt
import ssl
import time
import sounddevice as sd
import wavio
import whisper

# MQTT Broker Configuration
MQTT_HOST = "f7559e3e38f94eb7bfc2906b6be26633.s1.eu.hivemq.cloud" 
MQTT_PORT = 8883
MQTT_TOPIC = "SIC/support"
USERNAME = "sherrymegally"
PASSWORD = "********"

print("Loading Whisper model...")
model = whisper.load_model("base") # تحميل موديل Whisper

duration = 3        # مدة التسجيل بالثواني
sample_rate = 16000 # معدل العينات

def record_and_transcribe(filename="command.wav"):
    print("\nListening for your command...")
    command = sd.rec(
        int(duration * sample_rate), 
        samplerate=sample_rate, 
        channels=1, 
        dtype='int16') 
        
    sd.wait()
    wavio.write(filename, command, sample_rate, sampwidth=2)

    result = model.transcribe(filename)
    text = result["text"].strip()

    print("You said: " + text)
    return text

# Initialize MQTT Client
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(cert_reqs=ssl.CERT_REQUIRED)

print(f"Connecting to MQTT Broker {MQTT_HOST}...")
client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_start()

try:
    while True:
        text_command = record_and_transcribe()
        
        if text_command:
            print(f"Publishing message: '{text_command}' to topic '{MQTT_TOPIC}'")
            client.publish(MQTT_TOPIC, text_command)
        
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopping Publisher...")
    client.loop_stop()
    client.disconnect()
