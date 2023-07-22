# Podemos saltar una iteracción o una vuelta usando la palabra clave continue

spaces = ""
for letter in "murciélago":
    spaces += " "
    if letter == "l":
        continue
    print(spaces,letter) 
          
