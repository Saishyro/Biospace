import pandas as pd
import numpy as np

class DataProcessing:
    def __init__(self):
        """
        Inicializa la clase DataProcessing para procesar los datos crudos obtenidos de diferentes fuentes.
        """
        pass

    def clean_data(self, raw_data):
        """
        Limpia los datos crudos, eliminando valores nulos, duplicados y haciendo transformaciones necesarias.

        Args:
            raw_data (DataFrame): DataFrame con los datos crudos a limpiar.

        Returns:
            DataFrame: DataFrame con los datos limpios y procesados.
        """
        try:
            # Eliminar duplicados
            cleaned_data = raw_data.drop_duplicates()
            
            # Rellenar valores nulos con la media o eliminar si es necesario
            for column in cleaned_data.columns:
                if cleaned_data[column].isnull().sum() > 0:
                    if cleaned_data[column].dtype in [np.float64, np.int64]:
                        cleaned_data[column].fillna(cleaned_data[column].mean(), inplace=True)
                    else:
                        cleaned_data[column].fillna('Unknown', inplace=True)
            
            return cleaned_data
        except Exception as e:
            print(f"Error en la limpieza de datos: {str(e)}")
            return None

    def transform_data(self, cleaned_data):
        """
        Transforma los datos limpios para prepararlos para el análisis o modelado.

        Args:
            cleaned_data (DataFrame): DataFrame con los datos limpios a transformar.

        Returns:
            DataFrame: DataFrame con los datos transformados listos para análisis.
        """
        try:
            # Normalización de los datos numéricos
            numeric_columns = cleaned_data.select_dtypes(include=[np.number]).columns
            cleaned_data[numeric_columns] = (cleaned_data[numeric_columns] - cleaned_data[numeric_columns].mean()) / cleaned_data[numeric_columns].std()
            
            # Codificación de variables categóricas
            categorical_columns = cleaned_data.select_dtypes(include=['object']).columns
            cleaned_data = pd.get_dummies(cleaned_data, columns=categorical_columns)
            
            return cleaned_data
        except Exception as e:
            print(f"Error en la transformación de datos: {str(e)}")
            return None

# Código para realizar pruebas individuales
if __name__ == "__main__":
    # Crear un DataFrame de ejemplo
    example_data = pd.DataFrame({
        'experiment_id': [1, 2, 2, 3, 4, np.nan],
        'experiment_name': ['Exp-001', 'Exp-002', 'Exp-002', 'Exp-003', None, 'Exp-005'],
        'value': [120.5, 90.0, 90.0, None, 150.0, 200.0]
    })

    processor = DataProcessing()
    cleaned_data = processor.clean_data(example_data)
    transformed_data = processor.transform_data(cleaned_data)
    
    print("Datos Limpiados:")
    print(cleaned_data)
    print("\nDatos Transformados:")
    print(transformed_data)