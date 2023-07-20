# Pedir al usuario la temperatura.
user_therm = int(input("Ingrese la temperatura: "))
# Si la temperatura es menor que 0, imprime "me congelo"
if user_therm <= 0:
    print ("Me congeló")
# Si la temperatura es entre 1 y 15 imprime "tengo frio"
elif (user_therm >= 1) and (user_therm < 15):
    print("Tengo frio")
# Si la temperatura está en el rango de 16 a 25 imprime "temperatura ideal"
elif ((user_therm > 15) and (user_therm < 25)):
    print("Temperatura ideal")
# Si la temperatura es mayor a 26 imprime "Tengo mucho calor"
else:
    print("Tengo mucho calor")
    
