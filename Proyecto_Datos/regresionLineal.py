import moduloDatos as md
# Carga de datos
ruta = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/'
fichero = 'datosModificados.csv'
datos = md.cargaDatos(ruta, fichero, ',')
print(datos.head())