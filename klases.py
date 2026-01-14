
import math
# class Cars:
#     marka="Volvo"
#     durvis="4 durvis"
# my_car=Cars()

# print(my_car.marka)
# print(my_car.durvis)



# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

# p1 = Person("Emils", 36)

# print(p1.name)
# print(p1.age)
        
# p2 = Person("Peteris", 27)

# print(p2.name)
# print(p2.age)



# class Persona:
#     vards="Artis"
#     uzvards="Bērziņš"

# cilveks=Persona()
# print(cilveks.vards,cilveks.uzvards)


# class Persona:
#     def __init__(self, vards, uzvards):
#         self.vards = vards
#         self.uzvards = uzvards


#     def pilns_vards(self):
#         return self.vards + " " + self.uzvards

# p1=Persona("Artis","Bērziņš")

# print(p1.pilns_vards())





# class Rinkis:
#     def __init__(self,radiuss):
#         self.radiuss = radiuss

#     def rinka_laukums(self):
#         return math.pi*self.radiuss**2
    
#     def rinka_linija(self):
#         return 2*math.pi*self.radiuss
    
# rinkis1=Rinkis(5)
# print("Rinķa laukums:",rinkis1.rinka_laukums())
# print("Rinķa līnija:",rinkis1.rinka_linija())
        


# class Persona:
#     def __init__(self,vards,valsts,datums):
#         self.vards = vards
#         self.valsts = valsts
#         self.datums = datums

#     def vecums(self):
#         return 2025-self.datums
    
# p1=Persona("Jānis", "Latvija", 1999)

# print("Vecums ir:",p1.vecums())


class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade= grade

    def avg_grade(self):
        return sum(self.grade) / len(self.grade)
    
    def max_grade(self):
        return max(self.grade)
    
    

    def show_info(self):
        print("Maksimālā atzīme ir",self.max_grade())
        print (self.name ,"vidējā atzīme ir",self.avg_grade())
        if self.avg_grade()>=8:
            print("Students ir izcils:",self.izcils())
        else:
            print("Students nav izcils")    


s1=Student("Līga",[9,7,8,4,5])

s1.show_info()


