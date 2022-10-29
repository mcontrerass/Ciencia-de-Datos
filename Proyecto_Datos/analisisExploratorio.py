import moduloDatos as md
import matplotlib.pyplot as plt

# Carga de datos
ruta = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/'
fichero = 'precios_coches_copia.csv'
datos = md.cargaDatos(ruta, fichero, ';')
print(datos.head())

# Columna índice
datos.set_index('n', inplace=True)
datos.index.name = 'indice'
print(datos.head())

# Cambio nombre columnas
print(md.columnas(datos))
nombreColumnas = ['nombre','localizacion','año','kilometros recorridos','combustible','transmision','tipo propietario','kilometraje','motor','potencia','asientos','precio']
md.cambiaColumnas(datos,nombreColumnas)
print(md.columnas(datos))

# Estadísticas básicas
print(md.estadisticas(datos))
print('*'*100)
print('*'*100)
print(md.estadisticas(datos, 'all'))

# Valores nulos
datos = md.reemplazarNulos(datos, 'asientos')
print(md.estadisticas(datos))

# Cambio tipo
print(datos['motor'])
print(datos['precio'])
print(datos['potencia'])
datos['motor'] = md.cambiaTipo(datos['motor'])
datos['precio'] = md.cambiaTipo(datos['precio'])
datos['potencia'] = md.cambiaTipo(datos['potencia'])
datos = md.reemplazarNulos(datos, 'motor')
datos = md.reemplazarNulos(datos, 'precio')
datos = md.reemplazarNulos(datos, 'potencia')
print(datos['motor'])
print(datos['precio'])
print(datos['potencia'])
print(datos.info)
print(datos['nombre'].value_counts())

# Visualización de datos en gráfico
#plt.boxplot(datos['precio'])
#plt.title('Precio')
#plt.show()

# Gráfico de dispersión relación entre variables
y = datos['precio']
x = datos['potencia']
plt.scatter(x,y)
plt.title('Potencia / Precio')
plt.xlabel('Potencia')
plt.ylabel('Precio')
plt.show()

x = datos['motor']
plt.scatter(x,y)
plt.title('Motor / Precio')
plt.xlabel('Motor')
plt.ylabel('Precio')
plt.show()

# Mediante coeficiente de correlación y p valor
# Si prox a 1 relación positiva
# Si Prox a -1 relación negativa
# Si prox a 0 sin relación
# p valor
# Si <0.001 fuerte certeza en el resultado
# Si <0.05 moderado
# Si <0.1 baja o débil
# Si >0.1 sin certeza de correlación

from scipy import stats
pearson_coef, p_valor = stats.pearsonr(datos['motor'],datos['precio'])
print(f"El coeficiente de relación de Pearson es: {pearson_coef}")
print(f"El p-valor es: {p_valor}")

columnas = ['nombre','año','kilometros recorridos','motor','potencia','precio']
datos_nuevos = datos[columnas]
print(datos_nuevos.head(10))
datos_agrupados = datos_nuevos.groupby(['año'],as_index=False).mean()
print(datos_agrupados.head(20))

# Guardar datos
fichero = 'datosModificados.csv'
md.guardaDatos(datos, ruta, fichero)