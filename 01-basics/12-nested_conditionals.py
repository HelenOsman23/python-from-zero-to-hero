# Una evaluación condicional puede estar dentro de otra:

name = input("Hola, ¿Cuál es tu nombre?: ")
age = int(input("Dime tu edad: "))

if age >= 18:
    drink = input("¿Quieres cerveza o vino?: ")
    if drink == "cerveza":
        print("Toma",name)
        print("Aquí tienes tu cerveza")
    else:
        print("Aquí tienes tu vino")
else:
    juice = input("¿Quieres jugo de frutilla o naranja?: ")
    print("Toma",name)
    if juice == "frutilla":
        print("Aquí está tu jugo de frutilla")
    else:
        print("Aquí está tu jugo de naranjas")            

        