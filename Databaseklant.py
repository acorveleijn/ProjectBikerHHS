import sqlite3

import csv



def bikerdb():
    conn = sqlite3.connect('Biker.db') # Maak DB connectie. Als DB nog niet bestaat wordt deze gemaakt
    print(f'Database created succesfully')
    c = conn.cursor() # Maak de tabel klant als deze nog niet bestaat
    c.execute('''CREATE TABLE IF NOT EXISTS klant

                (naam text (30) NOT NULL,

                adres varchar (30) NOT NULL,

                postcode varchar (10) NOT NULL,

                woonplaats text (20) NOT NULL,

                land text (20) NOT NULL)

                ; ''')
    print('table created successfully')
    conn.commit()
    conn.close()

    conn = sqlite3.connect('Biker.db')
    c = conn.cursor()
    g_file = open('Klanten.csv')
    row = csv.reader(g_file)
    print('csv gelezen')
    c.executemany("INSERT INTO klant VALUES(?,?,?,?,?)", row)
    c.execute("SELECT * FROM klant")
    records = c.fetchall()
    print(c.fetchall())
    conn.commit()
    print('record added successfully')
    conn.close()