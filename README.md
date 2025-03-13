# Hand Gesture Controlled ESP8266 Buzzer

## 🚀 Overview
This project integrates **computer vision** and **IoT** to control an ESP8266 buzzer using **hand gestures** detected via a webcam. The system detects the number of raised fingers and sends the count to the ESP8266 over WebSockets, triggering different buzzer tones accordingly.

## 🔥 Features
✅ **Hand Tracking:** Uses **MediaPipe** to detect hand landmarks and count raised fingers.  
✅ **WebSocket Communication:** Real-time data transfer from the vision model to the ESP8266.  
✅ **Buzzer Feedback:** The ESP8266 receives finger count and plays corresponding buzzer tones.  
✅ **Multithreading:** Ensures a seamless WebSocket connection.  

---

## 🛠️ System Components
### 1️⃣ ESP8266 (IoT Module)
- Connects to WiFi and listens for WebSocket messages.
- Triggers a buzzer based on received finger count.

### 2️⃣ Python Controller (WebSocket Client)
- Establishes a WebSocket connection to the ESP8266.
- Sends detected finger count every **2 seconds**.

### 3️⃣ Computer Vision Model
- Captures video using **OpenCV**.
- Uses **MediaPipe Hands** to track hand landmarks.
- Counts raised fingers and sends the count to the controller.

---

## 🔧 Installation & Setup
### 📌 Prerequisites
- **ESP8266 Board**
- **Python 3.7+**
- Install Required Libraries:
  ```bash
  pip install opencv-python mediapipe websocket-client
  ```
- **Arduino IDE** with ESP8266 Board Manager

### ⚡ Wiring for ESP8266
| ESP8266 Pin | Component |
|------------|----------|
| D1         | Buzzer   |

### 📡 Uploading ESP8266 Code
1. Open **Arduino IDE**.
2. Install the **ESP8266 Board Package**.
3. Replace `ssid` and `password` with your WiFi credentials.
4. Upload `esp8266_code.ino` to the ESP8266.

### ▶️ Running the Python Scripts
1. Start the **vision model**:
   ```bash
   python main.py
   ```
2. Ensure ESP8266 is connected and running.
3. The buzzer will trigger based on detected gestures.

---

## 🎮 Usage
🔹 Raise **0 to 5 fingers** to trigger different buzzer tones.  
🔹 Press `q` to exit the vision model.  

---


## 🔮 Future Improvements
🚀 Add **LED indicators** for visual feedback.  
🚀 Optimize **gesture recognition** using deep learning.  
🚀 Improve **error handling** in WebSocket communication.  

---

## 📜 License
This project is licensed under the MIT License.  

**Copyright (c) 2024 Kareem Amr Mahmoud Sultan**  


*If you find this project helpful, consider giving it a ⭐ on GitHub!*

