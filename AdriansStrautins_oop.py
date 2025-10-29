
import tkinter as tk #importē tkinter

logs=tk.Tk()
logs.title("Fizika")
logs.geometry("500x500+700+300") #izveido logu

jedziens1=tk.Label(logs, text="p - Spiediens", font=('Arial',10,'bold'), padx=100, pady=10, width=13, height=1)
jedziens1.pack()
jedziens2=tk.Label(logs, text="F - Spiediena spēks", font=('Arial',10,'bold'), padx=100, pady=10, width=13, height=1)
jedziens2.pack()
jedziens3=tk.Label(logs, text="S - laukums", font=('Arial',10,'bold'), padx=100, pady=10, width=13, height=1)
jedziens3.pack() #pievieno jēdzienu skaidrojumu

tk.Label(logs, text="Ieraksti spiediena spēku F (kg): ").pack()
ievade1 = tk.Entry(logs)
ievade1.pack()

tk.Label(logs, text="Ieraksti virsmas laukumu S (kvadrātmetri): ").pack()
ievade2 = tk.Entry(logs)
ievade2.pack() #izveido ievades logus lielumiem

logs.mainloop() 