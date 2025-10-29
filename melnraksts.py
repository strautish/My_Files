
import tkinter as tk
from tkinter import messagebox

def aprekinat_spiedienu():
Ftext = entry_F.get()
Stext = entry_S.get()

# Pārbaude, vai ievades lauki nav tukši
if Ftext == "" or Stext == "":
messagebox.showerror("Kļūda", "Lūdzu ievadi abas vērtības!")
return

# Pārbaude, vai ievades ir skaitļi
if not (F_text.replace('.', '', 1).isdigit() and S_text.replace('.', '', 1).isdigit()):
messagebox.showerror("Kļūda", "Lūdzu ievadi tikai skaitļus!")
return

F = float(F_text)
S = float(S_text)

# Pārbaude, vai S nav nulle
if S == 0:
messagebox.showerror("Kļūda", "Virsmas laukums nevar būt 0!")
return

p = F / S
label_rezultats.config(text=f"Spiediens: {p:.2f} Pa")

# Galvenais logs
root = tk.Tk()
root.title("Spiediena aprēķins (p = F / S)")
root.geometry("300x200")

# Ievades lauki un etiķetes
label_F = tk.Label(root, text="Spēks (F) [N]:")
label_F.pack(pady=5)
entry_F = tk.Entry(root)
entry_F.pack()

label_S = tk.Label(root, text="Virsmas laukums (S) [m²]:")
label_S.pack(pady=5)
entry_S = tk.Entry(root)
entry_S.pack()

# Poga aprēķinam
poga = tk.Button(root, text="Aprēķināt spiedienu", command=aprekinat_spiedienu)
poga.pack(pady=10)

# Rezultāta attēlošana
label_rezultats = tk.Label(root, text="Spiediens: ")
label_rezultats.pack(pady=5)

# Programmas palaišana
root.mainloop()