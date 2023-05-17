# Importaciones kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from functools import partial

#importaciones locales
from database.operations import IngresarPlaca
from cam import mqtt_init

from kivy import Config

class MyApp(App):  

    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        layout.add_widget(Label(text='Cadula'))
        cedula = TextInput(multiline=False)
        layout.add_widget(cedula)

        layout.add_widget(Label(text='Placa'))
        placa = TextInput(multiline=False)
        layout.add_widget(placa)

        button = Button(text='Registrar', on_release=lambda instance: IngresarPlaca(placa.text, cedula.text))
        layout.add_widget(button)

        return layout
    
def abrirFormulario():
    MyApp().run()

if __name__ == '__main__':
    mqtt_init()