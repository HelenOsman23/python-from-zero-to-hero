import random
# Programar con estructuras de control y expresiones Booleanas un juego del cachipun
# El programa debe solicitar al usuario que escriba "piedra", "papel", o "tijera"
computer_choice = random.choice(["piedra","papel","tijera"])

print("---Bienvenidos al juego del cachipun---")

user_option = input("Escoge entre piedra papel o tijera: ")

if user_option == computer_choice:
    print("La opción del computador es: ",computer_choice)
    print("¡Empate!")
elif (user_option == "tijera" and computer_choice == "papel") or (user_option == "piedra" and computer_choice == "tijera") or (user_option == "papel" and computer_choice == "piedra"):
    print("La opción del computador es: ",computer_choice)
    print("¡Ganaste!")
else:
    print("La opción del computador es: ",computer_choice)
    print("¡Perdiste!")

