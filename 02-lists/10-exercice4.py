# Escriba un programa que permita crear una lista de palabras, para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que imprimir la lista
# El .append() se utiliza para agregar elementos a una lista 

user_number = int(input("Ingresa el número de palabras para la lista: "))
words = []

for number in range(user_number):
    word = input(f"Ingresa la palabra {number}")
    words.append(word)

print(words)    
    
