#generator protokołów v1.0 13_09_2022
from tkinter import *
import sqlite3
from tkinter import filedialog
from tkcalendar import DateEntry

root = Tk()

root.title("Edytor protokołów odbiorowych")


# tworzy nowy projekt (plik bazy danych "*.db")
def utworz_bd():
    global nazwa_projektu

    nazwa_projektu = n_projektu.get() + ".db"
    connection = sqlite3.connect(nazwa_projektu)
    cursor = connection.cursor()

    cursor.execute("create table dane_inwest (n_inwest text, lok_inwest text, n_inwestor text, lok_inwestor text, wykon text, lok_wykon text)")

    pocz_dane_inwest = [
        ("", "", "", "", "", ""),
    ]

    cursor.executemany("insert into dane_inwest values (?, ?, ?, ?, ?, ?)", pocz_dane_inwest)

    cursor.execute("create table dane (nazwa_instaalcji text, min_dim integer, max_dim integer, lenght integer, material text, others text, date text, ps integer, pl integer)")

    pocz_dane = [
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1),
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1),
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1),
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1),
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1),
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1),
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1),
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1),
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1),
        ("", 0, 0, 0, "", "", "09.10.2022", 1, 1)
    ]

    cursor.executemany("insert into dane values (?, ?, ?, ?, ?, ?, ?, ?, ?)", pocz_dane)


    connection.commit()
    connection.close()

    silnik()

# okno dialogowe z zapytaniem o nazwę nowego projektu
def otworz_nowy():
    global n_projektu
    top_1 = Toplevel()

    Label(top_1, text="Podaj nazwę projektu:").grid(row=0, column=0, padx=1, pady=1)
    n_projektu = Entry(top_1, width=40)
    n_projektu.grid(row=0, column=1, padx=1, pady=1)
    # nazwa_projektu = n_projektu.get()
    # print(nazwa_projektu)
    Button(top_1, text="Utwórz projekt", command=utworz_bd).grid(row=1, column=0, columnspan=2)
    Button(top_1, text="Zamknij", command=top_1.quit).grid(row=2, column=0, columnspan=2)

    top_1.mainloop()

# otwiera istniejący projekt
def otworz_isniejacy():
    global nazwa_projektu
    top_2 = Toplevel()

    top_2.filename = filedialog.askopenfilename(title="Wybierz plik", filetypes=(("Pliki baz danych", "*.db"),("wszystkie pliki", "*.*")))
    nazwa_projektu = top_2.filename
    silnik()

    top_2.mainloop()

