from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class MyApp(App):

	def build(self):
		self.layout = GridLayout(cols = 2)
		
		self.create_inputs()
		self.create_buttons()

		return self.layout

	def create_buttons(self):
		self.btn_register = Button(text = "Cadastrar")
		self.btn_apagar = Button(text = "Apagar")

		self.layout.add_widget(self.btn_register)
		self.layout.add_widget(self.btn_apagar)

	def create_inputs(self):
		self.text_name = TextInput(multiline=False)
		self.text_cpf = TextInput(multiline=False)
		self.text_datanasc = TextInput(multiline=False)
		self.label_name = Label(text="Nome")
		self.label_cpf = Label(text="CPF")
		self.label_datanasc = Label(text="Data de Nascimento")

		self.layout.add_widget(self.label_name)
		self.layout.add_widget(self.text_name)
		self.layout.add_widget(self.label_cpf)
		self.layout.add_widget(self.text_cpf)
		self.layout.add_widget(self.label_datanasc)
		self.layout.add_widget(self.text_datanasc)

class MyWidget(Widget):
	pass

if __name__ == "__main__":
	MyApp().run()