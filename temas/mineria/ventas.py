import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar datos
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
data = pd.read_csv(url)

# Análisis básico
print(data.info())
print(data.describe())

# Visualización: Relación entre total_bill y tip
sns.scatterplot(data=data, x="total_bill", y="tip", hue="day")
plt.title("Propinas vs Total de la Cuenta")
plt.xlabel("Total de la Cuenta")
plt.ylabel("Propina")
plt.show()

# Análisis por día
sns.boxplot(data=data, x="day", y="total_bill", palette="coolwarm")
plt.title("Distribución de Ventas por Día")
plt.show()

