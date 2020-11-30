__author__  = "José Eduardo Saroba Bieco"
__status__ = "Production"

from tkinter import *
import datetime

PATH = "RA.txt"

def add_RA():
    master = Tk()

    Label(master, text="RA").grid(row=0)
    Label(master, text="Horario").grid(row=1)

    now = datetime.datetime.now()
    defaultTime = StringVar(master, value=str(now.hour) + ":" + str(now.minute))

    e1 = Entry(master)
    e2 = Entry(master, textvariable=defaultTime)

    e1.grid(row=0, column=1)
    e1.focus()
    e2.grid(row=1, column=1)


    Button(master, text="Adicionar", command=lambda: add(e1.get(), e2.get(), master)).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text="Quit", command=master.destroy).grid(row=3, column=3, sticky=W, pady=4)
    master.mainloop()


def validateEntry(entry):
    # Validação unica: não estar já registrado no arquivo
    RAs = listOfRas()
    lista = []

    for linha in RAs:
        ra = linha.split(" - ")[0]
        lista.append(ra)
    
    return entry in lista


def add(ra, time, master):
    if not validateEntry(ra):
        file = open(PATH, "a")
        file.write(ra + " - " + time + "\n")
        file.close()
        validateEntry(ra)
        master.destroy()
    else:
        error = Label(master, text="RA já cadastrado", fg="red")
        error.place(x=75, y=50)


def show_all():
    RAlist = listOfRas()
    master = Tk()

    # lista = Listbox(master, font=("Courier New", 14), justify="center", selectmode=MULTIPLE)
    # scrollbar = Scrollbar(master, orient="vertical")
    # scrollbar.config(command=lista.yview)
    # scrollbar.pack(side="right", fill="y")
    # lista.config(yscrollcommand=scrollbar.set)

    lista = createListBox(master)

    # i = 1
    # for ra in RAlist:
    #     lista.insert(i, ra)
    #     i+=1
    # lista.pack()

    fillListBox(lista, RAlist)
    master.mainloop()


def toList(arg):
    lista = []

    for elm in arg:
        lista.append(elm)
    return lista


def remove_RA():
    # curselection()
    RAlist = listOfRas()
    master = Tk()
    master.geometry("370x230")

    lista = createListBox(master)

    fillListBox(lista, RAlist)

    removeButton = Button(master, text="Remover", command=lambda: removeFromList(lista, RAlist, master) ,bg="red", fg="black")
    removeButton.place(x=4, y=200)

    master.mainloop()


# FIXthis 0> FIXED 29/11
def removeFromList(root, lista, master):
    selected = toList(root.curselection())
    selected.sort()
    
    for elm in selected[::-1]:
        lista.pop(elm)
    print(selected)
    file = open(PATH, "w")

    for elm in lista:
        file.write(elm)
    file.close()

    root.delete(0, END)
    fillListBox(root, lista)

    # master.destroy()
    master.mainloop()


def listOfRas():
    file = open(PATH, "r")
    RAlist = file.readlines()
    file.close()

    return RAlist


def createListBox(root):
    lista = Listbox(root, font=("Courier New", 14), justify="center", selectmode=MULTIPLE)
    scrollbar = Scrollbar(root, orient="vertical")
    scrollbar.config(command=lista.yview)
    scrollbar.pack(side="right", fill="y")

    lista.config(yscrollcommand=scrollbar.set)

    return lista


def fillListBox(box ,content):
    i = 1
    for ra in content:
        box.insert(i, ra)
        i+=1
    box.pack()


RAs = []

root = Tk()

canvas1 = Canvas(root, width = 200, height = 200)
canvas1.pack()

button1 = Button(text="Add RA", command=add_RA, bg="white", fg="black")
canvas1.create_window(100, 50, window=button1)

button2 = Button(text="Mostrar lista", command=show_all, bg="yellow", fg="black")
canvas1.create_window(100, 100, window=button2)

button3 = Button(text="Remover RA", command=remove_RA, bg="red", fg="black")
canvas1.create_window(100, 150, window=button3)



root.mainloop()
