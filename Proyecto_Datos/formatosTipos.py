import pandas as pd
import numpy as np 

fichero = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/precios_coches.csv'

datos = pd.read_csv(fichero)
print(datos.head())
print(datos.dtypes)

# Cambiar tipo de datos
datos['Unnamed: 0'] = datos['Unnamed: 0'].astype('float64')
print(datos.dtypes)

# Hacer cálculos y ponerlos en otra columna
datos['millas_driven'] = datos['Kilometers_Driven'] * 0.621361
print(datos.head())

# Renombrar columna
datos.rename(columns={'millas_driven':'Millas'}, inplace=True)
print(datos.head())

# Normalizar datos
# min y valor anterior
print(datos[['Millas','Kilometers_Driven',]])
datos['Millas_normalizadas'] = datos['Millas']/datos['Millas'].max()
datos['Kilometros_normalizados'] = datos['Kilometers_Driven']/datos['Kilometers_Driven'].max()
print(datos[['Millas_normalizadas','Kilometros_normalizados']])
# min y max
print(datos[['Millas','Kilometers_Driven',]])
datos['Millas_normalizadas'] = (datos['Millas']-datos['Millas'].min())/(datos['Millas'].max()-datos['Millas'].min())
datos['Kilometros_normalizados'] = (datos['Kilometers_Driven']-datos['Kilometers_Driven'].min())/(datos['Kilometers_Driven'].max()-datos['Kilometers_Driven'].min())
print(datos[['Millas_normalizadas','Kilometros_normalizados']])