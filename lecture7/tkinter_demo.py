import tkinter
haupt_fenster = tkinter.Tk()
haupt_fenster.title("THI - WI3 / SWD")
leinwand = tkinter.Canvas(haupt_fenster, width=600, height=300)
leinwand.grid(columnspan=3, rowspan=5)

textfeld = tkinter.Label(haupt_fenster, text="Hallo WI, Wie geht's dir \ndenn heute so?")
textfeld.grid(column=1, row=2)

schaltflaeche = tkinter.Button(haupt_fenster, text="OK")
schaltflaeche.grid(column=1, row=4)
schaltflaeche.configure(width=15)
#schaltflaeche.pack()
haupt_fenster.mainloop()