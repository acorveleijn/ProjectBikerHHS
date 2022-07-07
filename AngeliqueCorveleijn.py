
# Het Pythonprogramma voor het beroepsproduct van ISDQ moet minimaal aan de volgende criteria voldoen:
# Het Pythonprogramma is een command line programma. ## er staat bij alle grafieken een print opdracht ##
# Het programma heeft een menu met twee keuzemogelijkheden. ## vanaf line 227 5 buttons voor 5 keuzemogelijkheden##
# Het programma leest een of meer datasets in (CSV exports van de Game Paradise database). ## 2 csv gebruikt ##
# Het programma maakt met MatPlotLib twee verschillende diagrammen gebaseerd op de ingelezen data set(s).
# Menu-optie laat diagram 1 zien en menu-optie 2 laat diagram 2 zien. ## vanaf line 227 5 buttons voor 5 keuzes##
# Het progamma laat ook uitleg zien over de twee diagrammen (uitleg over wat er te zien is in de twee diagrammen).
                                                ## Bij elke grafiek is een toplevel met informatie over de grafiek##
import tkinter as tk
import tkinter as ttk
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

root = Tk()
root.resizable(False, False)
root.title('Gameparadise')
root.configure()
root.iconphoto(True, tk.PhotoImage(file='logo.png'))

frame1 = ttk.Frame(root, width=300, height=280, background='#255')
frame1.grid()

text_edit = tk.Text(frame1, width=70, height=30, font=('corbel', 12))
text_edit.grid(row=1, column=0, columnspan=3, rowspan=4)
text_edit.config(state='disabled')

label1 = Label(frame1, text='Gameparadise', fg='white', background='#255')
label2 = Label(frame1, text='Groep 8 Angelique Corveleijn 21159246', fg='white', background='#255')
label3 = Label(text_edit, text='Grafieken met Matplotlib en Numpy')


def show():
    artikelcsv = pd.read_csv('artikel.csv', encoding="ISO-8859-1", sep=',')
    open5()
    huurprijs = artikelcsv['PRIJS_PER_D']
    np_huurprijs = np.array([huurprijs])
    print(huurprijs)
    print(np_huurprijs)

    max_huurprijs = np.max(huurprijs)
    min_huurprijs = np.min(huurprijs)
    gem_huurprijs = np.mean(huurprijs)
    print(max_huurprijs)
    print(min_huurprijs)
    print(gem_huurprijs)
    ## De prijzen zijn handmatig cecontroleerd. Dit heb ik gecontroleerd in de database.\n##
    ## Printscreen in document bij onderdeel Python.##

    font2 = {'family': 'serif', 'color': 'blue', 'size': 15}

    ##figuur1##
    x1 = np.array(['max_prijs', 'min_prijs', 'gem_prijs'])
    y = np.array([17, 2, 4.8466])
    plt.title('Huurprijzen', fontdict=font2, loc='right')
    plt.bar(x1, y)
    plt.show()


def figure_1():   ##Koopprijzen grafiek maken##
    artikelcsv = pd.read_csv('artikel.csv', encoding="ISO-8859-1", sep=',')
    open1()
    koopprijs = artikelcsv['PRIJS']
    np_koopprijs = np.array([koopprijs])
    print(np_koopprijs)
    print(koopprijs)
    print(type(koopprijs))
    max_koopprijs = np.max(koopprijs)
    min_koopprijs = np.min(koopprijs)
    gem_koopprijs = np.mean(koopprijs)

    print(max_koopprijs)
    print(min_koopprijs)
    print(gem_koopprijs)
    ## De prijzen zijn handmatig cecontroleerd. Dit heb ik gecontroleerd in de database.\n##
    ## Printscreen in document bij onderdeel Python.##

    font2 = {'family': 'serif', 'color': 'blue', 'size': 15}

    ##figuur1##
    x1 = np.array(['max_prijs', 'min_prijs', 'gem_prijs'])
    y = np.array([450, 26, 108.34666666666666])
    plt.title('Koopprijzen', fontdict=font2, loc='right')
    plt.bar(x1, y)
    plt.show()
    

