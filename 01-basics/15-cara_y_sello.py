import random

computer_choice = random.choice(["cara","sello"])
user_option = input("Escoge entre cara y sello: ")

if user_option == computer_choice :
    print("El computador tiro:",computer_choice)
    print("¡Empate!")
elif user_option == "cara" and computer_choice == "sello":
    print("El computador tiro:",computer_choice)
    print("¡Ganaste!")
else:
    print("El computador tiro:",computer_choice)
    print("¡Perdiste!")      