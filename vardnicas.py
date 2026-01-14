

#1uzdevums
# dict={
#     "Anna": 6,
#     "Jānis": 8,
#     "Pēteris": 7,
#     "Līga": 9,
#     "Andris": 5
# }

# print(dict.keys())
# print(dict.values())

# print(dict["Jānis"])
# dict.update({"Artis": 4})
# dict.pop("Pēteris")
# print(dict)


#2uzdevums
auglu_krasas={
    "ābols":"sarkans",
    "banāns":"dzeltens",
    "apelsīns":"oranžs",
}

auglu_krasas.update({"kivi":"zaļš"})
print(auglu_krasas)
auglu_krasas["banāns"]="brūns"
print(auglu_krasas)
print(auglu_krasas.values())