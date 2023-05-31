#include <Servo.h>

const char* MQTT_BROKER_ADRESS = "192.168.25.226";
const uint16_t MQTT_PORT = 1883;
const char* MQTT_CLIENT_NAME = "ESPClient_2";

Servo servoMotor;

// Topics
const char* DEVICE_TYPE = "Movement";
const char* DEVICE_ID = "3";

WiFiClient espClient;
PubSubClient mqttClient(espClient);

void SuscribeMqtt() {
  mqttClient.subscribe("statuslight");
  mqttClient.subscribe("engine");
}

String payload;

void PublisMqtt(char* topic, unsigned long data) {
   payload = "";
   payload = String(data);
   mqttClient.publish(topic, (char*)payload.c_str());
}

void PublisMqttString(char* topic, char* msg) {
   mqttClient.publish(topic, msg);
}

String message = "";

void OnMqttReceived(char* topic, byte* payload, unsigned int length) {

   message = "";
   for (size_t i = 0; i < length; i++) {
      message.concat((char)payload[i]);
   }

   if(strcmp(topic, "statuslight") == 0){
      if (message[0] == '1'){
         digitalWrite(19, 1);
         digitalWrite(5, 0);
         digitalWrite(18, 0);
      }
      else if (message[0] == '2'){         
         digitalWrite(5, 1);
         digitalWrite(19, 0);
         digitalWrite(18, 0);
      }
      else if (message[0] == '3'){
         digitalWrite(18, 1);
         digitalWrite(5, 0);
         digitalWrite(19, 0);
      }
   }


   if(strcmp(topic, "engine") == 0){

      // abre
      if (message[0] == '1'){
         servoMotor.write(45);
         delay(150); // waits 150ms to reach the position
      }
      // cierra
      if(message[0] == '0'){
         servoMotor.write(95);
         delay(150); // waits 150ms to reach the position
      }
   }
}