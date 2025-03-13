#include <ESP8266WiFi.h>
#include <WebSocketsServer.h>

const char* ssid = "------------------";  
const char* password = "---------------";

WebSocketsServer webSocket(81);
int buzzerPin = D1; 

void setup() {
    Serial.begin(115200);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    
    Serial.println("\nConnected to WiFi");
    webSocket.begin();
    webSocket.onEvent(webSocketEvent);
    
    pinMode(buzzerPin, OUTPUT);
}

void webSocketEvent(uint8_t num, WStype_t type, uint8_t *payload, size_t length) {
    if (type == WStype_TEXT) {
        int fingerCount = atoi((char*)payload);     Serial.printf("Received: %d fingers\n", fingerCount);
        tone(buzzerPin, 500 + (fingerCount * 200));  
        delay(300);  
        noTone(buzzerPin);
    }
}

void loop() {
    webSocket.loop();
}
