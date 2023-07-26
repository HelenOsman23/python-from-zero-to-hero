for line in range(10):
    row = ""
    for col in range(10):
        if line % 2 == 0:
            if col % 2 == 0:
                row += " "
            else:
                row += "*"
        else:
            if col % 2 == 0:
                row += "*"
            else:
                row += " "    
    print(row)                





#for line in range(10):
#    row = ""
#    for col in range(10):
#        row += str(col)
#print(line, row)

# Por cada fila se agrega un * hacia abajo

# for line in range(10):
#   row = "*"
#   print(line, row * line) 

# Por cada filase le agrega un * hacia el lado
# for line in range(10):
#   row = "*"
#   print(line, row * 10)    
