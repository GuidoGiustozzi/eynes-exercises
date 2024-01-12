def transpose(matrix):
    """ SACAMOS LA CANTIDAD DE FILAS Y COLUMNAS:  COMO ES LISTAS DE LISTA, LAS FILAS SE DETERMINAN POR LA CANTIDAD DE LISTAS QUE CONEITENE 
    Y LAS COLUMNAS SE DETERMINAN POR EL TAMAÑO DE LAS LISTAS, EN ESTE CASO TOMAMOS LA PRIMERA"""
    cantidadFilas = len(matrix)
    cantidadColumnas = len(matrix[0])
    lista_a_devolver = []
    for x in range(cantidadColumnas):
        lista_a_devolver.append([])  # AÑADIMOS LISTA VACIA
        for i in range(cantidadFilas):
            lista_a_devolver[x].append(matrix[i][x])
    return lista_a_devolver


matrix = [[5, 1],
          [4, 6]
          ]
transpuesta = (transpose(matrix))

for x in transpuesta:
    print(x)
