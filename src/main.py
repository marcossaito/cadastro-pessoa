import os

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from mensseges import MenssegerPopup
from dbservice import DBservice

class MyApp(App):

	def build(self):
		self.layout = GridLayout(cols = 2)
		
		self.create_labels_text()
		self.create_buttons()

		return self.layout

	def create_buttons(self):
		self.btn_register = Button(text = "Cadastrar")
		self.btn_register.bind(on_press=self.action_btn_register)

		self.btn_apagar = Button(text = "Apagar")
		self.btn_apagar.bind(on_press=self.clear_all_text)

		self.layout.add_widget(self.btn_register)
		self.layout.add_widget(self.btn_apagar)

	def action_btn_register(self,instance):
		db = DBservice("sigma")
		input_texts = []

		for index in range(len(self.texts_on_grid)):
			input_texts.append(self.texts_on_grid[index].text)

		t = tuple(input_texts)

		confirm = db.insert_user(t)

		if confirm:
			popup = MenssegerPopup("Sucsses","All Done!")
			popup.show_me()

		else:
			MenssegerPopup("Error","Ok")
			popup.show_me()
			self.clear_all_text(self.btn_register)

		self.clear_all_text(instance)

	def clear_all_text(self,instance):

		for text_input  in self.texts_on_grid:
			text_input.text = ''

	def create_labels_text(self):
		names = ['Nome', 'CPF', 'Data de Nascimento']
		self.texts_on_grid = []
		self.labels_on_grid = []

		for name in names:
			text = TextInput(multiline=False,size=(.5,.5))
			self.texts_on_grid.append(text)
			label = Label(text=name)
			self.labels_on_grid.append(label)

			self.layout.add_widget(label)
			self.layout.add_widget(text)

class MyWidget(Widget):
	pass

if __name__ == "__main__":
	MyApp().run()