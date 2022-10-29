#from gettext import npgettext
#from xml.etree.ElementInclude import include
import pandas as pd
import numpy as np

def cargaDatos(ruta, fichero, separador=','):
    datos = pd.read_csv(ruta+fichero, sep=separador)
    return datos

def columnas(datos):
    return datos.columns

def guardaDatos(datos, ruta, fichero):
    datos.to_csv(ruta+fichero)
    return True

def cambiaColumnas(datos, columnas):
    datos.columns = columnas
    return datos

def renombrarColumna(datos, cambio):
    datos.rename(columns=cambio, inplace=True)
    return datos

def estadisticas(datos, tipo='n'):
    """tipo numérico o todos"""
    if tipo=='n':
        return datos.describe()
    else:
        return datos.describe(include='all')

def reemplazarNulos(datos, columna):
    media = datos[columna].mean()
    datos[columna].replace(np.nan, media, inplace=True)
    return datos    

def cambiaTipo(columna, tipo='float64'):
    #columna = columna.astype(tipo)
    columna = pd.to_numeric(columna, errors='coerce')
    return columna

def normalizaColumna(datos, columna): # min y valor anterior
    datos[columna] = datos[columna]/datos[columna].max()
    return datos

def obtenerDummiesA(datos, columna):
    datos = pd.get_dummies(datos[columna])
    return datos

def obtenerDummiesB(datos, columna):
    datos = pd.get_dummies(datos,columns=[columna])
    return datos

if __name__ == '__main__':
    ruta = '/home/mcontrerass/Proyectos/Ciencia de Datos/Proyecto_Datos/datos/'
    fichero = 'precios_coches.csv'
    datos = cargaDatos(ruta,fichero)
    print(datos.head(5))

    print(columnas(datos))

    guardaDatos(datos, ruta, 'copia_precios_coches.csv')

    titulos_cabecera = ['indice','nombre','localizacion','año','kilometros recorridos','combustible','transmision','tipo propietario','kilometraje','motor','potencia','asientos','precio']
    cambiaColumnas(datos,titulos_cabecera)
    print(columnas(datos))

    print(estadisticas(datos))
    print(estadisticas(datos,'t'))

    print(reemplazarNulos(datos,'asientos'))

    columna1 = datos['kilometros recorridos']
    columna2 = datos['asientos']

    print('Columnas antes de cambiar tipo')
    print(columna1)
    print(columna2)

    columna1 = cambiaTipo(columna1)
    columna2 = cambiaTipo(columna2, 'int64')

    print('Columnas después de cambiar tipo')
    print(columna1)
    print(columna2)

    datos = renombrarColumna(datos, {'kilometros recorridos':'kilometros'})
    print(datos.columns)

    datos = normalizaColumna(datos, 'kilometros')
    print(datos['kilometros'])