# dodaje dane do istniejącej bazy danych
def uaktualnij_dane():
    conn = sqlite3.connect(nazwa_projektu)
    c = conn.cursor()

    dane_inwest = (n_inwest.get(), lok_inwest.get(), n_inwestor.get(), lok_inwestor.get(), n_wyk.get(), lok_wyk.get(), 1)
    c.execute(
        "UPDATE dane_inwest SET n_inwest = ?, lok_inwest = ?, n_inwestor = ?, lok_inwestor = ?, wykon = ?, lok_wykon = ? WHERE rowid = ?", dane_inwest)

    dane_inst_1 = (wiersz1.inst_nr.get(), wiersz1.min_dim_nr.get(), wiersz1.max_dim_nr.get(), wiersz1.len_nr.get(), wiersz1.mat_nr.get(), wiersz1.inne_nr.get(), wiersz1.cal.get(), wiersz1.ps_nr.get(), wiersz1.pl_nr.get(), 1)
    c.execute("UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?", dane_inst_1)
    dane_inst_2 = (wiersz2.inst_nr.get(), wiersz2.min_dim_nr.get(), wiersz2.max_dim_nr.get(), wiersz2.len_nr.get(),
                   wiersz2.mat_nr.get(), wiersz2.inne_nr.get(), wiersz2.cal.get(), wiersz2.ps_nr.get(),
                   wiersz2.pl_nr.get(), 2)
    c.execute(
        "UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?",
        dane_inst_2)
    dane_inst_3 = (wiersz3.inst_nr.get(), wiersz3.min_dim_nr.get(), wiersz3.max_dim_nr.get(), wiersz3.len_nr.get(),
                   wiersz3.mat_nr.get(), wiersz3.inne_nr.get(), wiersz3.cal.get(), wiersz3.ps_nr.get(),
                   wiersz3.pl_nr.get(), 3)
    c.execute(
        "UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?",
        dane_inst_3)
    dane_inst_4 = (wiersz4.inst_nr.get(), wiersz4.min_dim_nr.get(), wiersz4.max_dim_nr.get(), wiersz4.len_nr.get(),
                   wiersz4.mat_nr.get(), wiersz4.inne_nr.get(), wiersz4.cal.get(), wiersz4.ps_nr.get(),
                   wiersz4.pl_nr.get(), 4)
    c.execute(
        "UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?",
        dane_inst_4)
    dane_inst_5 = (wiersz5.inst_nr.get(), wiersz5.min_dim_nr.get(), wiersz5.max_dim_nr.get(), wiersz5.len_nr.get(),
                   wiersz5.mat_nr.get(), wiersz5.inne_nr.get(), wiersz5.cal.get(), wiersz5.ps_nr.get(),
                   wiersz5.pl_nr.get(), 5)
    c.execute(
        "UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?",
        dane_inst_5)
    dane_inst_6 = (wiersz6.inst_nr.get(), wiersz6.min_dim_nr.get(), wiersz6.max_dim_nr.get(), wiersz6.len_nr.get(),
                   wiersz6.mat_nr.get(), wiersz6.inne_nr.get(), wiersz6.cal.get(), wiersz6.ps_nr.get(),
                   wiersz6.pl_nr.get(), 6)
    c.execute(
        "UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?",
        dane_inst_6)
    dane_inst_7 = (wiersz7.inst_nr.get(), wiersz7.min_dim_nr.get(), wiersz7.max_dim_nr.get(), wiersz7.len_nr.get(),
                   wiersz7.mat_nr.get(), wiersz7.inne_nr.get(), wiersz7.cal.get(), wiersz7.ps_nr.get(),
                   wiersz7.pl_nr.get(), 7)
    c.execute(
        "UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?",
        dane_inst_7)
    dane_inst_8 = (wiersz8.inst_nr.get(), wiersz8.min_dim_nr.get(), wiersz8.max_dim_nr.get(), wiersz8.len_nr.get(),
                   wiersz8.mat_nr.get(), wiersz8.inne_nr.get(), wiersz8.cal.get(), wiersz8.ps_nr.get(),
                   wiersz8.pl_nr.get(), 8)
    c.execute(
        "UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?",
        dane_inst_8)
    dane_inst_9 = (wiersz9.inst_nr.get(), wiersz9.min_dim_nr.get(), wiersz9.max_dim_nr.get(), wiersz9.len_nr.get(),
                   wiersz9.mat_nr.get(), wiersz9.inne_nr.get(), wiersz9.cal.get(), wiersz9.ps_nr.get(),
                   wiersz9.pl_nr.get(), 9)
    c.execute(
        "UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?",
        dane_inst_9)
    dane_inst_10 = (wiersz10.inst_nr.get(), wiersz10.min_dim_nr.get(), wiersz10.max_dim_nr.get(), wiersz10.len_nr.get(),
                   wiersz10.mat_nr.get(), wiersz10.inne_nr.get(), wiersz10.cal.get(), wiersz10.ps_nr.get(),
                   wiersz10.pl_nr.get(), 10)
    c.execute(
        "UPDATE dane SET nazwa_instaalcji = ?, min_dim = ?, max_dim = ?, lenght = ?, material = ?, others = ?, date = ?, ps = ?, pl = ? WHERE rowid = ?",
        dane_inst_10)


    conn.commit()
    conn.close()

