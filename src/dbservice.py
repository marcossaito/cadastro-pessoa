import sqlite3
import os

#os.path.dirname(__file__)

class DBservice(object):

	LOCAL = os.path.dirname(os.path.abspath(__file__))

	def __init__(self,string):

		if not ( os.path.isfile("{0}/{1}.db".format(self.LOCAL,string)) ):
			self.conn = sqlite3.connect(string + ".db")
			self.c = self.conn.cursor()
			self.c.execute(''' CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cpf text, data_nascimento date)''')
	
			self.conn.commit()
			self.dbname = string
		
		elif os.path.isfile( "{0}/{1}.db".format(self.LOCAL,string) ):
			self.conn = sqlite3.connect(string + ".db")
			self.c = self.conn.cursor()
			self.dbname = string

		elif os.path.isfile( "{0}/appdb.db".format(self.LOCAL) ):
			self.conn = sqlite3.connect("appdb.db")
			self.c = self.conn.cursor()
			self.dbname = "appdb"

		else:
			self.conn = sqlite3.connect("appdb.db")
			self.c = self.conn.cursor()
			self.c.execute(''' CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cpf text, data_nascimento date)''')
	
			conn.commit()
			self.dbname = "appdb"

	def create_tables(self):
		
		if os.path.isfile( "{0}/{1}.db".format(self.LOCAL,self.dbname) ):
			self.c.execute(''' CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cpf text, data_nascimento date)''')
			self.conn.commit()

		else:
			return False

		return True

	def insert_user(self,insert_tuple):
		
		if insert_tuple == ('','',''):
			return False

		if os.path.isfile( "{0}/{1}.db".format(self.LOCAL,self.dbname) ):
			self.c.execute('''INSERT INTO user VALUES (NULL,?,?,?)''',insert_tuple)
			self.conn.commit()

		else:
			return False

		return True

	def select_all_user(self):

		return self.c.execute('''SELECT * FROM user''')

def create_default_db():
	conn = sqlite3.connect( "{0}/{1}.db".format(self.LOCAL,"appdb") )
	c = conn.cursor()

	c.execute(''' CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, cpf text, data_nascimento date)''')
	
	conn.commit()
	conn.close()

	print "All Done!"

if __name__ == "__main__":
	create_default_db()

