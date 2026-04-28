import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv1D, MaxPooling1D, Flatten, LSTM, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Cargar los datos
def cargar_datos(ruta_csv):
    df = pd.read_csv(ruta_csv)
    return df

# Preprocesamiento de los datos
def preprocesar_datos(df, secuencia=50):
    scaler = MinMaxScaler()
    datos_normalizados = scaler.fit_transform(df.values)
    
    X, y = [], []
    for i in range(secuencia, len(datos_normalizados)):
        X.append(datos_normalizados[i-secuencia:i])
        y.append(datos_normalizados[i, 0])  # Asumimos que queremos predecir la primera columna (por ejemplo, magnitud)

    X, y = np.array(X), np.array(y)
    return X, y, scaler

# Modelo CNN
def construir_modelo_cnn(input_shape):
    modelo = Sequential([
        Conv1D(64, kernel_size=3, activation='relu', input_shape=input_shape),
        MaxPooling1D(pool_size=2),
        Dropout(0.3),
        Flatten(),
        Dense(50, activation='relu'),
        Dense(1)
    ])
    modelo.compile(optimizer='adam', loss='mse')
    return modelo

# Modelo LSTM
def construir_modelo_lstm(input_shape):
    modelo = Sequential([
        LSTM(64, return_sequences=True, input_shape=input_shape),
        Dropout(0.2),
        LSTM(32),
        Dropout(0.2),
        Dense(1)
    ])
    modelo.compile(optimizer='adam', loss='mse')
    return modelo

# Entrenamiento y predicción
def entrenar_y_predecir(X, y, modelo, nombre_modelo="modelo"):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    historia = modelo.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.1, verbose=1)

    predicciones = modelo.predict(X_test)

    plt.figure(figsize=(10,4))
    plt.plot(y_test, label="Real")
    plt.plot(predicciones, label="Predicción")
    plt.title(f"Resultados del modelo {nombre_modelo}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{nombre_modelo}_resultado.png")
    plt.close()

    modelo.save(f"{nombre_modelo}.h5")
    return historia, predicciones

# Ejecutar todo
def main():
    ruta_csv = "dataset/sismos.csv"  # Asegúrate de que el archivo esté en esta ruta
    df = cargar_datos(ruta_csv)

    X, y, scaler = preprocesar_datos(df)

    print("Entrenando modelo CNN...")
    modelo_cnn = construir_modelo_cnn(X.shape[1:])
    entrenar_y_predecir(X, y, modelo_cnn, "modelo_cnn")

    print("Entrenando modelo LSTM...")
    modelo_lstm = construir_modelo_lstm(X.shape[1:])
    entrenar_y_predecir(X, y, modelo_lstm, "modelo_lstm")

if __name__ == "__main__":
    main()