def figure_2():   ##vergelijking  grafiek maken##
    ##figuur2##
    artikelcsv = pd.read_csv('artikel.csv', encoding="ISO-8859-1", sep=',')
    open2()
    huurprijs = artikelcsv['PRIJS_PER_D']
    koopprijs = artikelcsv['PRIJS']
    np_huurprijs = np.array([huurprijs])
    print(huurprijs)
    print(np_huurprijs)
    max_huurprijs = np.max(huurprijs)
    min_huurprijs = np.min(huurprijs)
    print(max_huurprijs)
    print(min_huurprijs)
    ## De prijzen zijn handmatig cecontroleerd. Dit heb ik gecontroleerd in de database.\n##
    ## Printscreen in document bij onderdeel Python.##

    y = np.array(koopprijs)
    y2 = np.array(huurprijs)

    font1 = {'color': 'blue', 'size': 10}
    font2 = {'family': 'serif', 'color': 'blue', 'size': 15}

    plt.title('Vergelijking huurprijs/koopprijs', fontdict=font2, loc='right')
    plt.xlabel("Console/Spel", fontdict=font1)
    plt.ylabel("Huurprijs", fontdict=font1)
    plt.plot(y2, marker='p', ls=':')
    plt.plot(y, marker='+', c='k')
    plt.grid(axis='y')
    plt.show()


def figure_3():   ## Gameparadise Koopprijzen en huurprijzen grafiek Verhouding##
    ##figuur 3##
    artikelcsv = pd.read_csv('artikel.csv', encoding="ISO-8859-1", sep=',')  ## csv-bestand uitlezen ##
    open3()
    ##plot1##
    huurprijs = artikelcsv['PRIJS_PER_D']
    koopprijs = artikelcsv['PRIJS']
    print(huurprijs)
    print(koopprijs)
    font1 = {'color': 'blue', 'size': 10}

    y = np.array(koopprijs)
    y2 = np.array(huurprijs)
        ## de reeksen zijn gecontroleerd op hoogste en laagste prijs aan de hand van query's##
    ## de printscreens zijn opgenomen in het beroepsproduct, hoofdstuk Python##
    plt.subplot(1, 2, 1)
    plt.plot(y)
    plt.title('koopprijs', font1)
    ##plot2##
    plt.subplot(1, 2, 2)
    plt.plot(y2)
    plt.title('huurprijs', font1)
    plt.suptitle('Gameparadise')
    plt.show()


def figuur4():  ## Grafiek merk van Klant##
    open4()
    df = pd.read_csv('klant.csv', encoding="ISO-8859-1", sep=',')    ##csv-bestand uitlezen##
    postcode = df['MERK_EIGEN_CONSOLE']
    print(postcode)
    plt.hist(postcode)
    plt.xlim()
    plt.ylim(0, 50)
    font1 = {'color': 'blue', 'size': 10}
    font2 = {'family': 'serif', 'color': 'blue', 'size': 15}
    plt.ylabel("Aantal", fontdict=font1)
    plt.title('Merk consoles van de klant', fontdict=font2, loc='right')
    plt.show()
    ## De prijzen zijn handmatig cecontroleerd. Dit heb ik gecontroleerd in de database.\n##
    ## Printscreen in document bij onderdeel Python.##


def open1():   ## Informatiewindow Koopprijzen##
    top1 = Toplevel()
    top1.title('Informatie Koopprijzen')
    label8 = ttk.Label(top1, text='Deze bar grafiek laat de duurste, de goedkoopste en de\n '
                                  'gemiddelde prijs zien als je een artikel koopt bij Gamepardise. De prijzen\n'
                                  'variëren nogal omdat er bij het maken van deze grafiek geen onderscheidt\n '
                                  'is gemaakt tussen consoles en spellen, die onderling nogal van prijs verschillen.\n').pack()
    button7 = ttk.Button(top1, text='sluit info', command=top1.destroy).pack()


