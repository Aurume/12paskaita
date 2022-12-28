# Perdaryti bet kurią ankstesnėse pamokose sukurtą arba savo programą,
# kurioje vartotojas turėjo įvesti duomenis, į programą su grafine sąsaja.
# Pvz., tą, kuri atrenka keliamuosius metus, skaičiuoja laiką nuo praeitos datos.

from tkinter import *
import calendar

visas_langas = Tk()

def ar_keliamieji():
    if calendar.isleap(int(laukelis_vardo.get())):
        ka_parodys_paspaudus["text"] = "Keliamieji"
    else:
        ka_parodys_paspaudus["text"] = "Nekeliamieji"
    laukelis_vardo.delete(0, "end")

def iseiti():
    visas_langas.destroy()

pirmas_uzrasas = Label(visas_langas, text="Įveskite metus: ")
laukelis_vardo = Entry(visas_langas)
mygtukas = Button(visas_langas, text="Tikrinti", command=ar_keliamieji)
laukelis_vardo.bind("<Return>", lambda e: ar_keliamieji())
ka_parodys_paspaudus = Label(visas_langas, text="")

# Nuspaudus klaviatūros mygtuką "Escape", uždarytų programos langą.
visas_langas.bind("<Escape>", lambda e: iseiti())

# statuso juostos kūrimas
status = Label(visas_langas, text="", bd=1, relief=SUNKEN, anchor=W)


pirmas_uzrasas.grid(row=0, column=0, sticky=E)
laukelis_vardo.grid(row=0, column=1)
mygtukas.grid()
ka_parodys_paspaudus.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W+E)

visas_langas.mainloop()
