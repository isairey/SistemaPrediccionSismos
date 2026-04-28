# prediccion_sismos
# Sistema de Predicción de Sismos con Redes Neuronales

Este proyecto consiste en el entrenamiento de dos modelos de deep learning (CNN y LSTM) para la predicción del comportamiento sísmico. Utiliza datos reales recolectados por el CENAIS y forma parte del informe de Práctica Laboral del tercer año de Ingeniería Informática en la Universidad de Oriente.

---

## 📁 Estructura del Repositorio
📦 nombre-del-repositorio/
├── dataset/
│   └── sismos.csv
├── doc/
│   └── informe_practica.pdf
├── graficos/
│   ├── modelo_cnn_resultado.png
│   └── modelo_lstm_resultado.png
├── models/
│   ├── modelo_cnn.h5
│   └── modelo_lstm.h5
├── src/
│   └── entrenar_modelos.py
├── README.md

---

🧠 Modelos Implementados

🧩 CNN – Red Neuronal Convolucional

Captura patrones espaciales en secuencias de datos sísmicos.

Arquitectura del modelo:

Conv1D

MaxPooling1D

Dropout

Flatten

Dense



🔁 LSTM – Long Short-Term Memory

Aprende dependencias temporales en series de tiempo.

Arquitectura del modelo:

LSTM con retorno de secuencias

Dropout

LSTM final

Dense de salida




---

🛠️ Tecnologías y Herramientas Utilizadas

Lenguaje de programación: Python

Framework de Deep Learning: TensorFlow / Keras

Manipulación y análisis de datos: Pandas, NumPy

Visualización de resultados: Matplotlib

Escalado de datos: Scikit-learn



---

👩‍💻 Autora

Madeley Graham
Estudiante de 3er año de Ingeniería Informática
Universidad de Oriente
Práctica laboral realizada en el CENAIS (Centro Nacional de Investigaciones Sismológicas)
Correo: madeleygraham9@gmail.com


---

🔁 Ramas del Repositorio

develop: Rama principal de desarrollo, donde se integran las funcionalidades.

principal: Rama estable, lista para revisión o entrega académica.
