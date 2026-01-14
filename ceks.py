
import csv

print("---Pirkuma reģistrācija---")
print("Ievadiet pirkumu. Lai beigtu - atstāj 'Pirkums' lauku tukšu un spied Enter.\n")

with open('ceks.csv', 'a', newline='', encoding='utf-8') as f:
    writer= csv.writer(f)

    if f.tell() == 0:
        writer.writerow(['Pirkums', 'Cena', 'Iedotā nauda'])

    while True:
        pirkums = input("Pirkums: ").strip()
        if pirkums == "":
            print("Ievade pabeigta!\n")
            break
        cena= input("Cena: ").strip()
        iedota_nauda= input("Iedotā nauda: ").strip()

        writer.writerow([pirkums.capitalize(), cena, iedota_nauda])
        print(f"Pievienots: {pirkums.capitalize()} par {cena} EUR, iedota nauda {iedota_nauda} EUR\n")