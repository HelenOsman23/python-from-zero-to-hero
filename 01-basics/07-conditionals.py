# La ejecución condicional del código se realiza evaluando sentencias lógicas. Estas sentencias entregan un valor de tipo Booleano (Bool), es decir, entregan True o False
# 
print("-------Expresiones Booleanas-------")
print( 5 > 4) # True
print( 5 < 4) # False
print( 4 == '4') # False porque uno es número y el otro es texto
print( 4 != 4) # False 

# Si queremos comparar menor o igual
print( 4 <= 4)
# Para mayor o igual
print( 4 >= 4)

# Podemos también tener expresiones Booleanas compuestas utilizando operadores and, or y not 
print("-----Expresiones Boolenas compuestas-----")
print( 4 < 5 or 6 > 8) # True or False => True
print( 4 < 5 and 6 > 8) # True and False => False
print( 4 > 5 and 6 > 8) # False and False => False

# El not devuelve el contrario del valor
print(not True)
print(not False)