for row in range(10):
    line = ""
    for col in range(10):
        if(row == 0 or row == 9 or col + row == 9 or col == row):
            line += "*"
        else:
            line += " "    
    print(line)
