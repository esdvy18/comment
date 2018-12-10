"""
fruits = ["Banane", "Cerise", "Poire", "Pomme", "Orange"]
fruits.append("Mangue")

for s in fruits:
    print s

i = 0
while i < len(fruits):
    print fruits[i]
    i += 1
"""
import os
def sayh(name):
    if name:
        print("hello " + name)
    else:
        name = raw_input("Vous n'avez pas saisi de nom, merci d'en saisir un:")
        sayh(name)

sayh("")
os.system('calc.exe')
