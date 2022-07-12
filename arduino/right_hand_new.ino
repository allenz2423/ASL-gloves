#include "WiFi.h"
#include<string>
#include <HTTPClient.h>
//#include <Adafruit_MPU6050.h>
//#include <Adafruit_Sensor.h>
//#include <Wire.h>

int THUMB_SPLAY, INDEX_SPLAY, MIDDLE_SPLAY, RING_SPLAY, PINKY_SPLAY, THUMB_CURL, INDEX_CURL, MIDDLE_CURL, RING_CURL, PINKY_CURL;
const char* ssid = "TP-Link_BA40";
const char* password =  "56363968";
const char* SERVER_IP_ADDRESS = "192.168.0.124";

//Adafruit_MPU6050 mpu;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  //  if (!mpu.begin()) {
  //    Serial.println("Failed to find MPU6050 chip");
  //    while (1) {
  //      delay(10);
  //    }
  //  }
  //  Serial.println("MPU6050 Found!");

}
void loop() {
  //  sensors_event_t a, g, temp;
  //  mpu.getEvent(&a, &g, &temp);
  // put your main code here, to run repeatedly:
  THUMB_CURL = analogRead(GPIO_NUM_25);
  INDEX_CURL = analogRead(GPIO_NUM_14);
  MIDDLE_CURL = analogRead(GPIO_NUM_33);
  RING_CURL = analogRead(GPIO_NUM_27);
  PINKY_CURL = analogRead(GPIO_NUM_12);
  reportData();
}

int getOtherArduinoData() {
  int ipAddresses[2];
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(SERVER_IP_ADDRESS, 730);
    int httpCode = http.GET();
    if (httpCode > 0) {
      String response = http.getString();
      ipAddresses[0] = response[0]
      ipAddresses.
      Serial.println(httpCode);
      Serial.println(response);
    } else {
      Serial.println("Error sending GET on: " + String(httpCode);
    }
  }
}

void reportData() {
  String handData = String(THUMB_CURL) + ", " + String(INDEX_CURL) + ", " + String(MIDDLE_CURL) + ", " + String(RING_CURL) + ", " + String(PINKY_CURL) + ", " + String(getOtherArduinoData());
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(SERVER_IP_ADDRESS, 5000);
    http.addHeader("Content-Type", "multipart/form-data");
    int httpResponseCode = http.POST(handData);
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
  delay(10);
}
