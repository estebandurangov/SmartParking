/* ----- Include Libraries ----- */
#include <WiFi.h>
#include <PubSubClient.h>
#include <Servo.h>

/* ----- Third Libraries ----- */
#include "config.h"  // Set your network SSID and password in this file
#include "MQTT.hpp"
#include "ESP32_Utils.hpp"
#include "ESP32_Utils_MQTT.hpp"

/* ----- Ports ----- */
#define LINEAR_HALL_ENTRANCE 34
#define LINEAR_HALL_EXIT 32
#define RED 19
#define GREEN 18
#define BLUE 5
#define SERVO 26


/* ----- Variables ----- */
long mov_timer = 0;

char msg[50];
int sensorValueEntrance;
int sensorValueExit;
int previousSensorValue = 100;
int sensorStatus = 0;
//Servo servoMotor;

/* Topics */
char topicCamera[] = "camera";
char topicMotor[] = "engine";

/* ----- Main funtions ----- */

// setup
void setup() {

  // set PIN_PIR a pin as an input
  pinMode(LINEAR_HALL_ENTRANCE, INPUT);
  pinMode(LINEAR_HALL_EXIT, INPUT);
  pinMode(RED, OUTPUT);
  pinMode(GREEN, OUTPUT);
  pinMode(BLUE, OUTPUT);
  servoMotor.attach(SERVO);

  // Serial setup
  Serial.begin(9600);  
  ConnectWiFi_STA(false);
  servoMotor.write(95);
  InitMqtt();
  delay(5000);
}

// loop
void loop() {

  HandleMqtt();
  long now = millis(); 

  //get sensor data each 500ms 
  if (now - mov_timer > 500) { 
    mov_timer = now;
    int sensorValueEntrance = analogRead(LINEAR_HALL_ENTRANCE);
    int sensorValueExit = analogRead(LINEAR_HALL_EXIT);
    if(sensorValueEntrance > 3000 && previousSensorValue < 500){
      snprintf (msg, 50, "1");
      PublisMqttString(topicCamera, msg);
      sensorStatus = 1;
    }
    if(sensorValueExit > 3000 && sensorStatus == 1){
      snprintf (msg, 50, "0");
      PublisMqttString(topicMotor, msg);
      digitalWrite(19, 0);
      digitalWrite(5, 0);
      digitalWrite(18, 0);
      sensorStatus = 0;
    }
    previousSensorValue = sensorValueEntrance;
  }

}