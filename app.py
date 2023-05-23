import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

import paho.mqtt.client as mqtt
import time
from picamera2 import Picamera2, Preview

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
	fileRoute = '/home/admin/IoT/SmartParking/platePicture.jpg'
	#takePicture(fileRoute)
	plate = processPlate(fileRoute)
	open = readPlate(plate)
	if (open):
		print("\nAbriendo puerta")
		#client.publish("engine", "1")
	else:
		print('\nNo puedo abrir puerta')
		#client.publish("luz_ingreso","1") # 1 => prende rojo => acceso denegado. 2 => prende azul => procesando. 3 => prende verde => acceso permitido

class MyBox(BoxLayout):
	pass

class EdgeApp(App):
	
	def build(self):
		return MyBox()

	def registerHandler(self, cedula, placa):
		result = createVehicle(cedula, placa)
		self.client.publish("register", result)
	
	def on_start(self):
		
		def on_message(client, userdata, message):
			processedMessage = str(message.payload.decode("utf-8"))
			topic = message.topic

			if topic == "camera" and processedMessage == "1":
				cameraHandler()

			if topic == "register":
				userdata['self'].root.ids.registrar_label.text = str(message.payload.decode("utf-8"))
		
		parameters = {'self':self}
		self.client = mqtt.Client(client_id='p1',
									clean_session = True,
									userdata = parameters)
		self.client.connect("localhost", 1883)
		self.client.on_message = on_message
		self.client.subscribe("camera")
		self.client.subscribe("register")
		self.client.loop_start()
	
if __name__ == "__main__":
	EdgeApp().run()