# definicja klasy wiersza z danymi instalacji
class wiersz:
    def __init__(self, nazwa_projektu, row_nr, nr_instalacji):
        self.nazwa_projektu = nazwa_projektu
        self.row_nr = row_nr
        self.nr_instalacji = nr_instalacji

    def parametry_instalacji(self):
        conn = sqlite3.connect(self.nazwa_projektu)
        c = conn.cursor()
        c.execute("SELECT * FROM dane")
        items = c.fetchall()

        self.ps_nr = IntVar()
        self.pl_nr = IntVar()

        self.ps_nr.set(items[self.nr_instalacji][7])
        self.pl_nr.set(items[self.nr_instalacji][8])

        Checkbutton(top, text="Próba szczelności", variable=self.ps_nr).grid(row=self.row_nr, column=0, padx=1, pady=1)
        Checkbutton(top, text="Płukanie", variable=self.pl_nr).grid(row=self.row_nr, column=1, padx=1, pady=1)
        self.inst_nr = Entry(top, width=40)
        self.inst_nr.grid(row=self.row_nr, column=2, padx=1, pady=1)
        Label(top, text="zakres średnic:").grid(row=self.row_nr, column=3, padx=10, pady=1)
        self.min_dim_nr = Entry(top, width=5)
        self.min_dim_nr.grid(row=self.row_nr, column=4, padx=1, pady=1)
        Label(top, text="mm do:").grid(row=self.row_nr, column=5, padx=1, pady=1)
        self.max_dim_nr = Entry(top, width=5)
        self.max_dim_nr.grid(row=self.row_nr, column=6, padx=1, pady=1)
        Label(top, text="mm, Łączna długość wynosi:").grid(row=self.row_nr, column=7, padx=1, pady=1)
        self.len_nr = Entry(top, width=5)
        self.len_nr.grid(row=self.row_nr, column=8, padx=1, pady=1)
        Label(top, text="m").grid(row=self.row_nr, column=9, padx=1, pady=1)
        Label(top, text="Materiał:").grid(row=self.row_nr, column=10, padx=1, pady=1)
        self.mat_nr = Entry(top, width=15)
        self.mat_nr.grid(row=self.row_nr, column=11, padx=1, pady=1)
        Label(top, text="Inne:").grid(row=self.row_nr, column=12, padx=1, pady=1)
        self.inne_nr = Entry(top, width=45)
        self.inne_nr.grid(row=self.row_nr, column=13, padx=1, pady=1)
        Label(top, text="Data:").grid(row=self.row_nr, column=14, padx=1, pady=1)
        self.cal = DateEntry(top, selectmode = 'day')
        self.cal.grid(row=self.row_nr, column=15, padx=1, pady=1)

        self.inst_nr.insert(0, items[self.nr_instalacji][0])
        self.min_dim_nr.insert(0, items[self.nr_instalacji][1])
        self.max_dim_nr.insert(0, items[self.nr_instalacji][2])
        self.len_nr.insert(0, items[self.nr_instalacji][3])
        self.mat_nr.insert(0, items[self.nr_instalacji][4])
        self.inne_nr.insert(0, items[self.nr_instalacji][5])
        self.cal.set_date(items[self.nr_instalacji][6])

