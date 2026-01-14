# Dati tiek pievienoti skoleni.csv failam.
# Pēc ievades programma nolasīs failu un pieprasa klasi un
# atlasa/izdrukā tikai pieprasītās klases skolēnus, izvada atlasītos datus jaunā csv failā

import csv

print("=== Skolēnu reģistrācija ===")
print("Ievadi skolēnus. Lai beigtu — atstāj 'Vārds' lauku tukšu un spied Enter.\n")

# 1. Ievade un saglabāšana failā skoleni.csv
with open('skoleni.csv', 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    
    # Ja fails tukšs — pievienojam virsrakstus
    if f.tell() == 0:
        writer.writerow(['Vārds', 'Uzvārds', 'Klase'])

    while True:
        vards = input("Vārds: ").strip()
        if vards == "":                    # tukšs vārds = beigt ievadi
            print("Ievade pabeigta!\n")
            break
        uzvards = input("Uzvārds: ").strip().capitalize()
        klase = input("Klase (piem. 10.A): ").strip().upper()

        # Saglabājam CSV failā
        writer.writerow([vards.capitalize(), uzvards, klase])
        print(f"Pievienots: {vards.capitalize()} {uzvards} no {klase} klases\n")

# # 2. Nolasām visus datus no faila
# while True:
#     skoleni = []
# 
#     with open('skoleni.csv', 'r', encoding='utf-8') as f:
#         reader = csv.reader(f)
#         next(reader)  # izlaižam virsrakstus (Vārds,Uzvārds,Klase)
# 
#         for rinda in reader:
#             if len(rinda) != 0:           # ja rinda nav tukša
#                 skoleni.append(rinda)
#         # Ja nav datu
#         if len(skoleni) == 0:
#             print("Failā nav skolēnu. Pievieno vismaz vienu!")
#             break
#             
#             
#         
#         mekle_klase = input("\nKuras klases skolēnus gribi redzēt? (piem. 10.A): ").strip().upper()
# 
#         atrastie = []
#         for skolens in skoleni:
#             if skolens[2] == mekle_klase:
#                 atrastie.append(skolens)
# 
#         if len(atrastie) > 0:
#             print(f"\nSkolēni no {mekle_klase} klases:")
#     #         print (atrastie)
#             for s in atrastie:
#                 print(f"• {s[0]} {s[1]}")
#                 
#         break
# 
# # Eksportējam uz atsevišķu failu
# faila_nosaukums = mekle_klase + "_klase.csv"
# with open(faila_nosaukums, 'w', newline='', encoding='utf-8') as eks:
#     writer = csv.writer(eks)
#     writer.writerow(['Vārds', 'Uzvārds', 'Klase'])
#     for s in atrastie:
#         writer.writerow(s)
# 
#     print(f"\nSaglabāts failā: {faila_nosaukums}")
#     

