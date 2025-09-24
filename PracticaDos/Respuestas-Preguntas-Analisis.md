# Cuestionario de la actividad

## 1. Métricas utilizadas

En la práctica usamos las siguientes métricas:

Accuracy (Exactitud): proporción de aciertos sobre el total de predicciones.

Loss (Binary Crossentropy): mide la diferencia entre las predicciones del modelo y las etiquetas reales.

Curvas de aprendizaje (loss/accuracy en train y validation): permiten ver si hay sobreajuste o subajuste.

Predicciones de prueba: probabilidad asociada a cada clase (positiva/negativa).

## 2. Estructuras de datos de Python utilizadas

Durante el proceso trabajamos con:

Listas (list) → para almacenar frases base y variaciones del dataset.

Diccionarios (dict) → para el vocabulario de Keras (tokenizer.word_index).

Tuplas (tuple) → al momento de combinar frases y etiquetas al generar el dataset.

## 3. Tipos de tensores, ndarrays, Series y/o DataFrames

ndarray de NumPy: generado después de tokenizar y aplicar padding (X_train_pad, X_test_pad).

Tensor de TensorFlow: al entrenar y evaluar el modelo, los arreglos son convertidos en tensores.

Series de pandas: columnas individuales como df["texto"] y df["sentimiento"].

DataFrame de pandas: el dataset completo (df).

## 4. Bibliotecas de datos utilizadas

NumPy → manejo de arreglos numéricos.

Pandas → manipulación de DataFrames (lectura/escritura de JSON y CSV).

Scikit-learn → separación train/test y baseline con regresión logística.

TensorFlow / Keras → definición, entrenamiento y evaluación de redes neuronales recurrentes.

Matplotlib → visualización de métricas (accuracy/loss).

## 5. Descripción del proceso

Generación del dataset sintético: se construyeron 6000 opiniones balanceadas (positivas y negativas), evitando contradicciones y con variaciones realistas en lugar, tiempo y adjetivos.

Preprocesamiento: se cargaron los datos desde JSON, se tokenizó el texto y se aplicó padding para estandarizar la longitud.

Entrenamiento del modelo LSTM:

Se definió una red con capas Embedding, LSTM, Dropout y Dense.

Se entrenó por 5 épocas con un batch size de 64.

Se alcanzó un accuracy en test de 0.9983.

Predicciones: se probaron frases manuales y el modelo predijo de forma correcta la mayoría, con una excepción que permitió analizar OOV tokens y la calibración de umbrales.

## Dificultades encontradas

No encontramos un dataset como tal que representara las opiniones del transporte publico, por lo tanto empleamos data sisntetica que nos permitiera realizar la actividad.
