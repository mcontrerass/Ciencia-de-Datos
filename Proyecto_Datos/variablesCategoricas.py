import pandas as pd

fichero = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/precios_coches.csv'

datos = pd.read_csv(fichero)
print(datos.columns)
print(datos['Fuel_Type'])

# Transformar variables categóricas en dummies
columna_dummies = pd.get_dummies(datos['Fuel_Type'])
print(columna_dummies)

datos_dummies = pd.get_dummies(datos, columns=['Fuel_Type'])
print(datos.head())
print('='*40)
print('='*40)
print(datos_dummies.head())