import numpy as np
lista1 = [1,2,3,4,5,6,3,2,8,9]
array1 = np.array(lista1)
print(type(lista1))
print(lista1)
print(type(array1))
print(array1)

lista2 = [[1,2,4],[2,5,3],[9,4,2]]
array2 = np.array(lista2)
print(array2)

# Arrays generación automática
array3 = np.arange(6)
print(array3)

array4 = np.arange(2,15,3)
print(array4)

matrizCeros = np.zeros((4,5))
print(matrizCeros)

matrizUnos = np.ones((3,5))
print(matrizUnos)

# Matriz de 40 elementos con valores del 2 al 6
matriz1 = np.linspace(2, 6, 40)
print("matriz1:")
print(matriz1)

# Matriz identidad de 7x7
matrizIdentidad = np.eye(7)
print(matrizIdentidad)

#Matriz de números aleatorios
matrizAl1 = np.random.rand(4, 6)
print(matrizAl1)

matrizAl2 = np.random.rand(4, 6)
print(matrizAl2)

matrizAlNormal = np.random.randn(4)
print(matrizAlNormal)

matrizAlEnteros = np.random.randint(1, 51, 20)
print(matrizAlEnteros)

#Tamaño de arrays
array5 = np.random.randint(1, 201, 30)
print(array5)
matriz2 = array5.reshape(5, 6)
print(matriz2)

# Max y min
array = np.random.randint(1, 901, 200)
print(array)
maximo = array.max()
print(f"El valor máximo es {maximo}")
print(array.argmax())
minimo = array.min()
print(f"El valor mínimo es {minimo}")
print(array.argmin())

# Mostrar elementos
array = np.arange(1, 11)
print(array)
print(array[2])
print(array[5:])
print(array[:6])

# Copia de array
array2 = array.copy()
print(array)
print(array2)
array2[4] = 9999
print(array)
print(array2)

# Operaciones con matrices
print(matrizAl1)
print(matrizAl1[0]) #Primera fila
print(matrizAl1[:2]) #Desde el inicio hasta la segunda fila
print(matrizAl1[1][2]) #Elemento de la segunda fila y tercera columna
print(matrizAl1[2,3]) #Elemento de la tercera fila y cuarta columna
print(matrizAl1[:,1]) #Elementos de la segunda columna de todas las filas
print(matrizAl1[:,:1]) #Elementos de la primera columna
print(matrizAl1[:,:2]) #Elementos de las dos primeras columnas
print(matrizAl1[:2,:2]) #Primeras dos filas de las dos primeras columnas
print(matrizAl1+10) #Sumar 10 a cada elemento de la matriz
print(matrizAl1*10) #Multimplicar 10 a cada elemento de la matriz
print(matrizAl1 + matrizAl1)
print(matrizAl1 * matrizAl1)
print(matrizAl1 + matrizAl2)
print(matrizAl1 * matrizAl2)
print(np.max(matrizAl1))
condicion = matriz1 > 4
print("matriz1:")
print(matriz1)
print("condicion:")
print(condicion)
print(matriz1[condicion])

# Números impares
condicion = matriz1 % 2 != 0
print(matriz1[condicion])

# Ejemplo redimensión
lista = np.arange(5,41)
print(lista)
lista = lista.reshape(3,12)
print(lista)

# Combinación
arrayCombinacion = np.random.randint(1,50,6)
print(f"La combinación es {arrayCombinacion}")