# Módulo de ingestión de datos para Biospace
import requests
import os
from utils.logger import logger
from backend.config import Config

class DataIngestion:
    def __init__(self):
        self.base_url = Config.OSDR_API_BASE_URL
        self.api_key = Config.OSDR_API_KEY

    def fetch_experiment_data(self, experiment_id):
        """
        Obtiene datos de un experimento específico desde la API de NASA OSDR.
        :param experiment_id: Identificador del experimento a consultar.
        :return: Datos del experimento en formato JSON o None si falla la solicitud.
        """
        endpoint = f"{self.base_url}/{experiment_id}"
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()
            logger.info(f"Datos obtenidos para el experimento {experiment_id}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al obtener los datos del experimento {experiment_id}: {e}")
            return None

# Ejemplo de uso
if __name__ == "__main__":
    data_ingestion = DataIngestion()
    experiment_data = data_ingestion.fetch_experiment_data("OSD-379")
    if experiment_data:
        print(experiment_data)