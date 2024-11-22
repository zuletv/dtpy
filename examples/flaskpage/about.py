import pandas as pd
import matplotlib.pyplot as plt


# Cargar el archivo Excel
archivo_excel = 'NASCAR.xlsx'  # Cambia esto si el archivo está en otra ubicación
df = pd.read_excel(archivo_excel)


# 1. Cantidad total de puntos por cada fabricante
points_by_manufacturer = df.groupby('MFR')['Points'].sum()


# 2. Piloto con el mayor puntaje acumulado en la temporada
top_driver = df.loc[df['Acumulado'].idxmax()]


# 3. Promedio de puntos obtenidos por los pilotos
average_points = df['Points'].mean()


# 4. Cantidad total de puntos por piloto
points_by_driver = df.groupby('Driver')['Points'].sum()


# 5. Número de pilotos diferentes que han ganado al menos una carrera
drivers_with_wins = df[df['Wins'] > 0]['Driver'].nunique()


# Mostrar resultados calculados
print("Cantidad total de puntos por fabricante:\n", points_by_manufacturer)
print("\nPiloto con el mayor puntaje acumulado en la temporada:\n", top_driver)
print("\nPromedio de puntos obtenidos por los pilotos:\n", average_points)
print("\nCantidad total de puntos por piloto:\n", points_by_driver)
print("\nNúmero de pilotos diferentes que han ganado al menos una carrera:\n", drivers_with_wins)


# Graficar resultados


# Configuración de subgráficas
fig, axs = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Análisis de Puntos de Pilotos NASCAR', fontsize=18)


# Gráfica de puntos por fabricante
axs[0, 0].bar(points_by_manufacturer.index, points_by_manufacturer.values, color='skyblue')
axs[0, 0].set_title('Cantidad Total de Puntos por Fabricante')
axs[0, 0].set_xlabel('Fabricante')
axs[0, 0].set_ylabel('Total de Puntos')


# Gráfica de puntos por piloto
axs[0, 1].bar(points_by_driver.index, points_by_driver.values, color='salmon')
axs[0, 1].set_title('Cantidad Total de Puntos por Piloto')
axs[0, 1].set_xlabel('Piloto')
axs[0, 1].set_ylabel('Total de Puntos')
axs[0, 1].tick_params(axis='x', rotation=45)


# Gráfica de promedio de puntos por piloto (texto)
axs[1, 0].text(0.5, 0.5, f'Promedio de Puntos por Piloto: {average_points:.2f}',
              ha='center', va='center', fontsize=14)
axs[1, 0].set_axis_off()  # Ocultar ejes


# Gráfica de número de pilotos con al menos una victoria (texto)
axs[1, 1].text(0.5, 0.5, f'Número de Pilotos con al Menos una Victoria: {drivers_with_wins}',
              ha='center', va='center', fontsize=14)
axs[1, 1].set_axis_off()  # Ocultar ejes


# Ajuste de diseño
plt.tight_layout(rect=[0, 0, 1, 0.95])


# Mostrar la gráfica
plt.show()

