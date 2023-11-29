import tkinter
from tkinter import messagebox # manchmal notwendig

def sag_servus():
    messagebox.showinfo("THI-SWD", "Servus WI")
    messagebox.showerror("THI-SWD", "Ungültige Auswahl!")
    messagebox.showwarning("THI-SWD", "Achtung vor der SWD-Klausur")
    schaltflaeche.config(text="Na dann!")
    print("Servus")

haupt_fenster = tkinter.Tk()
haupt_fenster.title("THI - WI3 / SWD")
leinwand = tkinter.Canvas(haupt_fenster, width=600, height=300)
leinwand.grid(columnspan=3, rowspan=5)

schaltflaeche = tkinter.Button(haupt_fenster, text="Sag Servus", command=sag_servus)
schaltflaeche.grid(column=1, row=3)
schaltflaeche.configure(width=15)
#schaltflaeche.pack()
haupt_fenster.mainloop()