def open2():   ## Informatiewindow Vergelijking Huur/Koopprijzen##
    top2 = Toplevel()
    top2.title('Informatie Vergelijking Huur/Koopprijzen')
    label4 = ttk.Label(top2, text='In deze grafiek kan je 2 lijnen zien die de prijzen weergeven van de\n'
                                  'artikelen die Gameparadise verkoopt. De zwarte lijn zijn de koopprijzen.\n'
                                  'De blauwe lijn laat de huurprijzen zien.\n ').pack()
    button8 = ttk.Button(top2, text='sluit info', command=top2.destroy).pack()


def open3():   ## Informatiewindow Prijsverhouding Huur/Koop##
    top3 = Toplevel()
    top3.title('Informatie Prijsverhouding Huur/Koop')
    label5 = ttk.Label(top3, text=' In deze afbeelding is er gekozen voor 2 identieke grafieken.\n'
                                  ' Dit is om de prijsverhouding aan te duiden. Je kan uit\n'
                                  ' grafieken opmaken dat de prijsverhouding gelijk is. De \n'
                                  ' duurdere koopartikelen zijn dus niet duurder om te huren\n'
                                  ' dan een "goedkoop" spelletje.\n ').pack()
    button9 = ttk.Button(top3, text='sluit info', command=top3.destroy).pack()


def open4():    ## Informatie window Merk consoles van de klant##
    top4 = Toplevel()
    top4.title('Informatie Merk consoles van de klant')
    label6 = ttk.Label(top4, text='Met deze grafiek kan je het aantal en de merken van de consoles zien\n'
                                  'die bekend zijn van de klanten van Gameparadise.').pack()
    button10 = ttk.Button(top4, text='sluit info', command=top4.destroy).pack()


def open5():    ##Informatiewindow grafiek Huurprijzen##
    top5 = Toplevel()
    top5.title('Informatie grafiek Huurprijzen')
    label7 = ttk.Label(top5, text='Deze bar grafiek laat de duurste, de goedkoopste en de\n '
                                  'gemiddelde prijs zien als je een artikel huurt bij Gamepardise. De prijzen\n'
                                  'variëren nogal omdat er bij het maken van deze grafiek geen onderscheidt\n '
                                  'is gemaakt tussen consoles en spellen, die onderling nogal van prijs verschillen.\n').pack()
    button8 = ttk.Button(top5, text='sluit info', command=top5.destroy).pack()


text_edit.config(state='normal')
global logo
logo = PhotoImage(file='logo8.png')
label3 = ttk.Label(text_edit)
label3.config(image=logo)
label3.pack(side=tk.LEFT)
label3.img = logo
label3.config(image=label3.img, compound=LEFT)
klein_logo = logo.subsample(2, 2)
label3.config(image=klein_logo)
label3.config(text='Grafieken met Matplotlib en Numpy', background='white', font=('corbel', 12), foreground='#255')
label3.config(compound='bottom')
text_edit.config(state='disabled')


button2 = tk.Button(frame1, text='Koopprijzen   ', width=20, height=2, fg='white', background='#255', command=figure_1)
button3 = tk.Button(frame1, text='Huurprijzen  ', width=20, height=2, fg='white', background='#255', command=show)
button4 = tk.Button(frame1, text='Vergelijking  ', width=20, height=2, fg='white', background='#255', command=figure_2)
button5 = tk.Button(frame1, text='Verhouding ', width=20, height=2, fg='white', background='#255', command=figure_3)
button6 = tk.Button(frame1, text='Merk van klant', width=20, height=2, fg='white', bg='#255', command=figuur4)


button2.grid(row=1, column=4, columnspan=2)
button3.grid(row=2, column=4, columnspan=2)
button4.grid(row=3, column=4, columnspan=2)
button5.grid(row=4, column=4, columnspan=2)
button6.grid(row=5, column=4, columnspan=2)
label1.grid(row=5, column=0)
label2.grid(row=5, column=1)


root.mainloop()
