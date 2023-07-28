# Podemos tener diccionarios complejos con valores que también son colecciones 

classroom = {
    "helen": {
        "name":"Helen Pierina",
        "age": 23,
        "grades": [6,5,4,6,5,4,5,6]
    },
    "maria": {
        "name": "Maria clara",
        "age": 27,
        "grades": [7,6,5,6,7,7,6,5]
    },
    "thamara": {
        "name": "Thamara Carolina",
        "age": 35,
        "grades": [5,6,4,5,6,7,6,5,4]
    }
}

print(len(classroom))
print(classroom.keys())