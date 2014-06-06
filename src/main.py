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
		
		self.create_labels_text()
		self.create_buttons()

		return self.layout

	def create_buttons(self):
		self.btn_register = Button(text = "Cadastrar")
		self.btn_apagar = Button(text = "Apagar")

		self.layout.add_widget(self.btn_register)
		self.layout.add_widget(self.btn_apagar)

	def create_labels_text(self):
		names = ['Nome', 'CPF', 'Data de Nascimento','CoolSttuf']
		self.lines_on_grid = []

		for name in names:
			text = TextInput(multiline=False)
			label = Label(text=name)

			line = (label,text)
			self.layout.add_widget(label)
			self.layout.add_widget(text)

class MyWidget(Widget):
	pass

if __name__ == "__main__":
	MyApp().run()