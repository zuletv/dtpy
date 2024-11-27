from flask import Flask, render_template
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
app = Flask(__name__)

@app.route("/about")
def sobremi():
    return "<marquee><h1>Aviel Arturo Piña Sosa 369123, Diana Zuleth Talamantes Velazquez 369467, Laura Fernanda Zazueta Zayola 369278 </h1></marquee>"

@app.route("/arbol-3")
def arbol():
    # Cargar datos desde un archivo Excel
    try:
        df = pd.read_excel('hypercarss.xlsx')
    except FileNotFoundError:
        return "Error: El archivo 'hypercarss.xlsx' no se encuentra."

    # Renombrar columnas motor y transmisión
    df.rename(columns={'Motor': 'Motor1', 'Transmision': 'Transmision1'}, inplace=True)

    # Previsualizar los datos
    df.fillna(0, inplace=True)

    # Dividir características y variable objetivo
    try:
        X = df[["Caballos de fuerza"]]
        y = df["Hypercars"]
    except KeyError as e:
        return f"Error: No se encontró la columna {e} en el archivo Excel."

    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Crear y entrenar el modelo
    modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
    modelo.fit(X_train, y_train)

    # Realizar predicciones
    y_pred = modelo.predict(X_test)

    # Evaluar el modelo
    precision = accuracy_score(y_test, y_pred)
    print("Precisión del modelo:", precision)

    # Visualizar el árbol de decisión
    plt.figure(figsize=(12, 8))
    plot_tree(modelo, feature_names=X.columns, class_names=modelo.classes_, filled=True)
    plt.title("Árbol de Decisión - Clasificación")

    # Guardar la gráfica en un archivo
    os.makedirs('./static/images', exist_ok=True)  # Crear directorio si no existe
    plt.savefig('./static/images/graficaarbol.png')
    plt.close()

    return render_template("arboles.html", precision=precision)

if __name__ == "__main__":
    app.run(debug=True)

