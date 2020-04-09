import sqlite3
import datetime

class Connection(object):
	"""docstring for Connection"""
	def __init__(self, data = []):
		data = data
	def conn(self):
		return sqlite3.connect('test.db')

	def create(self, name="test.db"):
		try:
			conn = self.conn()
			cursor = conn.cursor()
			conn.execute('''CREATE TABLE TAGUS_DB
				(qte INT NOT NULL,
				label TEXT NOT NULL,
				prix_u INT NOT NULL,
				prix_t INT NOT NULL,
				ref TEXT NOT NULL,
				date_instant timestamp);''')
			print("table already created")
			return True
		except sqlite3.Error as e:
			#raise e
			print("table already exists")
			return False

	def insert(self, row):
		conn = self.conn()
		cursor = conn.cursor()
		query = """INSERT INTO TAGUS_DB
			('qte', 'label', 'prix_u', 'prix_t', 'ref', 'date_instant')
			VALUES (?, ?, ?, ?, ?, ?);"""
		data_tuple = (row[0], row[1], row[2], row[3], row[4], row[5])
		cursor.execute(query, data_tuple)
		conn.commit()
		cursor.close()
		print(row[1], " added successfully")


	def select(self, ref = []):
		conn = self.conn()
		cursor = conn.cursor()
		query = """SELECT qte, label, prix_u, prix_t, ref, date_instant FROM TAGUS_DB
			WHERE ref = ?"""
		cursor.execute(query, (ref,))
		records = cursor.fetchall()
		for r in records:
			print("label : ", r[1])
			print("registring date : ", r[5])
		cursor.close()

	def select_all(self):
		conn = self.conn()
		cursor = conn.cursor()
		query = """SELECT qte, label, prix_u, prix_t, ref, date_instant FROM TAGUS_DB"""
		cursor.execute(query)
		records = cursor.fetchall()
		for r in records:
			print("label : ", r[1])
			print("registring date : ", r[5])
		cursor.close()

if __name__ == '__main__':
	c = Connection()
	t = c.create()
	c.insert([12, "Drone inspire 1", 600000, 12*600000, "ref-1", datetime.datetime.now()])
	c.insert([17, "Drone phantom", 60000, 17*60000, "ref-2", datetime.datetime.now()])
	c.insert([1, "Drone inspire 2", 900000, 1*600000, "ref-5", datetime.datetime.now()])
	c.insert([7, "Drone mavic pro", 1000000, 7*60000, "ref-22", datetime.datetime.now()])
	c.select(ref = "ref-1")
	c.select_all()
	print(t)