# 🎙️ Voice-Controlled IoT System

A voice-controlled IoT system that uses **Whisper Speech Recognition**, **MQTT**, and **HiveMQ Cloud** to control a servo motor and three LEDs connected to a Raspberry Pi.

## 📌 Project Overview

The system consists of two main programs:

* **Publisher:** Records the user's voice, converts it into text using Whisper, and publishes the command through MQTT.
* **Subscriber:** Receives the command from HiveMQ Cloud and controls the Raspberry Pi hardware accordingly.

### System Architecture

```text
             User Voice
                 │
                 ▼
            Microphone
                 │
                 ▼
       Whisper Speech Recognition
                 │
                 ▼
          MQTT Publisher
                 │
                 ▼
          HiveMQ Cloud
          MQTT Broker
                 │
                 ▼
          MQTT Subscriber
                 │
                 ▼
           Raspberry Pi
          ┌──────┼──────┐
          ▼      ▼      ▼
       Servo   LEDs   GPIO
```

## 🛠️ Technologies Used

* Python
* Raspberry Pi
* MQTT
* HiveMQ Cloud
* Paho MQTT
* OpenAI Whisper
* SoundDevice
* Wavio
* GPIO Zero
* SSL/TLS

## 🔌 Hardware Components

* Raspberry Pi
* Servo Motor
* Green LED
* Red LED
* Yellow LED
* Resistors
* Microphone

### GPIO Connections

| Component   | Raspberry Pi GPIO |
| ----------- | ----------------: |
| Servo Motor |           GPIO 21 |
| Green LED   |           GPIO 23 |
| Red LED     |           GPIO 24 |
| Yellow LED  |           GPIO 25 |

## 📡 MQTT Communication

The project uses **HiveMQ Cloud** as the MQTT broker.

```text
Broker: HiveMQ Cloud
Protocol: MQTT
Port: 8883
Security: TLS/SSL
Topic: SIC/support
```

The publisher sends the recognized voice command to the `SIC/support` MQTT topic.

The subscriber listens to the same topic and executes the received command on the Raspberry Pi.

## 🎤 Supported Voice Commands

| Voice Command | Action                                               |
| ------------- | ---------------------------------------------------- |
| `Entering`    | Moves the servo to the middle position for 5 seconds |
| `Getting out` | Moves the servo and turns off all LEDs               |
| `Lights on`   | Turns on all three LEDs                              |
| `Area 1`      | Turns on the green LED                               |
| `Area 2`      | Turns on the red LED                                 |
| `Area 3`      | Turns on the yellow LED                              |

## 🧠 Speech Recognition

The publisher uses **OpenAI Whisper** to convert speech into text.

The current implementation uses the `base` Whisper model.

Audio is recorded using:

```text
Duration: 3 seconds
Sample Rate: 16000 Hz
Channels: 1
```

The recognized text is then published to HiveMQ Cloud through MQTT.

## 📂 Project Structure

```text
Voice-Controlled-IoT/
│
├── publisher.py
├── subscriber.py
├── README.md
└── .gitignore
```

The `command.wav` file is generated automatically during recording and does not need to be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

### 2. Install the Required Libraries

```bash
pip install paho-mqtt
pip install sounddevice
pip install wavio
pip install openai-whisper
pip install gpiozero
```

## 🔐 MQTT Credentials

For security, MQTT credentials should **not** be stored directly in the source code.

Use environment variables instead:

```python
import os

USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")
```

Example:

```bash
export MQTT_USERNAME="your_username"
export MQTT_PASSWORD="your_password"
```

Add the following to `.gitignore`:

```text
.env
command.wav
__pycache__/
*.pyc
```

> **Important:** Never upload your real HiveMQ password or other private credentials to GitHub.

## ▶️ How to Run

### 1. Run the Subscriber

On the Raspberry Pi:

```bash
python subscriber.py
```

The subscriber will connect to HiveMQ Cloud and wait for MQTT messages.

Expected output:

```text
Connecting to MQTT Broker...
MQTT Subscriber is running and waiting for messages...
```

### 2. Run the Publisher

Run the publisher:

```bash
python publisher.py
```

The program will load the Whisper model and start listening for voice commands.

Example:

```text
Listening for your command...
You said: area 1
Publishing message: 'area 1' to topic 'SIC/support'
```

The subscriber receives the message through HiveMQ Cloud and activates the corresponding hardware.

## 🔒 Secure MQTT Connection

The connection to HiveMQ Cloud uses **TLS/SSL encryption** on port `8883`.

```python
client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
```

This provides encrypted communication between the MQTT clients and the HiveMQ Cloud broker.

## ✨ Features

* 🎙️ Voice-controlled IoT system
* 🧠 AI-based speech recognition using Whisper
* 📡 MQTT communication
* ☁️ HiveMQ Cloud MQTT broker
* 🔐 TLS/SSL secure communication
* 🥧 Raspberry Pi GPIO control
* 🚪 Servo motor control
* 💡 Three-zone LED control
* 🟢 Area 1 control
* 🔴 Area 2 control
* 🟡 Area 3 control

## 🚀 Future Improvements

* Add more voice commands
* Support Arabic voice commands
* Add an LCD display
* Add sensors for automatic control
* Add a GUI
* Add voice feedback
* Improve command recognition
* Add MQTT status messages
* Optimize Whisper for faster processing

## 👩‍💻 Author

**Sherry Gerges**

**Mohamed Khaled**

**Alhussein Ahmed**


Electrical Engineering Student

Interested in:

* IoT
* Embedded Systems
* Communication Systems
* Python
* Raspberry Pi

## 📜 License

This project was developed for educational and development purposes.
