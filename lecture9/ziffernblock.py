# Zeige Schaltflaechen von 1 bis 9 an, in einem 3x3 Gitter
import tkinter
from tkinter import messagebox

def button_callback(nummer):
    messagebox.showinfo("THI-SWD", f"Button {nummer} geklickt")
from functools import partial
haupt_fenster = tkinter.Tk()
nummer = 1
for zeile in range(3):
    for spalte in range(3):
        schaltflaeche = tkinter.Button(haupt_fenster, 
                                       text=nummer, width=10, height=5,
                                       command=partial(button_callback, nummer))
        schaltflaeche.grid(row=zeile, column=spalte)
        nummer += 1

haupt_fenster.mainloop()