import sqlite3
import os

class DBservice(object):

	def __init__(self,string):

		if not (os.path.isfile(string + ".db")):
			self.conn = sqlite3.connect(string + ".db")
			self.c = self.conn.cursor()
			self.c.execute(''' CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cpf text, data_nascimento date)''')
	
			self.conn.commit()
			self.dbname = string
		
		elif os.path.isfile(string + ".db"):
			self.conn = sqlite3.connect(string + ".db")
			self.c = self.conn.cursor()
			self.dbname = string

		elif os.path.isfile("appdb.db"):
			self.conn = sqlite3.connect(string + ".db")
			self.c = self.conn.cursor()
			self.dbname = "appdb"

		else:
			self.conn = sqlite3.connect("appdb.db")
			self.c = self.conn.cursor()
			self.c.execute(''' CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cpf text, data_nascimento date)''')
	
			conn.commit()
			self.dbname = "appdb"

	def create_tables(self):
		
		if os.path.isfile(self.dbname+".db"):
			self.c.execute(''' CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cpf text, data_nascimento date)''')
			self.conn.commit()

		else:
			return False

		return True

	def insert_user(self,insert_tuple):
		
		if os.path.isfile(self.dbname+".db"):
			self.c.execute('''INSERT INTO user VALUES (NULL,?,?,?)''',insert_tuple)
			self.conn.commit()

		else:
			return False

		return True

def create_default_db():
	conn = sqlite3.connect("appdb.db")
	c = conn.cursor()

	c.execute(''' CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cpf text, data_nascimento date)''')
	
	conn.commit()
	conn.close()

	print "All Done!"

if __name__ == "__main__":
	create_default_db()

