import sqlite3
from sqlite3 import Error
import datetime

class Connexion(object):
	"""docstring for Connexion"""
	def __init__(self, data = []):
		self.data = data

	def create_connection(self):
		"""
		Create a database connection to the SQLite daabase
		specified by db_file
		:param filename: database file
		:return: Connection object or none
		"""
		conn = None
		try:
			conn = sqlite3.connect("tagus.db")
			return conn
		except Error as e:
			print(e)
		return conn

	def create_table(self):
		"""
		create a table from the table sql statement
		:param conn: Connection object
		:param sql: a CREATE TABLE statement
		:return:
		"""
		sql_produits = """CREATE TABLE IF NOT EXISTS produits (
										id integer PRIMARY KEY AUTOINCREMENT,
										label text NOT NULL,
										prix integer NOT NULL,
										fabriquant text
										);"""

		sql_solds = """CREATE TABLE IF NOT EXISTS solds (
											id integer PRIMARY KEY AUTOINCREMENT,
											qte integer NOT NULL,
											produit_id integer NOT NULL,
											cur_date timestamp,
											FOREIGN KEY (produit_id) REFERENCES produits (id)
											);"""

		sql_employes = """CREATE TABLE IF NOT EXISTS employes (
											id integer PRIMARY KEY AUTOINCREMENT,
											nom integer NOT NULL,
											role text NOT NULL,
											cni integer NOT NULL,
											tel text NOT NULL,
											mail text NOT NULL
											);"""
		
		sql_depenses = """CREATE TABLE IF NOT EXISTS depenses (
											id integer PRIMARY KEY AUTOINCREMENT,
											label_produit text NOT NULL,
											prix integer NOT NULL,
											quantite integer NOT NULL,
											employe_id integer NOT NULL,
											cur_date timestamp,
											FOREIGN KEY (employe_id) REFERENCES employes (id)
											);"""

		sql_mouvements = """CREATE TABLE IF NOT EXISTS mouvements (
											id integer PRIMARY KEY AUTOINCREMENT,
											employe_id integer NOT NULL,
											motif text NOT NULL,
											FOREIGN KEY (employe_id) REFERENCES employes (id)
											);"""

		sql_departs = """CREATE TABLE IF NOT EXISTS departs (
											id integer PRIMARY KEY AUTOINCREMENT,
											mouvement_id integer NOT NULL,
											depart timestamp,
											FOREIGN KEY (mouvement_id) REFERENCES mouvements (id)
											);"""

		sql_arrivees = """CREATE TABLE IF NOT EXISTS arrivees (
											id integer PRIMARY KEY AUTOINCREMENT,
											depart_id integer NOT NULL,
											arrivee timestamp,
											FOREIGN KEY (depart_id) REFERENCES departs (id)
											);"""

		try:
			conn = self.create_connection()
			c = conn.cursor()
			c.execute(sql_produits)
			c.execute(sql_solds)
			c.execute(sql_employes)
			c.execute(sql_departs)
			c.execute(sql_mouvements)
			c.execute(sql_depenses)
			c.execute(sql_arrivees)
			conn.commit()
			c.close()
			print("Created !")
		except Error as e:
			print(e)

	def create_produit(self, produit):
		"""
		Crete a new produit into the produit table
		:param conn:
		:param produit:
		:return: produit_id
		"""
		sql = """INSERT INTO produits(label,prix,fabriquant)
				VALUES(?,?,?)"""
		conn = self.create_connection()
		cur = conn.cursor()
		cur.execute(sql, produit)
		conn.commit()
		cur.close()
		return cur.lastrowid

	def create_sold(self, sold):
		"""
		Crete a new sold into the sold table
		:param conn:
		:param sold:
		:return: produit_id
		"""
		sql = """INSERT INTO solds(qte,produit_id,cur_date)
				VALUES(?,?,?)"""
		conn = self.create_connection()
		cur = conn.cursor()
		cur.execute(sql, sold)
		conn.commit()
		cur.close()
		return cur.lastrowid

	def select_product(self):
		conn = self.create_connection()
		cursor = conn.cursor()
		query = """SELECT label, prix, fabriquant FROM produits"""
		cursor.execute(query)
		records = cursor.fetchall()
		l = []
		for r in records:
			l.append({"label":r[0], "prix":r[1], "fabriquant":r[2]})
		return l

if __name__ == '__main__':
	d = "tagus.db"
	t = Connexion()
	t.create_table()

	produit = ("Drone DJI phantom 4", 500000, "DJI")
	produit1 = ("Drone DJI Mavic pro 2", 800000, "DJI")
	produit2 = ("Drone DJI Inspire 1", 700000, "DJI")

	sold = (2, 2, datetime.datetime.now())
	sold1 = (1, 1, datetime.datetime.now())
	sold2 = (5, 0, datetime.datetime.now())
	sold3 = (20, 1, datetime.datetime.now())

	i = t.create_produit(produit)
	print(i)
	t.create_produit(produit1)
	t.create_produit(produit2)

	t.create_sold(sold)
	t.create_sold(sold1)
	t.create_sold(sold2)
	t.create_sold(sold3)