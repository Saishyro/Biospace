import requests
import logging

# Configurar el registro
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, base_url, headers=None):
        self.base_url = base_url
        self.headers = headers if headers else {}

    def get(self, endpoint, params=None):
        """
        Método para realizar una solicitud GET a la API externa.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            logger.info(f"GET {url} - Status Code: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error en la solicitud GET: {e}")
            return None

    def post(self, endpoint, data=None):
        """
        Método para realizar una solicitud POST a la API externa.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            logger.info(f"POST {url} - Status Code: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error en la solicitud POST: {e}")
            return None

    def put(self, endpoint, data=None):
        """
        Método para realizar una solicitud PUT a la API externa.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.put(url, headers=self.headers, json=data)
            response.raise_for_status()
            logger.info(f"PUT {url} - Status Code: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error en la solicitud PUT: {e}")
            return None

    def delete(self, endpoint):
        """
        Método para realizar una solicitud DELETE a la API externa.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
            logger.info(f"DELETE {url} - Status Code: {response.status_code}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error en la solicitud DELETE: {e}")
            return None

# Ejemplo de uso del cliente de API
if __name__ == "__main__":
    base_url = "https://osdr.nasa.gov/osdr"
    headers = {"Content-Type": "application/json"}
    api_client = APIClient(base_url, headers)

    # Solicitar datos de un experimento
    experiment_data = api_client.get("data/osd/files/12345")
    if experiment_data:
        print(experiment_data)