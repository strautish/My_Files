

import tkinter as tk
from tkinter import messagebox

def atjaunot_krasu():
    r = sarkans.get()
    g = zalais.get()
    b = zils.get()
    hex_kods = f"#{r:02x}{g:02x}{b:02x}"
    paraugs.config(bg=hex_kods)

# Funkcijas, ko izsauc, kad mainās slaideru vērtības
def mainit_sarkano(v):
    atjaunot_krasu()

def mainit_zalo(v):
    atjaunot_krasu()

def mainit_zilo(v):
    atjaunot_krasu()

# Funkcija paziņojuma logam
def paradit_rgb():
    r = sarkans.get()
    g = zalais.get()
    b = zils.get()
    hex_kods = f"#{r:02x}{g:02x}{b:02x}"
    messagebox.showinfo(
        "Pašreizējās RGB vērtības",
        f"R: {r}\nG: {g}\nB: {b}\n\nHEX kods: {hex_kods}"
    )

# Galvenais logs
logs = tk.Tk()
logs.title("Krāsu Mikseris")
logs.geometry("300x320")
logs.resizable(False, False)

# Slaideri krāsu izvēlei
sarkans = tk.Scale(logs, from_=0, to=255, orient="horizontal",
                   label="Sarkans (R)", command=mainit_sarkano)
sarkans.pack(fill="x", padx=10, pady=5)

zalais = tk.Scale(logs, from_=0, to=255, orient="horizontal",
                  label="Zaļš (G)", command=mainit_zalo)
zalais.pack(fill="x", padx=10, pady=5)

zils = tk.Scale(logs, from_=0, to=255, orient="horizontal",
                label="Zils (B)", command=mainit_zilo)
zils.pack(fill="x", padx=10, pady=5)

# Krāsas parauga etiķete
paraugs = tk.Label(logs, text="Krāsas paraugs", bg="#000000", fg="white", width=20, height=4)
paraugs.pack(pady=10)

# Poga RGB un HEX vērtību parādīšanai
poga = tk.Button(logs, text="Parādīt RGB un HEX vērtības", command=paradit_rgb)
poga.pack(pady=5)

# Inicializē sākotnējo krāsu
atjaunot_krasu()

# Galvenā notikumu cilpa
logs.mainloop()