
import tkinter as tk
from tkinter import ttk

logs=tk.Tk()
logs.geometry("500x700+300+300")
logs.title("Kalkulators")

def saskait():
    sk1 = int(skaitlis1.get())
    sk2 = int(skaitlis2.get())
    summa = sk1 + sk2
    
    teksts3.config(text="Rezultāts:  +" str(summa))


teksts1=ttk.Label(logs, text="Ievadi pirmo skaitli")
teksts1.pack()

skaitlis1=ttk.Entry(logs)
skaitlis1.pack()

teksts2=ttk.Label(logs, text="Ievadi otro skaitli")
teksts2.pack()

skaitlis2=ttk.Entry(logs)
skaitlis2.pack()

poga=ttk.Button(logs, text="Saskaitīt", command=saskait)
poga.pack()

teksts3=ttk.Label(logs, text="Summa:", font="bold")
teksts3.pack()




logs.mainloop()


