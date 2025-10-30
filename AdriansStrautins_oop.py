
import tkinter as tk #importē tkinter
from tkinter import messagebox

logs=tk.Tk() #logs
logs.title("Spiediena aprēķins") #loga nosaukums
logs.geometry("500x500+700+300") #loga koordinātas un izmērs
logs.resizable(True,True) #loga izmēra maiņa

jedziens1=tk.Label(logs, text="p - Spiediens", font=('Arial',10,'bold'), padx=100, pady=10, width=13, height=1)
jedziens1.pack() #pievieno jēdzienu skaidrojumu
jedziens2=tk.Label(logs, text="F - Spiediena spēks", font=('Arial',10,'bold'), padx=100, pady=10, width=13, height=1)
jedziens2.pack() #pievieno jēdzienu skaidrojumu
jedziens3=tk.Label(logs, text="S - Laukums", font=('Arial',10,'bold'), padx=100, pady=10, width=13, height=1)
jedziens3.pack() #pievieno jēdzienu skaidrojumu

tk.Label(logs, text="Ieraksti spiediena spēku F (ņūtoni): ", font=('Arial',10,'bold') ).pack()
ievade1 = tk.Entry(logs)
ievade1.pack() #izveido ievades logu lielumam F

tk.Label(logs, text="Ieraksti virsmas laukumu S (kvadrātmetri): ", font=('Arial',10,'bold')).pack()
ievade2 = tk.Entry(logs)
ievade2.pack() #izveido ievades logus lielumam S

def rezultats(): #funkcija
    try:
        sk1 = float(ievade1.get()) #pirmā lieluma iegūšana
        sk2 = float(ievade2.get()) #otrā lieluma iegūšana
        sum = sk1/sk2 #darbība
    except ValueError:
        messagebox.showwarning("Brīdinājums!", "Ievadi skaitli") #nepareizu simbolu kļūda
    except ZeroDivisionError:
        messagebox.showinfo("Spiediena rezultāts", "Nevar dalīt ar nulli") #dalīšana ar nulli kļūda
    messagebox.showinfo("Spiediena rezultāts", f"Spiediens:{sum} paskāli") 

rezultata_poga = tk.Button(logs, text="Dalīt", bg="green", command=rezultats) #rezultāta poga


rezultata_poga.pack()

logs.mainloop() 