#include "WiFi.h"
#include<string>
#include <HTTPClient.h>
const char* ssid = "TP-Link_BA40";
const char* password =  "56363968";
const char* IP_ADDRESS = "192.168.0.124";
int THUMB_SPLAY, INDEX_SPLAY, MIDDLE_SPLAY, RING_SPLAY, PINKY_SPLAY, THUMB_CURL, INDEX_CURL, MIDDLE_CURL, RING_CURL, PINKY_CURL;
const String message = "TAKE MY IP";
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
}

void loop() {
  // put your main code here, to run repeatedly:
  THUMB_CURL = analogRead(GPIO_NUM_36);
  INDEX_CURL = analogRead(GPIO_NUM_39);
  MIDDLE_CURL = analogRead(GPIO_NUM_34);
  RING_CURL = analogRead(GPIO_NUM_35);
  PINKY_CURL = analogRead(GPIO_NUM_33);
  sendToServer();
  delay( 50 );
}

//bool receivedFromArduino(){
//  if(WiFi.status() == WL_CONNECTED) {
//    HTTPClient http;
//    
//  }
//}

void sendToServer() {
  if(WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(IP_ADDRESS, 730);
    http.addHeader("Content-Type", "multipart/form-data");
    int httpResponseCode = http.POST(message);
  }
}

void communicateWithOtherArduinos() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(IP_ADDRESS, 5000);
    http.addHeader("Content-Type", "multipart/form-data");
    int httpResponseCode = http.POST(String(THUMB_CURL) + ", " + String(INDEX_CURL) + ", " + String(MIDDLE_CURL) + ", " + String(RING_CURL) + ", " + String(PINKY_CURL));
    //    String(a.acceleration.y) + ", " + String(a.acceleration.z) + ", " + String(g.gyro.x) + ", " + String(g.gyro.y) + ", " + String(g.gyro.z)
    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.println(httpResponseCode);
      Serial.println(response);

    } else {
      Serial.print("Error sending POST on: ");
      Serial.println(httpResponseCode);
    }
    http.end();
  } else {
    Serial.println("Yo wifi broke");
  }
}
