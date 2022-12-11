import moduloDatos as md
import matplotlib.pyplot as plt

# Carga de datos
ruta = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/'
fichero = 'datosModificados.csv'
datos = md.cargaDatos(ruta, fichero, ',')
print(datos.head())

# Columna índice
datos.set_index('indice', inplace=True)
print(datos.head())

from sklearn.linear_model import LinearRegression

# Crear regresión lineal
lm = LinearRegression()

# Definir variables predictoras y variable objetivo
x = datos[['motor']]
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

# Visualización
import seaborn as sns
#from seaborn import lmplot
sns.regplot(x='motor', y='precio', data=datos)
plt.show()
sns.lmplot(x='motor', y='precio', data=datos)

# Visualizar residuales, predicción - error
sns.residplot(x='motor', y='precio', color='orange', data=datos)
plt.show()

######################################################################
# Separación en entrenamiento y pruebas
# Definir variables predictoras y variable objetivo
x = datos[['motor']]
y = datos['precio']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=0)
print(x_train)
print('*'*100)
print(y_train)

# Entrenamiento o ajuste
lm.fit(x_train,y_train)

# Predicción
prediccion = lm.predict(x_test)
a = lm.intercept_
b = lm.coef_

# Mostrar ecuación
print('*'*100)
print(f'y={a}+{b}*x')
print('*'*100)
print('Predicción')
print(prediccion)
print(y_test)
print(lm.score(x_train,y_train))

# Visualización
import seaborn as sns
#from seaborn import lmplot
sns.regplot(x='motor', y='precio', data=datos)
plt.show()
sns.lmplot(x='motor', y='precio', data=datos)

# Visualizar residuales, predicción - error
sns.residplot(x='motor', y='precio', color='orange', data=datos)
plt.show()