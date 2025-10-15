
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("250x300")
root.title("Kalkulators")

tk.Label(root, text="Ieraksti pirmo skaitli: ").pack()
ievade1 = tk.Entry(root)
ievade1.pack()

tk.Label(root, text="Ieraksti otro skaitli: ").pack()
ievade2 = tk.Entry(root)
ievade2.pack()

def rezultats():
    try:
        sk1 = float(ievade1.get())
        sk2 = float(ievade2.get())
        sum = sk1/sk2
    except ValueError:
        messagebox.showwarning("Brīdinājums!", "Ievadi skaitli")
    except ZeroDivisionError:
        messagebox.showinfo("Rezultāts", "Nevar dalīt ar nulli")
    messagebox.showinfo("Rezultāts", f"Atbilde:{sum}")

rezultata_poga = tk.Button(root, text="Dalīt", command=rezultats)
rezultata_teksts = tk.Label(root, text="Rezultāts: ")

rezultata_poga.pack()
rezultata_teksts.pack()

root.mainloop()