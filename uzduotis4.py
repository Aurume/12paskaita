# Patobulinti 3 užduoties programą, kad ji turėtų statuso juostą apačioje, kurioje:
#
# Būtų rodoma "Sukurta", kai atspausdinamas pasisveikinimo tekstas
# Būtų rodoma "Išvalyta", kai ištrinamas pasisveikinimo tekstas
# Būtų rodoma "Atkurta", kai atkuriamas paskutinis pasisveikinimo tekstas

from tkinter import *
visas_langas = Tk()

atstatyti = StringVar()

def paspaudus():
    vardas = laukelis_vardo.get()
    ka_parodys_paspaudus["text"] = ("Labas, " + vardas + "!")
    status["text"] = "Sukurta"

def isvalyti():
    atstatyti.set(laukelis_vardo.get())
    laukelis_vardo.delete(0, 'end')
    ka_parodys_paspaudus["text"] = ""
    status["text"] = "Išvalyta"


def atkurti():
    laukelis_vardo.insert(0, atstatyti.get())  # atkuria varda
    paspaudus()  # atkuria ir pasisveikinima
    status["text"] = "Atkurta"

def iseiti():
    visas_langas.destroy()

pirmas_uzrasas = Label(visas_langas, text="Įveskite vardą: ")
laukelis_vardo = Entry(visas_langas)
mygtukas = Button(visas_langas, text="Patvirtinti", command=paspaudus)
laukelis_vardo.bind("<Return>", lambda e: paspaudus())  #Atspausdina pasisveikinimą paspaudus mygtuką "Enter".
ka_parodys_paspaudus = Label(visas_langas, text="")

# Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą.
visas_langas.bind("<Escape>", lambda e: iseiti())

# statuso juostos kūrimas
status = Label(visas_langas, text="", bd=1, relief=SUNKEN, anchor=W)


# Meniu kūrimas čia:
meniu = Menu(visas_langas)
visas_langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)
meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()   # "Atkurti" ir "Išeiti" būtų atskyrimo brūkšnys
submeniu.add_command(label="Išeiti", command=iseiti)


pirmas_uzrasas.grid(row=0, column=0, sticky=E)
laukelis_vardo.grid(row=0, column=1)
mygtukas.grid()
ka_parodys_paspaudus.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W+E)

visas_langas.mainloop()
