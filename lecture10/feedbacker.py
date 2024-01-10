class Feedbacker:
    def __init__(self):
        pass
    
    def positive(self):
        pass
    
    def negative(self):
        pass

class PrintFeedbacker(Feedbacker):
    def positive(self):
        print("Gut gemacht!")

    def negative(self):
        print("Probier's nochmal!")

from tkinter import messagebox
class TkinterFeedbacker(Feedbacker):
    
    def positive(self):
        messagebox.showinfo("THI Quiz", "Richtige Antwort")

    def negative(self):
        messagebox.showerror("THI Quiz", "Leider nein")
        
if input("Verwende Tkinter? (j|n)") == "j":
    f = TkinterFeedbacker()
else:
    f = PrintFeedbacker()
    
if int(input("Was ist 2+2?")) == 4:
    f.positive()
else:
    f.negative()