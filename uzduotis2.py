# Patobulinti 1 užduoties programą, kad ji:
#Atspausdintų pasisveikinimą ne tik nuspaudus mygtuką, bet ir paspaudus mygtuką "Enter".

from tkinter import *

#cia paprastas tuscias langas, be ivedimu.
#visas_langas = Tk()
#visas_langas.geometry("300x300")
#pavadinimas = Label(visas_langas, text="")  # tuscia, nes nenoriu kad butu pavadinimas.
#pavadinimas.pack()  # be situ dvieju eiluciu veikia, kai nereikia pavadinimo
#visas_langas.mainloop()


# Turėtų laukelį su užrašu "Įveskite vardą", kuriame vartotojas galėtų įvesti vardą,
# Turėtų mygtuką su užrašu "Patvirtinti",
# kurį nuspaudus, programa po lauku atspausdintų "Labas, {vardas}!"

#su grid funcija?
visas_langas = Tk()

def paspaudus():
    vardas = laukelis_vardo.get()
    ka_parodys_paspaudus["text"] = ("Labas, " + vardas + "!")

pirmas_uzrasas = Label(visas_langas, text="Įveskite vardą: ")
laukelis_vardo = Entry(visas_langas)
mygtukas = Button(visas_langas, text="Patvirtinti", command=paspaudus)
laukelis_vardo.bind("<Return>", lambda e: paspaudus()) #Atspausdina pasisveikinimą paspaudus mygtuką "Enter".
ka_parodys_paspaudus = Label(visas_langas, text="")

pirmas_uzrasas.grid(row=0, column=0, sticky=E)
laukelis_vardo.grid(row=0, column=1)
mygtukas.grid()
ka_parodys_paspaudus.grid(row=1, columnspan=3)

visas_langas.mainloop()



