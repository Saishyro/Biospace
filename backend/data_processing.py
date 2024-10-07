# Archivo: backend/data_processing.py

import pandas as pd
import requests
import json

# URL base de la API
API_BASE_URL = "https://api.nasa.gov/osdr"

# Endpoint para obtener los datos de experimentos biológicos
def obtener_datos_experimento(study_id, api_key):
    """
    Funcionalidad para obtener los datos del experimento desde la API de OSDR.
    """
    url = f"{API_BASE_URL}/datasets/{study_id}?api_key={api_key}"
    response = requests.get(url)
    
    if response.status_code == 200:
        datos = response.json()
        return datos
    else:
        raise Exception(f"Error al obtener datos: {response.status_code}")

# Procesamiento de los datos obtenidos
def procesar_datos(datos):
    """
    Lógica para transformar los datos crudos de la API en un formato adecuado para la visualización.
    """
    # Creando un DataFrame con los datos obtenidos de la API
    df = pd.DataFrame(datos['results'])
    
    # Seleccionando columnas relevantes
    df = df[['experiment_name', 'subject_count', 'treatment_type', 'launch_date', 'return_date']]
    
    # Transformaciones adicionales: conversión de fechas, etc.
    df['launch_date'] = pd.to_datetime(df['launch_date'])
    df['return_date'] = pd.to_datetime(df['return_date'])
    
    return df

# Convertir los datos procesados en JSON para la visualización
def convertir_datos_a_json(df):
    """
    Convierte el DataFrame procesado a un formato JSON para enviar al frontend.
    """
    datos_json = df.to_json(orient='records')
    return datos_json

# Llamada principal para obtener, procesar y estructurar los datos
def preparar_datos_para_visualizacion(study_id, api_key):
    try:
        datos = obtener_datos_experimento(study_id, api_key)
        df_procesado = procesar_datos(datos)
        datos_json = convertir_datos_a_json(df_procesado)
        return datos_json
    except Exception as e:
        print(f"Error en el procesamiento: {str(e)}")