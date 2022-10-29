import pandas as pd

fichero = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/precios_coches.csv'
#datos = pd.read_csv(fichero, header=None)
datos = pd.read_csv(fichero)

#datos = pd.read_json(fichero)
#datos = pd.read_excel(fichero)
#datos = pd.read_sql(fichero)

#print(datos)
print(datos.head(5))
print('*'*125)
print(datos.tail(5))
print(datos.columns)
titulos_cabecera = ['indice','nombre','localización','año','kilómetros recorridos','combustible','transmisión','tipo propietario','kilometraje','motor','potencia','asientos','precio']
datos.columns = titulos_cabecera
print(datos.head(5))
print(datos.columns)

# Exportar datos
fichero = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/precios_cochesCopia.csv'
datos.to_csv(fichero)

# Otros formatos de archivos
#datos.to_json(fichero)
#datos.to_excel(fichero)
#datos.to_sql(fichero)