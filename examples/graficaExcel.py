import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo Excel proporcionado
archivo_excel = 'bourdain_travel_places (1).xlsx'
df = pd.read_excel(archivo_excel)

# Contar la cantidad de visitas a cada coordenada (agrupando por 'title (coordenadas de la región)')
df_visitas_coordenadas = df['title (coordenadas de la región)'].value_counts()

# Crear la gráfica
plt.figure(figsize=(12, 6))
df_visitas_coordenadas.plot(kind='bar', color='teal')
plt.title('Lugares Visitados por Anthony Bourdain (Basado en Coordenadas)', fontsize=16)
plt.xlabel('Coordenadas de la Región', fontsize=14)
plt.ylabel('Cantidad de Visitas', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()

# Mostrar la gráfica
plt.show()

# Guardar la gráfica en un archivo de imagen
plt.savefig('grafica_lugares_visitados.png')