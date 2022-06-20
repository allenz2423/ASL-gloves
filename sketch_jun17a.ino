#include "WiFi.h"
#include <iostream>
#include<string>  
#include <HTTPClient.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

int THUMB, INDEX, MIDDLE, RING, PINKY;
const char* ssid = "SSID";
const char* password =  "PASSWORD";

Adafruit_MPU6050 mpu;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println("Connected to the WiFi network");
  if (!mpu.begin()) {
    Serial.println("Failed to find MPU6050 chip");
    while (1) {
      delay(10);
    }
  }
  Serial.println("MPU6050 Found!");
  
}
void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
  // put your main code here, to run repeatedly:
  THUMB = analogRead(GPIO_NUM_36);
  INDEX = analogRead(GPIO_NUM_39);
  MIDDLE = analogRead(GPIO_NUM_34);
  RING = analogRead(GPIO_NUM_35);
  PINKY = analogRead(GPIO_NUM_32);
  if(WiFi.status() == WL_CONNECTED){
    HTTPClient http;
    http.begin("IP", 5000);
    http.addHeader("Content-Type", "multipart/form-data");
    int hand [5] = {THUMB, INDEX, MIDDLE, RING, PINKY};
    int httpResponseCode = http.POST(String(THUMB) + ", " + String(INDEX) + ", " + String(MIDDLE) + ", " + String(RING) + ", " + String(PINKY) + ", " + String(a.acceleration.x) + ", " + String(a.acceleration.y) + ", " + String(a.acceleration.z) + ", " + String(g.gyro.x) + ", " + String(g.gyro.y) + ", " + String(g.gyro.z));

      if(httpResponseCode > 0) {
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
