/**
 * @file master.cpp
 * @author DinossauroBebado
 * @brief This code receive the serial data from the python code 
 * and send via ESPNOW to the slave esp with the torrets
 * 
 * @version 0.1
 * @date 2021-07-23
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include <ESP8266WiFi.h>
#include <espnow.h>
#include <Arduino.h>

// REPLACE WITH RECEIVER MAC Address
uint8_t broadcastAddress[] = {0x8C, 0xAA, 0xB5, 0x7B, 0x49, 0xFF};

const int analogInPin = A0; // ESP8266 Analog Pin ADC0 = A0

// Structure example to send data
// Must match the receiver structure
typedef struct struct_message
{
    int x;
    int y;
    bool laser;
} struct_message;

// Create a struct_message called myData
struct_message myData;

unsigned long lastTime = 0;
unsigned long timerDelay = 200; // send readings timer

// Callback when data is sent
void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus)
{
    Serial.print("Last Packet Send Status: ");
    if (sendStatus == 0)
    {
        Serial.println("Delivery success");
    }
    else
    {
        Serial.println("Delivery fail");
    }
}

void setup()
{
    // Init Serial Monitor
    Serial.begin(115200);

    // Set device as a Wi-Fi Station
    WiFi.mode(WIFI_STA);

    // Init ESP-NOW
    if (esp_now_init() != 0)
    {
        Serial.println("Error initializing ESP-NOW");
        return;
    }

    // Once ESPNow is successfully Init, we will register for Send CB to
    // get the status of Trasnmitted packet
    esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
    esp_now_register_send_cb(OnDataSent);

    // Register peer
    esp_now_add_peer(broadcastAddress, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
}

void loop()
{
    if ((millis() - lastTime) > timerDelay)
    {
        // Set values to send
        myData.x = analogRead(analogInPin);
        myData.y = 110;
        myData.laser = false;

        // Send message via ESP-NOW
        esp_now_send(broadcastAddress, (uint8_t *)&myData, sizeof(myData));

        lastTime = millis();
    }
}