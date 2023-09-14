from sklearn.tree import DecisionTreeClassifier
from joblib import dump
from sklearn.model_selection import train_test_split
import os
import pandas as pd

# Importar las bibliotecas necesarias para trabajar con GCP
from google.cloud import storage

# Crea un cliente de almacenamiento GCS
storage_client = storage.Client()

# Ubicación del archivo CSV en GCS
gcs_csv_uri = 'gs://productivizacion_modelo_ml_bucket/iris_dataset.csv'

# Lee el archivo CSV directamente desde GCS a un DataFrame de Pandas
df = pd.read_csv(gcs_csv_uri, sep=';')

# Separa tus datos en características (X) y etiquetas (y)
X = df.drop('target', axis=1)
y = df['target']

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define y entrena tu modelo en el conjunto de entrenamiento
skmodel = DecisionTreeClassifier()
skmodel.fit(X_train, y_train)

# Evalúa el modelo en el conjunto de prueba (calcula la precisión)
accuracy = skmodel.score(X_test, y_test)
print(f'Precisión del modelo en el conjunto de prueba: {accuracy:.2f}')

# Guarda el modelo entrenado en un archivo local
dump(skmodel, "model.joblib")

# Sube el modelo entrenado a GCS
bucket = storage_client.get_bucket("productivizacion_modelo_ml_bucket")
model_blob = bucket.blob("model.joblib")
model_blob.upload_from_filename("model.joblib")

print("Modelo entrenado guardado en GCS.")

