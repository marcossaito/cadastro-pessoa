import sqlite3
import os

class DBservice(object):

	def __init__(self,string):

		if os.path.isfile(string + ".db"):
			self.conn = sqlite3.connect(string + ".db")
			self.dbname = string
		else:
			self.conn = sqlite3.connect("appdb.db")
			self.c = conn.cursor()
			self.dbname = "appdb"

	def create_tables(self):
		
		if os.path.isfile(self.dbname+".db")
			self.c.execute(''' CREATE TABLE user (id INTEGER AUTOINCREMENT, name text, cpf text, data_nascimento date)''')
			self.conn.commit()

		else:
			return False

		return True

	def insert_user(self,nome,cpf,data_nascimento):
		
		if os.path.isfile(self.dbname+".db"):
			self.c.execute(''' INSERT INTO user VALUES (NULL,?,?,?)''',(nome,cpf,data_nascimento))
			self.conn.commit()

		else:
			return False

		return True