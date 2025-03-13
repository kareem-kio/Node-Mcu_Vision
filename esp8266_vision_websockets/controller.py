import websocket
import threading
import time

ESP_IP = "ws://192.168.1.6:81"  #   My esp ip in network

ws = websocket.WebSocket()

#timer to send the data each 2 seconds
last_sent_time = 0

def connect_ws():
    """Try to connect to the ESP8266 WebSocket server."""
    while True:
        try:
            ws.connect(ESP_IP)
            print("[✓] Connected to ESP8266 WebSocket")
            break
        except Exception as e:
            print(f"[!] WebSocket retrying... {e}")
            time.sleep(2)

# using multi threading
threading.Thread(target=connect_ws, daemon=True).start()

def led(finger_count):
    """Send the detected finger count to ESP8266 via WebSocket."""
    global last_sent_time

    # send every 2 seconds
    if time.time() - last_sent_time >= 2:
        try:
            ws.send(str(finger_count))  # sending finger count
            print(f"[→] Sent to ESP: {finger_count}")
            last_sent_time = time.time()  # putting time at the current as the last sent time
        except Exception:
            print("[!] Connection lost. Reconnecting...")
            threading.Thread(target=connect_ws, daemon=True).start()