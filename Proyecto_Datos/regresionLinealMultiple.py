import moduloDatos as md
import matplotlib.pyplot as plt
import pandas as pd

# Carga de datos
ruta = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/'
fichero = 'datosModificados.csv'
datos = md.cargaDatos(ruta, fichero, ',')
#print(datos.head())

# Columna índice
datos.set_index('indice', inplace=True)
#print(datos.head())

# Columnas con nulos
columnas_nulos = [ col for col in datos.columns if datos[col].isnull().any()]
print(columnas_nulos)

# Columnas
print(md.columnas(datos))

# Hot encoding
datos_dummies = md.obtenerDummiesA(datos, 'combustible')
print(datos_dummies.head())
datos = pd.concat([datos, datos_dummies], axis=1)
print(datos.columns)

# Normalización
datos = md.normalizaColumna(datos, 'motor')
datos = md.normalizaColumna(datos, 'potencia')

from sklearn.linear_model import LinearRegression

# Crear regresión lineal
lm = LinearRegression()

# Definir variables predictoras y variable objetivo
x = datos[['motor', 'potencia', 'asientos', 'CNG', 'Diesel', 'LPG', 'Petrol']]
y = datos['precio']
print(x)
print('*'*100)
print(y)

# Entrenamiento o ajuste
lm.fit(x,y)

# Predicción
prediccion = lm.predict(x)
a = lm.intercept_
b = lm.coef_

# Mostrar ecuación
print('*'*100)
print(f'y={a}+{b}*x')
print('*'*100)
print('Predicción')
print(prediccion)
print(y)
print(lm.score(x,y))

# Comparativa
resultado = {'Real':datos['precio'], 'Prediccion':prediccion}
R = pd.DataFrame(data=resultado)
print(R.head())

from sklearn import metrics
ECM = metrics.mean_squared_error(datos['precio'], prediccion)
print(ECM)
r_cuadrado = metrics.r2_score(datos['precio'], prediccion)
print(r_cuadrado)

# Gráfica
# plt.plot(datos['motor'], prediccion, 'r', label='Prediccion')
plt.scatter(datos['motor'], y, label='Datos')
plt.scatter(datos['motor'], prediccion, c='red', label='Prediccion')
plt.title('Regresion lineal')
plt.xlabel('Motor')
plt.ylabel('Y')
plt.legend()
plt.grid()
plt.show()