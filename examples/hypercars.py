import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel
archivo_excel = 'Hypercars.xlsx'  # Cambia esto por el nombre de tu archivo
df = pd.read_excel(archivo_excel)

# Mostrar las primeras filas para verificar la estructura
print(df.head())

# Crear la gráfica con varias series
plt.figure(figsize=(12, 8))

# Suponemos que "Mes" es el eje X, y graficamos "Ventas1", "Ventas2", "Ventas3"
plt.plot(df['Transmision'], marker='o', linestyle='-', label='Transmision', color='b')

plt.plot(df['Caballos de fuerza'], marker='s', linestyle='-', label='Caballos de fuerza', color='g')
plt.plot(df['Velocidad maxima (km/h)'], marker='^', linestyle='-', label='Velocidad maxima (km/h)', color='r')

# Añadir título y etiquetas
plt.title('Transmision', fontsize=16)
plt.xlabel('Hypercars', fontsize=14)
plt.ylabel('Velocidad maxima (km/h)', fontsize=14)
plt.xticks(rotation=45)  # Rotar las etiquetas del eje X si es necesario

# Añadir una leyenda para identificar cada línea
plt.legend()

# Guardar la gráfica en un archivo (en este caso, PNG)
plt.savefig('grafica_comparacion_ventas.png')
# Mostrar la gráfica
plt.show()
