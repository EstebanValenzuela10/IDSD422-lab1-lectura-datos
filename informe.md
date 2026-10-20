# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 19/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Se recibieron reportes de ventas de una semana en CSV (ERP), JSON (API de fidelización) y Excel (Finanzas). Los tres archivos contienen 5 filas y 4 columnas con la misma información. La venta promedio por sucursal fue 12008 y el ticket promedio fue 38.07. Se recomienda estandarizar el intercambio en CSV y ampliar la observación antes de proyectar resultados.

## 1. ¿Los tres formatos contienen la misma información?

*Carga los tres archivos (CSV, JSON y Excel) en Python y en R, y compara dimensiones y estructura. Completa la tabla:*

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales | 5 | 4 | `pd.read_csv` / `readr::read_csv` |
| JSON | API de fidelización | 5 | 4 | `json.load` + `pd.json_normalize` / `jsonlite::fromJSON` |
| Excel | Consolidado de finanzas | 5 | 4 | `pd.read_excel(..., sheet_name="ventas")` / `readxl::read_excel(sheet = "ventas")` |

Los formatos tienen estructuras internas distintas —texto tabular, lista de diccionarios y libro binario—, pero no cambian el contenido: después de la lectura, las tres tablas tienen las mismas 5 filas y 4 columnas.

## 2. Tipos de datos y calidad

*Inspecciona los tipos que infiere cada lenguaje. Completa la tabla y comenta si los tipos son los esperados para cada variable:*

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | `int64` | `numeric` (`double`) | Importe numérico entero en los valores observados. |
| `clientes` | `int64` | `numeric` (`double`) | Conteo numérico entero en los valores observados. |
| `sucursal` | `str` | `character` | Nombre textual de la sucursal. |
| `region` | `str` | `character` | Región textual; en R se confirmó que es `character`. |

Si `ventas` llegara como texto, el tipo inferido no sería numérico y las sumas, promedios y comparaciones podrían fallar o producir resultados incorrectos. Esto indicaría la necesidad de limpiar y convertir la columna antes del análisis.

## 3. Particularidades técnicas encontradas

- **CSV:** se leyó como una tabla delimitada con `read_csv`/`pd.read_csv`; las columnas de texto quedaron como `character` en R y texto (`str`) en Python.
- **JSON:** llegó como una lista de diccionarios, por lo que en Python se cargó con `json.load` y se aplanó con `pd.json_normalize`; en R `fromJSON` permitió convertirlo a `data.frame`.
- **Excel:** se leyó indicando explícitamente la única hoja, llamada `ventas`; las categóricas conservaron sus tipos textuales.

## 4. Indicadores para la reunión del lunes

*Calcula los indicadores con los datos consolidados y completa la tabla:*

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | 12008 |
| Ticket promedio (ventas ÷ clientes) | 38.07 |
| Sucursal con mayor venta | Guayaquil Centro (15200) |
| Sucursal con menor venta | Cuenca (8540) |
| Región con mayor venta total | Sierra (30860; Costa: 29180) |

## 5. Conclusiones y recomendación

1. Pude leer los tres archivos en Python con pandas, cada uno con su función (read_csv, read_json y read_excel, el json fue aplanado antes de leerlo). Los tres produjeron un DataFrame sin errores de lectura y con los mismos datos, lo que permite trabajar con cualquiera de las tres fuentes.

2. Los tres archivos tienen shape (5, 4), es decir, cinco filas y cuatro columnas. En todos, sucursal y region se leyeron como texto y ventas y clientes como enteros, sin valores faltantes. 

3. La venta promedio por sucursal fue 12 008. El ticket global fue 38,07 por cliente, y por sucursal va de Guayaquil Centro con mayores ventas y Cuenca con menores ventas. La Sierra suma más porque tiene tres sucursales, pero cada sucursal de la Costa vende más en promedio.

**Recomendación para la Gerencia:** Se recomienda que la empresa trabaje con un solo tipo de archivo para que el equipo de BI se le facilite el trabajo y generen reportes de manera más eficiente para la toma de decisiones 