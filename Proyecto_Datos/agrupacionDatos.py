import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

fichero = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/precios_coches.csv'

datos = pd.read_csv(fichero)

print(datos.columns)
titulos_cabecera = ['indice','nombre','localizacion','año','kilometros recorridos','combustible','transmision','tipo propietario','kilometraje','motor','potencia','asientos','precio']
datos.columns = titulos_cabecera
print(datos.head())
print(datos.columns)
print(datos.dtypes)

# Visualización en gráfico
intervalo = np.linspace(min(datos['kilometros recorridos']), max(datos['kilometros recorridos']), 4)
nombre_grupos = ['pocos', 'normal', 'muchos']
datos['kilometros agrupados'] = pd.cut(datos['kilometros recorridos'], intervalo, labels=nombre_grupos, include_lowest=True)
print(datos['kilometros agrupados'])
plt.hist(datos['kilometros recorridos'], bins=intervalo, rwidth=0.9, color='#999')
plt.title('Histograma Kilómetros Recorridos')
plt.xlabel('Kilómetros')
plt.ylabel('Frecuencia')
plt.show() 