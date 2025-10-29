import tkinter as tk

logs=tk.Tk()
logs.title("Ievieto bildi!")
logs.geometry('400x600')

def saskaita():
    try:
        rezultats=int(ievade1.get())+int(ievade2.get())
        teksts.config(text=rezultats)
        teksts2.config(image=bilde)
    except ValueError:
        teksts.config(text=("Kļūda! Ievadiet skaitļus!"))

teksts=tk.Label(logs, text="")
teksts.pack(pady=10)

teksts2=tk.Label(logs, text="")
teksts2.pack(pady=30)

bilde=tk.PhotoImage(file='')

ievade1=tk.Entry(logs)
ievade1.pack(pady=10)
ievade2=tk.Entry(logs)
ievade2.pack(pady=10)

poga=tk.Button(logs, text="Saskaitīt", command=saskaita)
poga.pack(pady=10)

logs.mainloop