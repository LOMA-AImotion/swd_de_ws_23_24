# Zeige Schaltflaechen von 1 bis 9 an, in einem 3x3 Gitter
import tkinter

haupt_fenster = tkinter.Tk()
nummer = 1
for zeile in range(3):
    for spalte in range(3):
        schaltflaeche = tkinter.Button(haupt_fenster, text=nummer, width=10, height=5)
        schaltflaeche.grid(row=zeile, column=spalte)
        if zeile == 2: # nur zum Ausprobieren
            schaltflaeche.configure(height=10)
        nummer += 1

haupt_fenster.mainloop()