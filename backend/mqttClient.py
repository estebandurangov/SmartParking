import paho.mqtt.client as mqtt
import time
from picamera2 import Picamera2, Preview
import json

# local imports
from model.plateRecognition import processPlate
from database.operations import readPlate
from database.operations import createVehicle

def takePicture(route):
	picam2 = Picamera2()
	preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
	picam2.configure(preview_config)
	picam2.start_preview(Preview.QTGL)
	picam2.start()
	time.sleep(2)
	picam2.capture_file(route)
	picam2.close()

def cameraHandler():
	fileRoute = '/home/admin/IoT/SmartParking/backend/platePicture.jpg'
	#takePicture(fileRoute)
	plate = processPlate(fileRoute)
	open = readPlate(plate)
	if (open):
		print("\nAbriendo puerta")
		#client.publish("egine", "1")
	else:
		print('\nNo puedo abrir puerta')
		#client.publish("luz_ingreso","1") # 1 => prende rojo => acceso denegado. 2 => prende azul => procesando. 3 => prende verde => acceso permitido

def newVehicleHandler(data):
	print("MIRE LA DATA: ",data)
	newVehicle = json.loads(data)
	createVehicle(newVehicle["placa"], newVehicle["user_id"])

def on_message(client, userdata, message):
	processedMessage = message.payload.decode()
	topic = message.topic

	if topic == "camera" and processedMessage == "1":
		cameraHandler()

	if topic == "newvehicle":
		newVehicleHandler(processedMessage)

def mqtt_init():
	client = mqtt.Client()
	client.connect("localhost", 1883)
	client.subscribe("camera")
	client.subscribe("newvehicle")
	client.on_message = on_message
	client.loop_forever()
 
if __name__ == '__main__':
	mqtt_init()