# Algo de estadistica descriptiva 

import numpy as np 
from scipy import stats 
import pandas as pd 

np.random.seed(21357) # para poder replicar el random

datos = np.random.randn(5, 4) # datos normalmente distribuidos
print(datos)

print(np.mean(datos))
print(datos.mean(axis=1)) # media aritmetica de cada fila
print(datos.mean(axis=0)) # media aritmetica de cada columna

# mediana
print(np.median(datos)) 
# Desviación estandar 
print(np.std(datos))

# varianza
print(np.var(datos)) 

# moda
print(stats.mode(datos)) # Calcula la moda de cada columna y la frecuencia

#correlacion
print(np.corrcoef(datos)) # Crea matriz de correlación.

# calculando la correlación entre dos vectores.
print(np.corrcoef(datos[0], datos[1]))

# covarianza
print(np.cov(datos)) # calcula matriz de covarianza


# covarianza de dos vectores
print(np.cov(datos[0], datos[1]))

# usando pandas
dataframe = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'], 
                        columns=['col1', 'col2', 'col3', 'col4'])
print(dataframe)

# resumen estadistadistico con pandas
print(dataframe.describe())

# sumando las columnas
print(dataframe.sum())

# sumando filas
print(dataframe.sum(axis=1))

# media aritmetica de cada columna con pandas
print(dataframe.mean())

