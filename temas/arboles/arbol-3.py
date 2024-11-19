import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Cargar datos desde un archivo Excel
ruta_archivo = "ruta_a_tu_archivo.xlsx"  # Cambia esta ruta al archivo correcto
df = pd.read_excel(ruta_archivo)

# Previsualizar los datos
print("Primeras filas de los datos:")
print(df.head())

# Dividir características y variable objetivo
# Asegúrate de ajustar estos nombres según tu archivo
X = df[["Caracteristica1", "Caracteristica2", "Caracteristica3"]]  # Reemplaza con las columnas correctas
y = df["Clase"]  # Columna objetivo o etiqueta

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear y entrenar el modelo
modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)

# Realizar predicciones
y_pred = modelo.predict(X_test)

# Evaluar el modelo
print("Precisión del modelo:", accuracy_score(y_test, y_pred))

# Visualizar el árbol de decisión
plt.figure(figsize=(12, 8))
plot_tree(modelo, feature_names=X.columns, class_names=modelo.classes_, filled=True)
plt.title("Árbol de Decisión - Clasificación")
plt.show()

