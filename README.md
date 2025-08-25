# Práctica: Minería Ilegal

El presente proyecto tiene como finalidad demostrar un flujo sencillo de **ETL y análisis de datos** aplicado al dataset **EVOA** de Datos Abiertos Colombia "https://datos.gov.co/", permitiendo extraer información sobre la explotación ilícita de oro de aluvión, generar estadísticas básicas, visualizar resultados y aplicar un modelo de **Machine Learning** introductorio.

### Integrantes: Juan José Tellez, Carlos Enrique Guillent

### Grupo: 4

### ¿Qué hace?

1. **Conecta** a la API pública de datos.gov.co (recurso `g48d-yu62`).
2. **Extrae** todos los registros (con paginación automática).
3. **Limpia/transforma** columnas numéricas (año y hectáreas).
4. **Guarda** los datos limpios en `data/mineria_ilegal.csv`.
5. **Analiza** : top 10 departamentos por hectáreas de explotación ilícita.
6. **Visualiza** : genera `data/top10_ilicita.png` (gráfico de barras).
7. **ML** : entrena una **regresión lineal** que intenta predecir hectáreas ilícitas usando otras variables del dataset y muestra el **R²** de prueba.

## Requisitos

* **Python** 3.12+
* **Poetry** (gestor de dependencias)
  * macOS: `brew install poetry`

### Clonar el repositorio:

**git clone** https://github.com/cariuss/TELLEZ-GUILLENT-PRACTICA-I.git

**cd** TELLEZ-GUILLENT-PRACTICA-I

### Instalar dependencias

**poetry** install

### **Ejecutar el proyecto**

**poetry run python** practica_1.py (contiene el main de ejecución)