# tworzy główne okno dialogowe
def silnik():
    global top
    top = Toplevel()

    global nazwa_projektu, wiersz1, wiersz2, wiersz3, wiersz4, wiersz5, wiersz6, wiersz7, wiersz8, wiersz9, wiersz10, n_inwest, lok_inwest, n_inwestor, lok_inwestor, n_wyk, lok_wyk

    conn = sqlite3.connect(nazwa_projektu)
    c = conn.cursor()

    c.execute("SELECT * FROM dane_inwest")
    items_inwest = c.fetchall()

    c.execute("SELECT * FROM dane")
    items = c.fetchall()



    global inst_1, min_dim_1, max_dim_1, len_1, inst_2, min_dim_2, max_dim_2, len_2, inst_3, min_dim_3, max_dim_3, len_3

    #Dane projektu
    Label(top, text="Nazwa inwestycji:", anchor=W, width=18).grid(row=0, column=0, padx=10, pady=10)
    n_inwest = Entry(top, width=200)
    n_inwest.grid(row=0, column=1, padx=10, pady=10, columnspan=16)
    Label(top, text="Lokalizacja inwestycji:", anchor=W, width=18).grid(row=1, column=0, padx=10, pady=10)
    lok_inwest = Entry(top, width=200)
    lok_inwest.grid(row=1, column=1, padx=10, pady=10, columnspan=16)
    Label(top, text="Nazwa inwestora:", anchor=W, width=18).grid(row=2, column=0, padx=10, pady=10)
    n_inwestor = Entry(top, width=200)
    n_inwestor.grid(row=2, column=1, padx=10, pady=10, columnspan=16)
    Label(top, text="Adres inwestora:", anchor=W, width=18).grid(row=3, column=0, padx=10, pady=10)
    lok_inwestor = Entry(top, width=200)
    lok_inwestor.grid(row=3, column=1, padx=10, pady=10, columnspan=16)
    Label(top, text="Wykonawca:", anchor=W, width=18).grid(row=4, column=0, padx=10, pady=10)
    n_wyk = Entry(top, width=200)
    n_wyk.grid(row=4, column=1, padx=10, pady=10, columnspan=16)
    Label(top, text="Adres wykonawcy:", anchor=W, width=18).grid(row=5, column=0, padx=10, pady=10)
    lok_wyk = Entry(top, width=200)
    lok_wyk.grid(row=5, column=1, padx=10, pady=10, columnspan=16)

    n_inwest.insert(0, items_inwest[0][0])
    lok_inwest.insert(0, items_inwest[0][1])
    n_inwestor.insert(0, items_inwest[0][2])
    lok_inwestor.insert(0, items_inwest[0][3])
    n_wyk.insert(0, items_inwest[0][4])
    lok_wyk.insert(0, items_inwest[0][5])


    #Parametry 1 instalacji
    nr_instalacji = 0
    nr_wiersza = 7
    wiersz1 = wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz1.parametry_instalacji()

    #Parametry 2 instalacji
    nr_instalacji += 1
    nr_wiersza += 1
    wiersz2 = wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz2.parametry_instalacji()

    #Parametry 3 instalacji
    nr_instalacji += 1
    nr_wiersza += 1
    wiersz3 = wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz3.parametry_instalacji()

    #Parametry 4 instalacji
    nr_instalacji += 1
    nr_wiersza += 1
    wiersz4 = wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz4.parametry_instalacji()

    #Parametry 5 instalacji
    nr_instalacji += 1
    nr_wiersza += 1
    wiersz5 = wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz5.parametry_instalacji()


    #Parametry 6 instalacji
    nr_instalacji += 1
    nr_wiersza += 1
    wiersz6 = wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz6.parametry_instalacji()

    #Parametry 7 instalacji
    nr_instalacji += 1
    nr_wiersza += 1
    wiersz7 = wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz7.parametry_instalacji()

    #Parametry 8 instalacji
    nr_instalacji += 1
    nr_wiersza += 1
    wiersz8 = wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz8.parametry_instalacji()

    #Parametry 9 instalacji
    nr_instalacji += 1
    nr_wiersza += 1
    wiersz9= wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz9.parametry_instalacji()

    #Parametry 10 instalacji
    nr_instalacji += 1
    nr_wiersza += 1
    wiersz10 = wiersz(nazwa_projektu, nr_wiersza, nr_instalacji)
    wiersz10.parametry_instalacji()


    Button(top, text="Dodaj dane do generatora protokołów", command=uaktualnij_dane).grid(row=30, column=0, columnspan=8, ipadx=80)
    Button(top, text="Zamknij", command=top.quit).grid(row=30, column=10, columnspan=8, ipadx=80)

    items = c.fetchall()
    # print(items)

    top.mainloop()




Button(root, text="Otwórz istniejący zestaw protokołów", command=otworz_isniejacy).grid(row=0, column=0)
Button(root, text="Otwórz nowy zestaw protokołów", command=otworz_nowy).grid(row=1, column=0)
Button(root, text="Zamknij", command=root.quit).grid(row=2, column=0)

# Button(root, text="Dodaj dane do generatora protokołów", command=uaktualnij_dane).grid(row=3, column=0, columnspan=8, ipadx=80)

root.mainloop()

