# Módulo para entrenamiento y predicción de modelos de Machine Learning en Biospace
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from utils.logger import logger

class MLModels:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train_model(self, data: pd.DataFrame, target_column: str):
        """
        Entrena un modelo de Machine Learning para predecir resultados.
        :param data: DataFrame de pandas con los datos procesados.
        :param target_column: Nombre de la columna objetivo para el entrenamiento.
        """
        try:
            # Separar características y objetivo
            X = data.drop(columns=[target_column])
            y = data[target_column]

            # Dividir los datos en conjunto de entrenamiento y prueba
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Entrenar el modelo
            self.model.fit(X_train, y_train)
            logger.info("Modelo entrenado correctamente.")

            # Evaluar el modelo
            y_pred = self.model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            logger.info(f"Precisión del modelo: {accuracy:.2f}")
        except Exception as e:
            logger.error(f"Error al entrenar el modelo: {e}")

    def predict(self, input_data: pd.DataFrame):
        """
        Realiza predicciones usando el modelo entrenado.
        :param input_data: DataFrame con las características para realizar las predicciones.
        :return: Predicciones realizadas por el modelo.
        """
        try:
            predictions = self.model.predict(input_data)
            logger.info("Predicción realizada correctamente.")
            return predictions
        except Exception as e:
            logger.error(f"Error al realizar la predicción: {e}")
            return None

# Ejemplo de uso
if __name__ == "__main__":
    from models.data_processing import DataProcessing
    from models.data_ingestion import DataIngestion

    # Ingesta, procesamiento y entrenamiento del modelo
    data_ingestion = DataIngestion()
    raw_data = data_ingestion.fetch_experiment_data("OSD-379")

    if raw_data:
        data_processing = DataProcessing()
        processed_data = data_processing.clean_data(raw_data)

        if processed_data is not None:
            ml_model = MLModels()
            # Suponiendo que processed_data tiene una columna "target" que queremos predecir
            ml_model.train_model(processed_data, target_column="target")