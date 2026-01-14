
import math
# Uzdevums 1

# class Darbinieks:
#     def __init__(self,vards,amats):
#         self.vards = vards
#         self.amats = amats

# jauns_darbinieks = Darbinieks("Anna", "Projekta vadītājs")


# Uzdevums 2

# class Darbinieks:
#     def __init__(self,vards,amats):
#         self.vards = vards
#         self.amats = amats

#     def radit_profilu(self):
#         print("Darbinieks:", self.vards)
#         print("Amats:", self.amats)

# jauns_darbinieks = Darbinieks("Anna", "Projekta vadītājs")

# jauns_darbinieks.radit_profilu()


# Uzdevums 3

# class Darbinieks:
#     def __init__(self,vards,amats,alga):
#         self.vards = vards
#         self.amats = amats
#         self.alga = 3000

#     def paaugstinat_algu(self,summa):
#         self.alga += summa
#         print("Jaunā alga ir:", self.alga)

#     def radit_profilu(self):
#         print("Darbinieks:", self.vards)
#         print("Amats:", self.amats)
#         print("Alga:", self.alga)

        

    

# jauns_darbinieks = Darbinieks("Anna", "Projekta vadītājs", 3000)


# jauns_darbinieks.paaugstinat_algu(500)

# jauns_darbinieks.radit_profilu()




# Uzdevums 4


# class Darbinieks:
#     def __init__(self,vards,amats,alga):
#         self.vards = vards
#         self.amats = amats
#         if alga == 2000:
#             self.alga = 2000
#         else:
#             self.alga = alga

#     def paaugstinat_algu(self,summa):
#         self.alga += summa
#         print("Jaunā alga ir:", self.alga)
        

#     def radit_profilu(self):
#         print("Darbinieks:", self.vards)
#         print("Amats:", self.amats)
#         print("Alga:", self.alga)


# jauns_darbinieks = Darbinieks("Anna", "Projekta vadītājs", 3500)

# jauns_darbinieks.paaugstinat_algu(200)

# jauns_darbinieks.radit_profilu()


# vecs_darbinieks = Darbinieks("Jānis", "Analītiķis", 2000)

# vecs_darbinieks.radit_profilu()





# Uzdevums 5

class Darbinieks:
    def __init__(self,vards,amats,alga):
        self.vards = vards
        self.amats = amats
        if alga == 2000:
            self.alga = 2000
        else:
            self.alga = alga

    def paaugstinat_algu(self,summa):
        if summa > 0:
            self.alga += summa
            print("Jaunā alga ir:", self.alga)
        else:
            print("Algas paaugstinājums nevar būt negatīvs!")

    def radit_profilu(self):
        print("Darbinieks:", self.vards)
        print("Amats:", self.amats)
        print("Alga:", self.alga)


jauns_darbinieks = Darbinieks("Anna", "Projekta vadītājs", 3500)

jauns_darbinieks.paaugstinat_algu(200)

jauns_darbinieks.radit_profilu()


jauns_darbinieks.paaugstinat_algu(-100)

jauns_darbinieks.radit_profilu()