from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from functools import partial

from operations import IngresarPlaca


class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10;

        self.add_widget(Label(text='Cadula'))
        self.cedula = TextInput(multiline=False)
        self.add_widget(self.cedula)

        self.add_widget(Label(text='Placa'))
        self.placa = TextInput(multiline=False)
        self.add_widget(self.placa)

        self.button = Button(text='Registrar')
        self.add_widget(self.button)

        self.button.bind(on_press=partial(RegistrarPlaca(self.placa.text)))
        


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10)

        layout.add_widget(Label(text='Cadula'))
        cedula = TextInput(multiline=False)
        layout.add_widget(cedula)

        layout.add_widget(Label(text='Placa'))
        placa = TextInput(multiline=False)
        layout.add_widget(placa)

        button = Button(text='Registrar', on_release=lambda instance: self.RegistrarPlaca(placa.text, cedula.text))
        layout.add_widget(button)


        return layout
    
    def RegistrarPlaca(self,placa,cedula):
        IngresarPlaca(placa,cedula)



if __name__ == '__main__':
    MyApp().run()