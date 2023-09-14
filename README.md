# Productivización de un Modelo de ML con Vertex AI y Vertex Pipelines en GCP

## Objetivo

El objetivo de este ejercicio es demostrar la capacidad para crear un pipeline de Machine Learning utilizando Vertex AI y Vertex Pipelines en Google Cloud Platform (GCP). Este pipeline abarca desde la obtención de datos desde un bucket de Google Cloud Storage (GCS), la formación de un modelo de ML, hasta la generación de predicciones almacenadas en BigQuery. Además, se aborda la implementación del proceso en un contenedor Docker y la gestión segura de los secretos de autenticación de GCP.

## Pasos a seguir

### 1. Configuración de GCP

Antes de comenzar, asegúrate de tener una cuenta gratuita en Google Cloud Platform (GCP) y configura las credenciales de autenticación en GCP.

### 2. Obtención del Conjunto de Datos

Se utilizo la base de datos iris de la librería sklearn y se almacenó en Google Cloud Storage con el nombre de iris_dataset.csv, si queremos trabajar con otra data
simplemente se carga otra información.

### 3. Creación de un Pipeline en Vertex AI y Vertex Pipelines

El objetivo principal es crear un pipeline de Vertex AI utilizando Vertex Pipelines.

Todo el paso a paso se encuentra en PIPELINE_MODELO_ML\productivizacion_modelo_ml\02_customtrain.ipynb

## 3.1 
Los 3 pasos siguientes se desarrollan dentro de PIPELINE_MODELO_ML\productivizacion_modelo_ml\traincontainer\trainer\train.py

#### - Leer los datos desde el bucket de GCS:

    El primer paso consiste en obtener los datos desde un bucket de Google Cloud Storage (GCS) donde se almacenan los datos necesarios para el 
    entrenamiento y evaluación del modelo. el archivo iris_dataset.csv


#### - Dividir los datos en conjuntos de entrenamiento y prueba:

    Se divide los datos en conjuntos de entrenamiento y prueba para evaluar el rendimiento del modelo.

#### - Entrenar un modelo de Machine Learning:

    Entrenamos un modelo de Machine Learning con lgoritmo de Arboles de decisión utilizando Vertex AI.
    
## 3.2
Los demás pasos siguientes hasta el final se desarrollan dentro de PIPELINE_MODELO_ML\productivizacion_modelo_ml\02_customtrain.ipynb

#### - Generar predicciones utilizando el modelo entrenado:

    Por conveniencia se utiliza la misma data iris_dataset.csv para llevar a producción el modelo entrenado, dentro del pipeline

#### - Almacenar las predicciones en una tabla de BigQuery:

    Las predicciones se almacena dentro de la tAbla de BigQuery

### 4. Contenedor Docker

Al principio se crea contendor Docker dentro del archivo  PIPELINE_MODELO_ML\productivizacion_modelo_ml\02_customtrain.ipynb, con las dependencias necesarias.

### 5. Gestión de Secretos

Finalmente se realiza un ejemplo de uso de secret manager dentro del archivo  PIPELINE_MODELO_ML\productivizacion_modelo_ml\02_customtrain.ipynb, con las credenciales necesarias.

