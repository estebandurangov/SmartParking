#include <Servo.h>

const char* MQTT_BROKER_ADRESS = "192.168.43.4";
const uint16_t MQTT_PORT = 1883;
const char* MQTT_CLIENT_NAME = "ESPClient_2";

Servo servoMotor;

// Topics
const char* DEVICE_TYPE = "Movement";
const char* DEVICE_ID = "3";

WiFiClient espClient;
PubSubClient mqttClient(espClient);

void SuscribeMqtt() {
  mqttClient.subscribe("motor");
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

String content = "";

void OnMqttReceived(char* topic, byte* payload, unsigned int length) {
   content = "";   
   for (size_t i = 0; i < length; i++) {
      content.concat((char)payload[i]);
   }

   if (content[0] == '1'){
      Serial.println(servoMotor.read());
      //if(servoMotor.read()<90)
         servoMotor.write(95);
         //delay(15); // waits 15ms to reach the position
      
   }

   if (content[0] == '0'){
      servoMotor.write(1);
   }
}
