import kivy.uix.popup import Popup
import kivy.uix.button import Button

class MenssegerPopup(object):

	def __init__(self,title,content):
		self.btn = Button(text=content)
		self.popup = Popup(title=title,content=self.btn,auto_dismiss=False)
		self.btn.bind(on_press=self.popup.dismiss())

	def show_me(self):
		self.popup.open()