# leer_csv.py — Cargar el reporte CSV del ERP (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/leer_csv.py

# TODO 1: importa pandas y carga data/ventas.csv en un DataFrame
# TODO 2: imprime las dimensiones (filas, columnas) del DataFrame
# TODO 3: imprime las primeras filas para revisar las columnas

import pandas as pd

# Cargo el csv en un data frame
ventas = pd.read_csv('data/ventas.csv')

# Imprimir las dimenciones
print('Las dimensiones de la tabla es: ',ventas.shape)

# Imprimir las primeras filas
print(ventas.head())

# Imprimir los datos por columna
print('\n Tipos de columna' )
print(ventas.dtypes)