/* ----- Include Libraries ----- */
#include <WiFi.h>
#include <PubSubClient.h>

/* ----- Third Libraries ----- */
#include "config.h"  // Set your network SSID and password in this file
#include "MQTT.hpp"
#include "ESP32_Utils.hpp"
#include "ESP32_Utils_MQTT.hpp"

/* ----- Ports ----- */
#define PIR_MOTION_SENSOR 13               // Pin for PIR sensor in the esp32 board

/* ----- Variables ----- */
long mov_timer = 0;
long ka_timer = 0;

char msg[50];
int value = 0;

// Variable state represents home state-> 0 normal  - 1 lookout
char home_state = 0;

/* Topics */
char topic[] = "sensor";

/* ----- Main funtions ----- */

// setup
void setup() {
  // set PIN_PIR a pin as an input
  pinMode(PIR_MOTION_SENSOR, INPUT);   
  // Serial setup
  Serial.begin(9600);  
  ConnectWiFi_STA(false);
  InitMqtt();
  delay(5000);
}

// loop
void loop() {
  HandleMqtt();
  long now = millis(); 
  //get PIR data each 500ms 
  if (now - mov_timer > 500) { 
    mov_timer = now;
    Serial.print(home_state);
    int sensorResponse = digitalRead(PIR_MOTION_SENSOR);
    Serial.print("ATENCION");
    Serial.print(sensorResponse);
    // if(){//if it detects the moving people?
    //       snprintf (msg, 50, "oelo");
    //       Serial.print("Publish message: ");115200
    //       Serial.println(msg);
    //       PublisMqttString(topic, msg);
    // }
  }

  // Sending Keep Alive message each 5 seconds
  if (now - ka_timer > 5000) { 
    ka_timer = now;
    // DeviceID=3,ONLINE_STATE
    snprintf (msg, 50, "3,100" );
    Serial.print("Sending Movement keep alive message to Rpi: ");
    Serial.println(msg);
    PublisMqttString(topic, msg);
  }
  
}