# 🌍 Predicción de Sismos con Deep Learning

Sistema de predicción de actividad sísmica basado en **redes neuronales profundas (CNN y LSTM)**, desarrollado para el análisis de patrones espaciales y temporales en datos sísmicos reales.

---

## 📌 Descripción

Este proyecto implementa modelos de **Deep Learning** para la predicción del comportamiento sísmico utilizando datos reales recolectados por el **CENAIS (Centro Nacional de Investigaciones Sismológicas)**.

El objetivo principal es analizar series de tiempo sísmicas y detectar patrones que permitan anticipar posibles eventos o comportamientos relevantes.

El sistema forma parte de una práctica académica en el área de **Ingeniería Informática**, enfocado en el uso de inteligencia artificial aplicada a fenómenos naturales.

---

## 🚀 Características

- 🌍 Análisis de datos sísmicos reales  
- 🧠 Implementación de modelos CNN y LSTM  
- 📊 Procesamiento de series de tiempo  
- 📈 Visualización de resultados  
- ⚡ Entrenamiento y evaluación de modelos  
- 🗂️ Organización modular del proyecto  

---

## 🧠 Modelos Implementados

### 🔹 CNN (Red Neuronal Convolucional)

Modelo enfocado en la detección de patrones espaciales dentro de los datos.

**Arquitectura:**
- Conv1D  
- MaxPooling1D  
- Dropout  
- Flatten  
- Dense  

---

### 🔹 LSTM (Long Short-Term Memory)

Modelo especializado en el análisis de dependencias temporales en series de tiempo.

**Arquitectura:**
- LSTM (con retorno de secuencias)  
- Dropout  
- LSTM final  
- Capa Dense de salida  

---

## 🛠️ Tecnologías utilizadas

- **Python** → Lenguaje principal  
- **TensorFlow / Keras** → Deep Learning  
- **Pandas & NumPy** → Manipulación de datos  
- **Matplotlib** → Visualización  
- **Scikit-learn** → Preprocesamiento  

---

## 📂 Estructura del proyecto

```
prediccion_sismos/
│
├── 📁 dataset/
│ └── sismos.csv
├── 📁 doc/
│ └── informe_practica.pdf
├── 📁 graficos/
│ ├── modelo_cnn_resultado.png
│ └── modelo_lstm_resultado.png
├── 📁 models/
│ ├── modelo_cnn.h5
│ └── modelo_lstm.h5
├── 📁 src/
│ └── entrenar_modelos.py
└── README.md
```

---

## ⚙️ Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tuusuario/prediccion_sismos.git
cd prediccion_sismos
```
Crear entorno virtual (opcional pero recomendado):
```
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
```
Instalar dependencias:
```
pip install -r requirements.txt
```
---

## ▶️ Ejecución

Entrenar los modelos:
```
python src/entrenar_modelos.py
```
---

## 📊 Resultados

El proyecto incluye visualizaciones comparativas del desempeño de los modelos:

- 📈 Resultados de CNN
- 📉 Resultados de LSTM

Los modelos entrenados se almacenan en la carpeta /models.

---

## 💡 Funcionamiento

El sistema realiza:

- 📥 Carga de datos sísmicos
- 🧹 Preprocesamiento y normalización
- 🧠 Entrenamiento de modelos
- 📊 Evaluación de resultados
- 💾 Guardado de modelos entrenados
- 📈 Mejoras futuras
- 🔍 Optimización de hiperparámetros
- 🤖 Implementación de modelos híbridos
- 📡 Integración con datos en tiempo real
- ☁️ Despliegue en la nube
- 📊 Dashboard interactivo
- 🔁 Ramas del repositorio
```
develop → Desarrollo activo
principal → Versión estable
```
---

## ⚠️ Nota

Este proyecto es de carácter académico y experimental, enfocado en el aprendizaje y aplicación de técnicas de inteligencia artificial en el análisis de datos sísmicos.

---

## 👨‍💻 Autor

Adaptado y presentado por **Isai Reyes Peña**
