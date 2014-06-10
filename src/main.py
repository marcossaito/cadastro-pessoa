import os

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.camera import Camera

from mensseges import MenssegerPopup
from dbservice import DBservice

class MyApp(App):

	def build(self):
		
		self.layout1 = GridLayout(cols = 2,size_hint=(.7,1),pos_hint={'x':.0,'y':.001})
		self.layout_to_show = FloatLayout(size=(300,300))
		
		self.layout_to_show.add_widget(self.layout1)

		self.cam = Camera(play=False,size_hint=(.245,.245),pos_hint={'x':.726,'y':.7})
		self.button_take_photo = Button(text='Take Photo',size_hint=(.245,.245),pos_hint={'x':.726,'y':.3})
		self.button_show_users = Button(text='Users',size_hint=(.245,.245),pos_hint={'x':.726,'y':.055})
		self.button_show_users.bind(on_press=self.action_btn_user)

		self.layout_to_show.add_widget(self.cam)
		self.layout_to_show.add_widget(self.button_take_photo)
		self.layout_to_show.add_widget(self.button_show_users)

		self.create_labels_text()
		self.create_buttons()

		return self.layout_to_show

	def create_buttons(self):
		
		self.btn_register = Button(text = "Cadastrar")
		self.btn_register.bind(on_press=self.action_btn_register)

		self.btn_apagar = Button(text = "Apagar")
		self.btn_apagar.bind(on_press=self.clear_all_text)

		self.layout1.add_widget(self.btn_register)
		self.layout1.add_widget(self.btn_apagar)

	def action_btn_user(self,instance):

		db = DBservice("sigma")
		labels = []

		l = db.select_all_user()
		layout = GridLayout(cols = 1)

		for row in l:
			s = str(row)
			label = Label(text=s)
			layout.add_widget(label)

		popup = Popup(title='Users',content=layout,auto_dismiss=True,size_hint=(.5,.6),pos=(.2,.2))
		popup.open()

	def action_btn_register(self,instance):
		
		db = DBservice("sigma")
		input_texts = []

		for index in range(len(self.texts_on_grid)):
			input_texts.append(self.texts_on_grid[index].text)

		t = tuple(input_texts)

		confirm = db.insert_user(t)

		if confirm:
			popup_sucsses = MenssegerPopup("Sucsses","All Done!")
			popup_sucsses.show_me()

		else:
			popup_error = MenssegerPopup("Error","Ok")
			popup_error.show_me()
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

			self.layout1.add_widget(label)
			self.layout1.add_widget(text)

class MyWidget(Widget):
	pass

if __name__ == "__main__":
	MyApp().run()