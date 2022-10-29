from operator import concat
import pandas as pd
import numpy as np

etiquetas = ['a','b','c','d','e']
datos = np.arange(4,9)
serie = pd.Series(datos, index=etiquetas)
print(serie)

# Acceder a un valor
print(serie['c'])

# Datos de distinto tipo
datos = [10, 20, 'José', 'María', 30, 'Luis']
serie = pd.Series(datos)
print(serie)

# Datos directos
serie = pd.Series([1000, 2000, 500, 300, 3000], ['Emp001','Emp002','Emp003','Emp004','Emp005'])
print(serie)

# Suma de series
serie1 = pd.Series([1000, 2000, 500, 300, 3000], ['Emp001','Emp002','Emp003','Emp004','Emp005'])
print(serie1)

serie2 = pd.Series([1010, 2020, 550, 330, 3030], ['Emp001','Emp002','Emp003','Emp004','Emp005'])
print(serie2)

serie3 = serie1 + serie2
print(serie3)

# Dataframes
filas = ['tienda1','tienda2','tienda3','tienda4','tienda5']
columnas = ['producto1','producto2','producto3']
datos = [[110,120,130],[220,230,240],[330,340,350],[440,450,460],[550,560,570]]
datos2 = [[np.nan,120,130],[np.nan,230,240],[330,np.nan,350],[440,450,np.nan],[550,560,570]]
dataframe = pd.DataFrame(datos, index=filas, columns=columnas)
dataframe2 = pd.DataFrame(datos2, index=filas, columns=columnas)
print(dataframe)

# Seleccionar filas
print(dataframe.loc['tienda2'])
print(dataframe.loc[['tienda2','tienda3']])

# Seleccionar columnas
print(dataframe['producto2'])
print(dataframe[['producto1','producto3']])

# Mostrar un elemento específico
print(dataframe.loc['tienda2','producto3'])

# Agregar una columna
dataframe['producto4'] = 25
print(dataframe)

dataframe['total'] = dataframe['producto1']+dataframe['producto2']+dataframe['producto3']+ \
    dataframe['producto4']
print(dataframe)

# Eliminar columna (solo al mostrar)
print(dataframe)
print(dataframe.drop(['total'], axis=1)) # axis=0 corresponde a fila y axis=1 corresponde a columna
print(dataframe)

# Eliminar columna del dataframe
print(dataframe)
#dataframe = dataframe.drop(['total'], axis=1) # Alternativa de eliminación 1
print(dataframe.drop(['total'], axis=1, inplace=True)) # Alternativa de eliminación 2
print(dataframe)

# Mostrar elementos que cumplen condición
condicion = dataframe>200
print(dataframe[condicion])

condicion = (dataframe['producto1']>=200) & (dataframe['producto2']>=300) # AND
print(dataframe[condicion])

condicion = (dataframe['producto1']>=200) | (dataframe['producto2']>=300) # OR
print(dataframe[condicion])

# Cambiar índice
nuevaColumna = '1 2 3 4 5'.split() # Agregar elementos separados por espacios
print(nuevaColumna) 
nuevaColumna = '1-2-3-4-5'.split('-') # Agregar elementos separados por un caracter
print(nuevaColumna)
dataframe['indices'] = nuevaColumna
print(dataframe)
dataframe = dataframe.set_index('indices')
print(dataframe)

# Eliminar filas o columnas con NaN
#dataframe2.dropna(axis=0, inplace=True) # axis=0 corresponde a fila y axis=1 corresponde a columna
print(dataframe2)

# Rellernar NaN con otro valor
#dataframe2.fillna(value=90, inplace=True)
print(dataframe2)

# Reemplazar NaN con la media
media = dataframe2.mean()
print(f"La media es igual a {media}")
dataframe2.fillna(value=media, inplace=True)
print(dataframe2)

# Unión de dataframes
data1 = dataframe.copy()
data2 = dataframe.copy()
print(data1)
print(data2)
dataTotal = pd.concat([data1, data2], axis=1)
print(dataTotal)
dataTotal = pd.concat([data1, data2], axis=0)
print(dataTotal)

print(dataTotal['producto1'].unique())
print(dataTotal['producto1'].value_counts())

dataTotal = dataTotal.apply(lambda x: x*5)
print(dataTotal)

print(dataTotal.columns)
print(dataTotal.index)
print(dataTotal.sort_values(['producto1']))

# Mostrar estadísticas del dataframe
print(dataTotal.describe())

# Pasar un dataframe a diferentes formatos
dataTotal.to_csv('dataTotal.csv')
#dataTotal.to_excel('dataTotal.xls')
data1.to_json('data1.json')

# Cargar datos a un dataframe desde un archivo
dataframeCarga = pd.read_csv('dataTotal.csv', index_col=0)
print(dataframeCarga)