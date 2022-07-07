import tkinter as tk
from tkinter import *
from tkinter import ttk
import csv
from nieuweklant import Klant
import sqlite3
# feedback:Klantgui: Maak een apart bestand met daarin de Class definitie voor het object.(nieuweklant.py gemaakt nav
# klant.py(ISBR))


from Databaseklant import bikerdb


def main():
    root = Tk()
    root.resizable(False, False)
    root.title('Biker')
    root.configure(background='#255')

    notebook = ttk.Notebook(root)
    notebook.pack(pady=10, expand=True)
    frame1 = ttk.Frame(notebook, width=400, height=280)
    frame2 = ttk.Frame(notebook, height=280, width=400)

    frame1.pack(fill='both', expand=True)
    frame2.pack(fill='both', expand=True)

    notebook.add(frame1, text='hoofdprogramma')
    notebook.add(frame2, text='klantenlijst')

    text_edit = tk.Text(frame2)
    text_edit.grid(row=1, column=0, columnspan=2)

    label2 = ttk.Label(frame2, text='klantenlijst bestaat uit naam,adres,postcode,woonplaats en land', font=('corbel', 10))
    label2.grid(column=0, row=0, columnspan=2)

    label3 = ttk.Label(frame1, text="Biker", font=('corbel', 8))
    label3.pack(side=TOP)

    style = ttk.Style()
    style.configure(frame1, background='#255')

    # feedback:De hoofdpagina is nog wat kaal.( foto logo Biker toegevoegd)
    logo = PhotoImage(file='Bikerlogo.gif')
    label1 = ttk.Label(frame1)
    label1.config(image=logo)
    label1.pack(side=tk.LEFT)
    label1.img = logo
    label1.config(image=label1.img, compound=LEFT)
    smal_logo = logo.subsample(2, 2)
    label1.config(image=smal_logo)

    klanten1 = Klant()
    klanten1.naam = 'Klaas Claassen'
    klanten1.adres = 'Klaassstraat 14'
    klanten1.postcode = '2552KC'
    klanten1.woonplaats = 'Den Haag'
    klanten1.land = 'Nederland'
    klanten2 = Klant()
    klanten2.naam = 'Piet Pietersen '
    klanten2.adres = ' Pietsersepad 13 '
    klanten2.postcode = ' 2552PP '
    klanten2.woonplaats = ' Den Haag '
    klanten2.land = 'Nederland'
    klantje = [klanten1, klanten2]
    # Feedback:Bij de klantenlijst wordt alles aan elkaar geplakt.(' ' toegevoegd)
    for k in klantje:
        gegevens = k.naam + ' ' + k.adres + ' ' + k.postcode + ' ' + k.woonplaats + ' ' + k.land
        text_edit.insert(END, gegevens)
        text_edit.insert(END, '\n')

    # Een functie maakt die gegevens van een object uit een CSV file leest en in een List plaatst.
    def test_function():
        text_edit.config(state='normal')
        with open('Klanten.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for rows in csv_reader:
                content = rows[0] + rows[1] + rows[2] + rows[3] + rows[4] + '\n'
                text_edit.insert(END, content)
        # De GUI wordt aangepast met een Button op de Hoofdpagina die als je op Button clickt de lijst met objecten uit het CSV inleest en  in de Text widget plaatst.
    button_open = ttk.Button(frame1, text='CSV', width=20, command=test_function)
    button_open.pack(side=TOP)

    def delete():
        text_edit.config(state='normal')
        text_edit.delete('1.0', END)

    button3 = ttk.Button(frame2, text='textveld legen', command=delete)
    button3.grid(column=3, row=3)
    text_edit.config(state='disabled')

    def open_klant():      # Database maken als deze nog niet bestaat en tabel student vullen.
        bikerdb()
        conn = sqlite3.connect('Biker.db')
        print("database open")             # Connectie met de DB maken om records uit tabel te lezen
        c = conn.cursor()
        klantjes = [('Klaas Claassen', 'Klaassstraat 14', '2552KC', 'Den Haag', 'Nederland'),
                ('Piet Pietersen', 'Pietsersepad 13', '2552PP', 'Den Haag', 'Nederland'), ]
        c.executemany('''INSERT INTO klant VALUES(?,?,?,?,?)''', klantjes)
        c.execute('''SELECT * FROM klant''')
        bestandje = c.fetchall()
        print('records toegevoegd')
        conn.commit()
        text_edit.config(state='normal')
        for s in bestandje:
            content = s[0] + s[1] + s[2] + s[3] + s[4]
            text_edit.insert(END, content)       # Records in table toevoegen aan text widget
            text_edit.insert(END, '\n')

    button_open2 = ttk.Button(frame1, text='Geef database', width=20, command=open_klant)
    button_open2.pack(side=TOP)
    text_edit.config(state='disabled')
    root.mainloop()


if __name__ == '__main__':
    main()

# Angelique Corveleijn
