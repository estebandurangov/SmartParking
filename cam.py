import paho.mqtt.client as mqtt
import time
from picamera2 import Picamera2, Preview
from mlModel.plateRecognition import reconocerPlaca
from database.operations import buscarPlaca

from layout import app

def tomar_foto():
	picam2 = Picamera2()
	preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
	picam2.configure(preview_config)
	picam2.start_preview(Preview.QTGL)
	picam2.start()
	time.sleep(2)
	metadata = picam2.capture_file("/home/admin/IoT/SmartParking/things/test.jpg")
	picam2.close()

def on_message(client, userdata, message):
	print(message.payload.decode())
	if ((message.payload.decode()) == "1"):
		print(type(client))
		#print(message.mid)
		tomar_foto()
		placaFoto = reconocerPlaca()
		abrir = buscarPlaca(placaFoto)
		if (abrir):
			print("oeoeoeoe")
		 	#client.publish("motor", "1")
		else:
			print('no se encontro')
			#abrirFormulario()
		#	client.publish("luz_ingreso","1") # 1 => prende rojo => acceso denegado. 2 => prende azul => procesando. 3 => prende verde => acceso permitido
			

def mqtt_init():
	client = mqtt.Client()
	client.connect("localhost", 1883)
	client.subscribe("sensor")

	client.on_message = on_message

	client.loop_forever()
 
if __name__ == '__main__':
	mqtt_init()