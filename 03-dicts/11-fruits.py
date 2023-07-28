fruits_prices = {
    "paltas" : 4200,
    "platanos" : 800,
    "piña" : 2000,
    "mangos" : 1000,
    "bambino" : 1100,
    "limones" : 850, 
    "lechugas" : 1200
}

# Se pide craer un programa que muestre el precio por kilo de la verdura o fruta solicitada
# 1 Pedir que ingrese la fruta a buscar 
search = input("¿Que precio quieres saber?: ")
# 2 Mostrar el precio si exite
if search in fruits_prices:
    print("El precio de",search,"es:",fruits_prices[search] )
# 3 Mostrar que no tiene ese vegetal
else:
    print("No tengo ese dato")