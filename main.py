from tkinter import *
from tkinter import ttk
import json

database_name = "data.json"

database = {
    "Имя": "",
    "Фамилия": "",
    "Отчество": "",
    "Кол-во проживающих": "",
    "Площадь": "",
    "Адрес": "",
    "Показания счетчика": "",
    "Оплата за все ком. услуги": "",
    "Период Оплаты": ""

}

database_array = {
    "Имя": [],
    "Фамилия": [],
    "Отчество": [],
    "Кол-во проживающих": [],
    "Площадь": [],
    "Адрес": [],
    "Показания счетчика": [],
    "Оплата за все ком. услуги": [],
    "Период Оплаты": []

}

def write_to_database():
    
    global database_name
    global database
    global database_array
    print(database)
    key_list =  ["Имя","Фамилия","Отчество", "Кол-во проживающих","Площадь","Адрес", "Показания счетчика","Оплата за все ком. услуги", "Период Оплаты"]
    try:
        for i in range(0, 9):
            buffer = database[key_list[i]]
            print(buffer)
            database_array[key_list[i]].append(buffer)
            print(database_array[key_list[i]])
    except KeyError:
        pass
    print(database_array[key_list[i]])
    with open(database_name, 'w') as w:
        json.dump(database_array, w)


def read_from_database():
    global database_array
    with open(database_name, 'r') as r:
        database_array = json.load(r)

try:
    read_from_database()
    print(database_array)
except Exception:
    pass






win = Tk()
def show_table(find_indx=""):
    pass
    global win
    global database
    win2 = Tk()
    win2.title("TABLE")
    win2.resizable(False,False)
    keyses = database.keys()
    key_list =  ["Имя","Фамилия","Отчество", "Кол-во проживающих","Площадь","Адрес", "Показания счетчика","Оплата за все ком. услуги", "Период Оплаты"]
    print(key_list)
    table = ttk.Treeview(win2, columns=key_list)
    table.grid(row=0, column=0)
    for c in range(0, 9):
        table.heading(key_list[c], text=key_list[c])
    
    for j in range(0, len(database_array[key_list[0]])):        
        table.insert('' , 'end', values=(
            database_array[key_list[0]][j],
            database_array[key_list[1]][j],
            database_array[key_list[2]][j],
            database_array[key_list[3]][j],
            database_array[key_list[4]][j],
            database_array[key_list[5]][j],
            database_array[key_list[6]][j],
            database_array[key_list[7]][j],
            database_array[key_list[8]][j]
            ))

    win2.mainloop() 

win.title("DATA BASE")
win.resizable(False, False)

Label(win, text="Имя").grid(row=0, column=0)
Label(win, text="Фамилия").grid(row=1, column=0)
Label(win, text="Отчество").grid(row=2, column=0)
Label(win, text="Кол-во проживающих").grid(row=3, column=0)
Label(win, text="Площадь").grid(row=4, column=0)
Label(win, text="Адрес").grid(row=5, column=0)
Label(win, text="Показания счетчика").grid(row=6, column=0)
Label(win, text="Оплата за все ком. услуги").grid(row=7, column=0)
Label(win, text="Период оплаты").grid(row=8, column=0)

input1 = []

input1.append(Entry(win))
input1.append(Entry(win))
input1.append(Entry(win))
input1.append(Entry(win))
input1.append(Entry(win))
input1.append(Entry(win))
input1.append(Entry(win))
input1.append(Entry(win))
input1.append(Entry(win))

for i in range(0, 9):
    input1[i].grid(row=i, column=1)


find_entry = Entry(win).grid(row=9, column=1)

def button_wriite():
    global input1
    global database

    keys = ["Имя","Фамилия","Отчество", "Кол-во проживающих","Площадь","Адрес", "Показания счетчика","Оплата за все ком. услуги", "Период Оплаты"]
    
    buffer = ""
    
    for i in range(0, 9):
        buffer = input1[i].get()
        if buffer != "":
            print(buffer)
            database[keys[i]] = buffer  
        else:
            database[keys[i]] = "NONE"  
    write_to_database()
    
    print(database)
    print(database_array)


Button(win, text="Find").grid(row=9, column=0)
Button(win, text="Write to database", command=button_wriite).grid(row=10, column=0)
Button(win, text="Show Table", command=show_table).grid(row=10, column=1)

win.mainloop()