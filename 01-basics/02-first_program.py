# Prácticamente la totalidad de las aplicaciones y programas computacionales realizan las mismas operaciones: 
# 1~ Tomar datos desde el exterior como el teclado, el mouse,las redes (internet) u algún otro dispositivo como sensores o cámaras

# Python trae también una función básica para ingresar datos desde el teclado. La función input().

# 2~ Salida de datos al exterior como la terminal, una archivo, enviarlo por la red (internet)  o un parlante. etc.

# Python trae para esto la función print() que veremos más en detalle después 

# 3~ Otra operación que hace la mayoría de los programas es la EJECUCIÓN CONDICIONAL, que dependiendo de los valores ingresados, ejecuta el programa de cierta forma.
# Python trae esta ESTRUCTURA DE CONTROL, que también conoceremos más adelante.

# 4~ También los programas realizan operaciones con los valores, ya sea combiando, acumulando, calculando, etc.

# 5~ Repeticiones: Muchas veces para obtener un resultado es necesario repetir pasos sucesivos (receta de cocina).

user_name = input("Hello, ¿What is your name?: ")

print("Nice to meet you " + user_name)

if user_name == "Harvys":
    print("¡Somos tocayos!")

for letter in user_name:
    print(letter)    

