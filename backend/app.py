import json
import requests
from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from models.data_ingestion import DataIngestion
from models.data_processing import DataProcessing
from models.ml_models import MLModels
from models.nlp_processing import NLPProcessor
from models.visualization_data import VisualizationData
from utils.api_client import APIClient
from utils.database import Database
from utils.logger import logger
import logging
from config import Config
from flask_cors import CORS
from data_processing import preparar_datos_para_visualizacion


# Inicializar la aplicación Flask
app = Flask(__name__, static_folder="../frontend", template_folder="../frontend")

CORS(app)

# Inicializar componentes necesarios
data_ingestion = DataIngestion()
data_processing = DataProcessing()
ml_models = MLModels()
nlp_processing = NLPProcessor()
visualization_data = VisualizationData()
database = Database()
api_client = APIClient(base_url=Config.OSDR_API_BASE_URL)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')

# Endpoint para la consulta de datos desde la API de OSDR
# Endpoint para búsqueda de estudios
@app.route('/api/search_experiment/<osd_study_id>', methods=['GET'])
def search_experiment(osd_study_id):
    try:
        # Definir la URL del endpoint de la API pública de OSDR
        osdr_api_url = f"https://osdr.nasa.gov/osdr/data/osd/files/{osd_study_id}"
        
        # Realizar la solicitud GET hacia la API
        response = requests.get(osdr_api_url)
        
        # Manejo de la respuesta
        if response.status_code == 200:
            data = response.json()
            # Enviar los datos obtenidos al frontend (en inglés)
            return jsonify(data)
        else:
            return jsonify({"error": "No se encontraron datos para el experimento solicitado."}), response.status_code

    except Exception as e:
        return jsonify({"error": f"Ocurrió un error al intentar conectar con la API: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

# Endpoint para la visualización de datos
@app.route('/api/visualization/<experiment_id>', methods=['GET'])
def visualize_experiment_data(experiment_id):
    try:
        # Obtener datos del experimento desde la base de datos
        data = database.get_experiment_data(experiment_id)
        # Generar datos para visualización
        visualization = visualization_data.generate(data)
        return jsonify(visualization)
    except Exception as e:
        logger.error(f"Error al visualizar los datos del experimento {experiment_id}: {str(e)}")
        return jsonify({"error": "No se pudo generar la visualización de los datos."}), 500

# Endpoint para entrenamiento y predicción de modelos ML
@app.route('/api/ml/train', methods=['POST'])
def train_ml_model():
    try:
        logger.info("Iniciando proceso de ingesta de datos.")
        # Ingesta de datos
        data = data_ingestion.ingest()
        logger.info("Datos ingresados correctamente.")

        # Procesamiento de datos
        processed_data = data_processing.process(data)
        logger.info("Datos procesados correctamente.")

        # Entrenar modelo
        ml_models.train(processed_data)
        logger.info("Modelo entrenado exitosamente.")

        return jsonify({"message": "Modelo entrenado exitosamente."})
    except Exception as e:
        logger.error(f"Error al entrenar el modelo: {str(e)}")
        return jsonify({"error": "No se pudo entrenar el modelo."}), 500
    
    
# Endpoint para obtener los datos procesados y listos para visualización
@app.route('/api/get_processed_data', methods=['GET'])
def get_processed_data():
    try:
        # Obtener los datos del experimento (de uno de los estudios específicos)
        # Vamos a asumir que necesitamos el ID del estudio desde el frontend
        study_id = request.args.get('study_id', 'OSD-665')  # Default: OSD-665 para pruebas
        api_key = Config.NASA_API_KEY  # Asegúrate de definir tu API key en la configuración

        # Llamar la función para preparar los datos del estudio
        data_json = preparar_datos_para_visualizacion(study_id, api_key)
        return jsonify(json.loads(data_json))
    except Exception as e:
        logger.error(f"Error al obtener los datos procesados: {str(e)}")
        return jsonify({"error": "No se pudo obtener los datos procesados."}), 500


# Ruta para servir archivos estáticos
@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(os.path.join(app.template_folder), path)

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)