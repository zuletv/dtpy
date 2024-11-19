import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, plot_tree
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
# Datos ficticios
data = {
    "Tamaño_casa": [50, 60, 70, 80, 100, 120, 150],
    "Precio_casa": [100, 120, 140, 160, 200, 240, 300]
}
df = pd.DataFrame(data)

# Separar características y variable objetivo
X = df[["Tamaño_casa"]]
y = df["Precio_casa"]

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear modelo
modelo = DecisionTreeRegressor(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)
print("Error cuadrático medio:", mean_squared_error(y_test, y_pred))

# Visualizar el árbol
plt.figure(figsize=(10, 6))
plot_tree(modelo, feature_names=["Tamaño_casa"], filled=True)
plt.title("Árbol de Decisión - Regresión Precio de Casa")
plt.show()

