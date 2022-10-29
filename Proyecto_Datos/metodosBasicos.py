import pandas as pd
import numpy as np

fichero = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/precios_coches.csv'
#datos = pd.read_csv(fichero, header=None)
datos = pd.read_csv(fichero)

print(datos.dtypes)
print(datos.describe())
print(datos.describe(include='all'))
print(datos.info())

# Preprocesamiento de datos
print(datos['Seats'].head(5))
datos['Seats'] = datos['Seats'] + 1
print(datos['Seats'].head(5))

# Sustituir valores faltantes
print(datos.describe())
#datos.dropna(subset=['Seats'],axis=0,inplace=True) # Elimina filas (axis=0) que en la columna 'Seats' tienen valor 'nan'
#datos.replace(np.nan,'nulo')
media_asientos = datos['Seats'].mean()
print(media_asientos)
datos['Seats'].replace(np.nan,media_asientos,inplace=True) # Reemplaza valores 'nan' por la media en la columna 'Seats'
print(datos.describe())
print(datos['Seats']>5)