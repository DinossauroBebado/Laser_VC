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
    int x; //fio laranja
    int y; //fio azul
    bool laser;
} struct_message;

// Create a struct_message called myData
struct_message myData;

Servo servoX;
Servo servoY; // Cria um objeto servo

int valX;
int valY;

int laserPin = 13; //D7
bool LaserState = false;
// Callback function that will be executed when data is received
void OnDataRecv(uint8_t *mac, uint8_t *incomingData, uint8_t len)
{
    memcpy(&myData, incomingData, sizeof(myData));

    Serial.print("X: ");
    Serial.println(myData.x);
    Serial.print("Y: ");
    Serial.println(myData.y);
    Serial.print("Laser: ");
    Serial.println(myData.laser); //bool pra saber se o laser esta ligado ou desligado
    Serial.println();

    valX = map(myData.x, 500, 0, 0, 170);
    valY = map(myData.y, 500, 0, 0, 170);

    Serial.println(valX);
    Serial.println(valY);

    servoY.write(valY);
    servoX.write(valX);

    if (myData.laser)
    {
        digitalWrite(laserPin, HIGH);
    }
    else
    {
        digitalWrite(laserPin, LOW);
    }
}
//coment
void setup()
{
    servoX.attach(14); //D5
    servoY.attach(12); //D6
    pinMode(laserPin, OUTPUT);
    digitalWrite(laserPin, HIGH);
    delay(500);
    digitalWrite(laserPin, LOW);
    delay(500);
    digitalWrite(laserPin, HIGH);
    delay(500);
    digitalWrite(laserPin, LOW);
    delay(500);
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