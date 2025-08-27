# Práctica: Minería Ilegal

Este proyecto tiene como finalidad demostrar un flujo sencillo de ETL y análisis de datos aplicado al dataset EVOA de Datos Abiertos Colombia
, permitiendo extraer información sobre la explotación ilícita de oro de aluvión, generar estadísticas básicas, visualizar resultados y aplicar un modelo introductorio de Machine Learning con TensorFlow.

## Integrantes

- Juan José Tellez

- Carlos Enrique Guillent

  **Grupo 4**

## 🚀 ¿Qué hace este proyecto?

Conecta a la API pública de datos.gov.co (recurso g48d-yu62).

Extrae los registros (con paginación automática).

Limpia y transforma las columnas relevantes.

Genera estadísticas básicas, como el Top 10 de departamentos con mayor explotación ilícita.

Visualiza resultados en gráficos con Matplotlib.

Entrena un modelo sencillo de regresión lineal con TensorFlow, mostrando la evolución del loss y métricas de evaluación (MSE y R²).

## 📋 Requisitos

Python 3.13 o superior

[Poetry](https://python-poetry.org/) 1.8+

Git

⚙️ Instalación

Clonar el repositorio y entrar a la carpeta:

``` bash
git clone https://github.com/cariuss/TELLEZ-GUILLENT-PRACTICA-I.git
cd TELLEZ-GUILLENT-PRACTICA-I
```

Instalar dependencias con Poetry:

``` bash
poetry install
```

Registrar el kernel de Jupyter:

```bash
poetry run python -m ipykernel install --user --name=tellez-guillent-practica-i
```

## 📓 Ejecutar el Notebook

Iniciar Jupyter:

```bash
poetry run jupyter notebook
```

Abrir el archivo:

> Analisis-Mineria-Ilegal.ipynb

Seleccionar el kernel:

> tellez-guillent-practica-i

## 📊 Resultados esperados

Gráfico con el Top 10 de departamentos.

Entrenamiento de modelo mostrando la evolución de la pérdida (loss) por épocas.

Métricas de evaluación: Error cuadrático medio (MSE) y Coeficiente de determinación (R²).

Visualización de predicciones vs valores reales en un gráfico de dispersión.

## 📚 Referencias

Dataset: [Explotación de oro de aluvión - EVOA](https://www.datos.gov.co/resource/g48d-yu62.json)

Chollet, François. Deep Learning with Python. 2nd Edition, Manning.
