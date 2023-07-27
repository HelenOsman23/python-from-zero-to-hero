# La forma más frecuente de recorrer un arreglo es tilizando el loop for.

some_list = ["sleep", "eat", "study"]

# Utilizamos el for para recorrer en la lista
for elem in some_list:
    print(elem.title())

# Lo anterior funciona bien si queremos utilizar directamente los valores existentes, pero si queremos actualizar un valor, necesitaremos los índices.
print("-------------------------")
# Utilizamos el for sobre un rango desde cero hasta la ultima posición de la lista. en todo momento es un rango de NÚMEROS
# Podemos utilizar esos números como indices para acceder a los elementos de la lista.
for position in range(len(some_list)):
    some_list[position] = some_list[position].upper()

print(some_list)    

cities = ["bogotá", "caracas", "lima", "la paz", "san josé"]

for citi in cities:
    print(citi.title())

for position in range(len(cities)):
    cities[position] = cities[position].title()

print(cities)

print("-------------------------")

numbers = [4,3,5,6,7,4,3,5,6,7]

for index in range(len(numbers)):
    numbers[index] = numbers[index] * 2

print(numbers)    