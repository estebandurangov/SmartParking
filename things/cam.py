import paho.mqtt.client as mqtt
import time
from picamera2 import Picamera2, Preview
from plateRecognition import reconocerPlaca
from model.operations import buscarPlaca

def TomarFoto():
	picam2 = Picamera2()
	preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
	picam2.configure(preview_config)
	picam2.start_preview(Preview.QTGL)
	picam2.start()
	time.sleep(2)
	metadata = picam2.capture_file("test.jpg")
	picam2.close()

def on_message(client, userdata, message):
	print(message.payload.decode())
	if ((message.payload.decode()) == "1"):
		print(type(client))
		#print(message.mid)
		TomarFoto()
		placaFoto = reconocerPlaca()
		placaFotoLimpia = placaFoto.strip()
		abrir = buscarPlaca(placaFotoLimpia)
		if (abrir):
			print("oeoeoeoe")
		# 	client.publish("motor", "1")
		else:
			client.publish("luz_ingreso","1") # 1 => prende rojo => acceso denegado. 2 => prende azul => procesando. 3 => prende verde => acceso permitido

client = mqtt.Client()
client.connect("localhost", 1883)
client.subscribe("sensor")

client.on_message = on_message

client.loop_forever()
 
