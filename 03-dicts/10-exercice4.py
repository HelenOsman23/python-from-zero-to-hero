averages = {
    "John" : 5,
    "Mary" : 6.5,
    "David" : 7,
    "Peter" : 6.4,
    "Emily" : 6.2,
    "Helen" : 4.8
}

# Recorrer las llaves de diccionario
for key in averages.keys():
# Revisar si el valor es mayor a 6
    if averages[key] > 6:
# Imprimir los aprobados
        print("El estudiante",key,"aprobó con un promedio:", averages[key])
    else:
# Imprimir los reprobados
        print("El estudiante",key,"reprobo con promedio:", averages[key])                        