import pandas as pd
from sklearn.neural_network import MLPClassifier

# Cargar los datos desde un archivo Excel
data = pd.read_excel('data.xlsx')

# Supón que 'X1', 'X2' son características y 'Y' es la clase
X = data[['X1', 'X2']]  # Reemplaza con las columnas relevantes
y = data['Y']            # Asegúrate de que 'Y' sea la columna de clase

# Crear y entrenar el modelo de red neuronal
model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=1000)
model.fit(X, y)

# Realizar predicciones
y_pred = model.predict(X)

# Mostrar resultados
print(f'Predicciones: {y_pred}')

