/**
 * @file slave.cpp
 * @author DinossauroBebado
 * @brief this code receive the cordenades from the master 
 * esp and tranform to degres for the X and Y axis 
 * @version 0.1
 * @date 2021-07-23
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include <ESP8266WiFi.h>
#include <espnow.h>
#include <Servo.h>
#include <Arduino.h>

// Structure example to receive data
// Must match the sender structure
typedef struct struct_message
{
    int x; //fio azul
    int y; //fio laranja
    bool laser;
} struct_message;

// Create a struct_message called myData
struct_message myData;

Servo servoX;
Servo servoY; // Cria um objeto servo

int valX;
int valY;
int laserPin = 13; //D7
bool lastLaserState = false;
// Callback function that will be executed when data is received
void OnDataRecv(uint8_t *mac, uint8_t *incomingData, uint8_t len)
{
    memcpy(&myData, incomingData, sizeof(myData));
    Serial.print("Bytes received: ");
    Serial.println(len);
    Serial.print("X: ");
    Serial.println(myData.x);
    Serial.print("Y: ");
    Serial.println(myData.y);
    Serial.print("Laser: ");
    Serial.println(myData.laser); //bool pra saber se o laser esta ligado ou desligado
    Serial.println();

    if (myData.laser == true && lastLaserState == false)
    {
        digitalWrite(laserPin, HIGH);
    }
    else
    {
        digitalWrite(laserPin, LOW);
    }
    lastLaserState = myData.laser;

    valX = map(myData.x, 0, 1023, 45, 150);
    valY = map(myData.y, 0, 1023, 45, 150);

    servoY.write(valY);
    servoX.write(valX);
}

void setup()
{
    servoX.attach(14); //D5
    servoY.attach(12); //D6
    pinMode(laserPin, OUTPUT);
    // Initialize Serial Monitor
    Serial.begin(115200);

    // Set device as a Wi-Fi Station
    WiFi.mode(WIFI_STA);

    // Init ESP-NOW
    if (esp_now_init() != 0)
    {
        Serial.println("Error initializing ESP-NOW");
        return;
    }

    // Once ESPNow is successfully Init, we will register for recv CB to
    // get recv packer info
    esp_now_set_self_role(ESP_NOW_ROLE_SLAVE);
    esp_now_register_recv_cb(OnDataRecv);
}

void loop()
{
}