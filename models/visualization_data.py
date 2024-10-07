import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json

class VisualizationData:
    def __init__(self):
        """
        Inicializa la clase VisualizationData, configurando estilos de gráficos para una visualización consistente.
        """
        sns.set_theme(style="whitegrid")

    def generate_visualization(self, data_json, output_path="./data/processed/visualization.png"):
        """
        Genera una visualización de los datos experimentales.

        Args:
            data_json (str): JSON que contiene los datos experimentales para ser visualizados.
            output_path (str): Ruta de salida para guardar la imagen del gráfico.
        """
        try:
            # Convertir el JSON de entrada a un DataFrame
            data_dict = json.loads(data_json)
            df = pd.DataFrame(data_dict)
            
            if df.empty:
                raise ValueError("El DataFrame está vacío. No se encontraron datos para visualizar.")
            
            # Ejemplo de generación de gráfico para análisis exploratorio
            plt.figure(figsize=(10, 6))
            sns.barplot(data=df, x="experiment_name", y="value", palette="viridis")
            plt.title("Visualización de Datos Experimentales")
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            
            # Guardar el gráfico
            plt.savefig(output_path)
            print(f"Visualización guardada exitosamente en {output_path}")
        except Exception as e:
            print(f"Error generando la visualización: {str(e)}")

# Código para realizar pruebas individuales
if __name__ == "__main__":
    # Ejemplo de JSON con datos experimentales
    example_data = json.dumps([
        {"experiment_name": "Exp-001", "value": 120},
        {"experiment_name": "Exp-002", "value": 90},
        {"experiment_name": "Exp-003", "value": 150}
    ])
    
    visualizer = VisualizationData()
    visualizer.generate_visualization(example_data)