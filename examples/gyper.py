import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar el archivo Excel
file_path = "Hypercars.xlsx"
data = pd.ExcelFile(file_path)

# Leer la hoja "Hyper Cars 2019"
df = data.parse('Hyper Cars 2019')

# Seleccionar columnas relevantes y limpiar datos
columns_of_interest = [
    "Hypercars", "Motor", "Caballos de fuerza",
    "Velocidad maxima (km/h)", "Precio", "Origen", "Transmision"
]
df = df[columns_of_interest].copy()

# Renombrar columnas para claridad
df.columns = [
    "Modelo", "Motor", "Caballos_de_fuerza", 
    "Velocidad_maxima_kmh", "Precio", "Origen", "Transmision"
]

# Limpiar datos de "Precio" (eliminar símbolos y convertir a numérico)
df["Precio"] = df["Precio"].str.replace(r"[^\d]", "", regex=True).astype(float)

# Análisis descriptivo
print("Descripción de los datos:")
print(df.describe())

# Visualización: Precio vs Caballos de fuerza
sns.scatterplot(data=df, x="Caballos_de_fuerza", y="Precio", hue="Origen", palette="tab10")
plt.title("Precio vs Caballos de Fuerza")
plt.xlabel("Caballos de Fuerza (HP)")
plt.ylabel("Precio (USD)")
plt.show()

# Visualización: Precio vs Velocidad máxima
sns.scatterplot(data=df, x="Velocidad_maxima_kmh", y="Precio", hue="Origen", palette="tab10")
plt.title("Precio vs Velocidad Máxima")
plt.xlabel("Velocidad Máxima (km/h)")
plt.ylabel("Precio (USD)")
plt.show()

# Distribución de motores
sns.countplot(data=df, y="Motor", palette="viridis")
plt.title("Distribución por Tipo de Motor")
plt.xlabel("Cantidad")
plt.ylabel("Tipo de Motor")
plt.show()

# Precio promedio por país de origen
avg_price_by_origin = df.groupby("Origen")["Precio"].mean().sort_values(ascending=False)
sns.barplot(x=avg_price_by_origin.values, y=avg_price_by_origin.index, palette="mako")
plt.title("Precio Promedio por Origen")
plt.xlabel("Precio Promedio (USD)")
plt.ylabel("Origen")
plt.show()

