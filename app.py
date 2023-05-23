from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy import Config
from functools import partial

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

def on_message(client, userdata, message):
	processedMessage = message.payload.decode()
	topic = message.topic

	if topic == "camera" and processedMessage == "1":
		cameraHandler()

class MyApp(App):
    client = mqtt.Client()
    client.connect("localhost", 1883)
    client.subscribe("camera")
    client.on_message = on_message
    client.loop_start()

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        layout.add_widget(Label(text='Cadula'))
        cedula = TextInput(multiline=False)
        layout.add_widget(cedula)

        layout.add_widget(Label(text='Placa'))
        placa = TextInput(multiline=False)
        layout.add_widget(placa)

        button = Button(text='Registrar', on_release=lambda instance: createVehicle(placa.text, cedula.text))
        layout.add_widget(button)

        return layout

if __name__ == '__main__':
    MyApp().run()
