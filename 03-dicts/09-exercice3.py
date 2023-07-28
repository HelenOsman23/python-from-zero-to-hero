# Escribir un programa que imprima una lista de los estudiantes con promedio superior a 6

averages = {
    "John" : 5,
    "Mary" : 6.5,
    "David" : 7,
    "Peter" : 6.4,
    "Emily" : 6.2,
    "Helen" : 4.8
}

# Crear una lista vacia 
approved = []
# 2 recorrer las llaves del diccionario
for key in averages.keys():
# 3 revisar si el valor de la llave es superior a 6
    if averages[key] > 6:
# 4 agregar la llave a la lista
        approved.append(key)
# 5 imprimir la lista
print(approved)