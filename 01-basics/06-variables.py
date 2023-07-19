# Vimos que a los valores se les puede asignar un nombre. Este nombre se conoce como variable.
# Tal como su nombre lo indica, podemos utilizar el mismo nombre para apuntar a diferentes valores, uno a la vez 

# Cuando primero le damos el valor a variable lo llamamos ASIGNACIÓN 
name = "Helen"

print(name.title())

# Cuando utilizamos la variable con un nuevo valor se llama RE ASIGNACIÓN
name = "Helen Ramirez"

print(name.title())

# Los nombres de las variables son sencibles a las mayúsculas y minúsculas:

NAME = "Soy Más"
Name = "Python"

print(name,NAME,Name)

# Los nombres de las variables no pueden partir con un número y tampoco coincidir con las palabras reservadas de Python
# https://flexiple.com/python/python-reserved-words/ 

# Para variables de más de una palabra utilizar el _ guion bajo
cake_type = "Napolitana"