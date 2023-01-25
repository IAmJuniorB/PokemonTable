import sqlite3
from PokemonDict import pokemon
from PokemonTableClass import PokemonClass

# create/connect to database
conn = sqlite3.connect('pokemontable.db')
c = conn.cursor()

#create a table, Uncomment after creating
#conn.execute("""CREATE TABLE pokemon (
#             ID INTEGER PRIMARY KEY AUTOINCREMENT,
#             NAME TEXT NOT NULL,
#             TYPE TEXT NOT NULL
#             );""")

poke_1 = PokemonClass(153, "Joe", "Super Sayain")
for key, value in poke_1():
    conn.execute("INSERT INTO pokemon (NAME, TYPE) VALUES (?, ?)", (value[0], value[1]))


conn = sqlite3.connect('pokemontable.db')
c = conn.cursor()

# Uncomment to add values in table
#for key, value in pokemon.items():
#    conn.execute("INSERT INTO pokemon (NAME, TYPE) VALUES (?, ?)", (value[0], value[1]))

# prints all data
c.execute("SELECT * from pokemon WHERE ID >= 140")
print(c.fetchall())

# commit changes and close connection
conn.commit()
conn.close()

