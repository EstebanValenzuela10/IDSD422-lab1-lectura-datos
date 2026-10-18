# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

library(readr)
ventas <- read_csv("data/ventas.csv")

str(ventas)

# Crear una nueva columna llamada ticket:
ventas$ticket <- ventas$ventas / ventas$clientes
head(ventas)

# Venta promedio por sucursal
mean(ventas$ventas)

# Ticket Promedio:
mean(ventas$ticket)

# Sucursal con mayor venta:
sucursal_mas_ventas <- ventas$sucursal[which.max(ventas$ventas)]
cat("La sucursal con mas ventas es:", sucursal_mas_ventas)

# Sucursal con menor venta:
sucursal_menos_ventas <- ventas$sucursal[which.min(ventas$ventas)]
cat("La sucursal con menos ventas es: " ,sucursal_menos_ventas)

# Región con mayor venta total:
ventas_por_region <- aggregate(ventas ~ region, data = ventas, sum)
cat("La region con mayor venta total es: ", ventas_por_region$region[which.max(ventas_por_region$ventas)])


