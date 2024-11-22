from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Cargar datos Iris
data = load_iris()
X, y = data.data, data.target
print(f"DATA: {data.data}")
print(f"TARGET: {data.target}")
# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo
modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)
print("Precisión del modelo:", accuracy_score(y_test, y_pred))

# Visualizar el árbol
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))
plot_tree(modelo, feature_names=data.feature_names, class_names=data.target_names, filled=True)
plt.title("Árbol de Decisión - Clasificación Iris")
plt.show()

