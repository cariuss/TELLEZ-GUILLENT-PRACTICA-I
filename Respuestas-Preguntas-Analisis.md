# Cuestionario de la actividad

## 1.⁠ ⁠¿Cómo se llevó a cabo el proceso?

El proceso se inició conectando a la API pública de Datos Abiertos de Colombia para obtener el dato del dataset EVOA. Hecho eso, realizamos una limpieza de datos, convirtiendo a numéricas las columnas de interés y eliminando registros incompletos.
Con la información lista, creamos estadísticas básicas tales como el Top 10 de departamentos con más explotación ilegal y lo representamos en un gráfico de barras. Por último, entrenamos un modelo de regresión lineal simple con TensorFlow, a fin de intentar predecir las hectáreas de explotación ilegal a partir de variables conexas.

## 2.⁠ ⁠¿Qué tipo de resultados se pueden obtener?

Los resultados demuestran claramente que Antioquia y Chocó concentran la mayor cantidad de extracción ilegal de oro aluvional.
En sentido opuesto, el Machine Learning model también pudo ajustarse de manera básica a los datos, con métricas que aunque no son perfectas demuestran que hay alguna relación entre las variables.

## 3.⁠ ⁠¿Qué tipo de tensores se utilizaron en el ejercicio?

Se usaron en su mayoría tensores de tipo float32 en matrices (2D) y vectores, que eran las representaciones numéricas de los valores de las características (X) y del objetivo (y). Se utilizaron estos tensores en las operaciones de entrenamiento de TensorFlow.

## 4.⁠ ⁠¿Qué bibliotecas de Python se usaron en el ejercicio?

Pandas → para manejar los datos.

NumPy → para procesar números y métricas de evaluación.

Matplotlib → para las gráficas.

Requests → para obtener la inforamción del api de datos abiertos.

TensorFlow → para construir y entrenar el modelo de Machine Learning.

## 5.⁠ ⁠¿Es el proceso para crear el ejercicio del libro igual que usamos con la práctica? Justifique su respuesta

No exactamente. El libro propone un ejemplo de introducción con datos sintéticos con imágenes para que aparezca cómo trabaja el flujo de Machine Learning.
En nuestro ejemplo, aplicamos lógica de extracción, preparación y entrenamiento, con un conjunto de datos real que requiere pasos adicional de limpieza y validación. La variación principal es el tipo de información que se analiza y la consistencia, varianza y dimensionalidad de los datos que encontramos para la práctica.

## 6.⁠ ⁠Conclusiones relacionadas con aprendizaje profundo

Trabajar con datos reales siempre significa tener un proceso de limpieza y transformación antes de entrenar.

Aunque los modelos sencillos como la regresión lineal pueden no tener gran precisión, permiten entender la relación entre variables y sentar la base para aplicar redes neuronales más complejas en el futuro.

TensorFlow facilita el manejo de tensores y la optimización del entrenamiento, mostrando en la práctica cómo funciona el cálculo de gradientes.
