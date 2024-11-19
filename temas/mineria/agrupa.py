from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Datos ficticios
data = {
    "Ingresos": [15, 16, 16, 17, 18, 19, 25, 26, 28, 30],
    "Gasto": [8, 9, 8, 11, 10, 12, 15, 14, 18, 20]
}
df = pd.DataFrame(data)

# Estandarizar datos
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Aplicar K-Means
kmeans = KMeans(n_clusters=2, random_state=0)
df["Cluster"] = kmeans.fit_predict(scaled_data)

# Visualización
plt.scatter(df["Ingresos"], df["Gasto"], c=df["Cluster"], cmap="viridis")
plt.title("Agrupación de Clientes")
plt.xlabel("Ingresos")
plt.ylabel("Gasto")
plt.show()

