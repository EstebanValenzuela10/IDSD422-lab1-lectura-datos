# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total


import pandas as pd

ventas = pd.read_csv('data/ventas.csv')

print(ventas.dtypes)

# Creo una nueva columna
# Crea la columna derivada "ticket" = ventas / clientes
ventas["Ticket"] = ventas["ventas"] / ventas["clientes"]
print(ventas.head())

# Venta promedio por sucursal:
print('Venta promedio general por sucursal:')
print(ventas['ventas'].mean())

# Ticket Promedio (ventas totales / clientes totales)
ticket_promedio = ventas['ventas'].sum() / ventas['clientes'].sum()
print('Ticket promedio (ventas totales / clientes totales):')
print(ticket_promedio)

# Sucursal con mayor venta:
print(' Sucursal con mayor venta: ' )
print(ventas.loc[ventas['ventas'].idxmax(), "sucursal"])

# Sucursal con menor venta:
print('\n Sucursal con menor venta: ')
print(ventas.loc[ventas['ventas'].idxmin(), "sucursal"])

# Región con mayor venta total
ventas_por_region = ventas.groupby("region").sum("ventas")
ventas_por_region.head()
print("La región con mayor venta total es:",ventas_por_region['ventas'].idxmax())