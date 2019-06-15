from sqlite3 import *

konekcija = connect("kuharicabaza.db")

c = konekcija.cursor()

c.execute('CREATE TABLE IF NOT EXISTS recepti (naziv_recepta TEXT, recept TEXT)')

konekcija.close()
