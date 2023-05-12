/* ----- Include Libraries ----- */
#include <WiFi.h>
#include <PubSubClient.h>
#include <Servo.h>
#include <IRremote.h>

/* ----- Third Libraries ----- */
#include "config.h"  // Set your network SSID and password in this file
#include "MQTT.hpp"
#include "ESP32_Utils.hpp"
#include "ESP32_Utils_MQTT.hpp"

/* ----- Ports ----- */
#define LINEAR_HALL_SENSOR 34               // Pin for PIR sensor in the esp32 board
#define SERVO_PIN 26 // ESP32 pin GIOP26 connected to servo motor
#define IR_PIN 21   //IR Receiver Pin 3

/* ----- Variables ----- */
long mov_timer = 0;
long mov_timer2 = 0;
long ka_timer = 0;

char msg[50];
int sensorValue;
int previousSensorValue = 1901;

decode_results results;

// Servo servoMotor;
IRrecv irrecv(IR_PIN);

/* Topics */
char topicSensor[] = "sensor";
char topicMotor[] = "motor";

/* ----- Main funtions ----- */

// setup
void setup() {
  irrecv.enableIRIn();

  // set PIN_PIR a pin as an input
  pinMode(LINEAR_HALL_SENSOR, INPUT);
  servoMotor.attach(SERVO_PIN);  // attaches the servo on ESP32 pin

  // Serial setup
  Serial.begin(9600);  
  ConnectWiFi_STA(false);
  InitMqtt();
  delay(5000);
}

// loop
void loop() {

  if (irrecv.decode(&results)){
    long int decCode = results.value;
    Serial.println(results.value);
    irrecv.resume();
    delay(10);
  }

  // HandleMqtt();
  // long now = millis(); 
  // //get sensor data each 500ms 
  // if (now - mov_timer > 500) { 
  //   mov_timer = now;
  //   int sensorValue = analogRead(LINEAR_HALL_SENSOR);
  //   Serial.println(sensorValue);
  //   if(sensorValue < 1900 && previousSensorValue > 1900){
  //     snprintf (msg, 50, "1");
  //     PublisMqttString(topicSensor, msg);
  //   }
  //   previousSensorValue = sensorValue;
  // }

  // Sending Keep Alive message each 5 seconds
  // if (now - ka_timer > 5000) { 
  //   ka_timer = now;
  //   // DeviceID=3,ONLINE_STATE
  //   snprintf (msg, 50, "3,100" );
  //   Serial.print("Sending Movement keep alive message to Rpi: ");
  //   Serial.println(msg);
  //   PublisMqttString(topicSensor, msg);
  // }
}