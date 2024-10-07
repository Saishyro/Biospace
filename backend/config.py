# Archivo de configuración para la aplicación Biospace Backend
import os
from dotenv import load_dotenv # type: ignore

# Cargar variables de entorno desde el archivo .env
load_dotenv()

class Config:
    """
    Clase de configuración principal para la aplicación Biospace Backend.
    Contiene todas las configuraciones necesarias para la base de datos,
    conexión con la API de OSDR, y configuraciones generales.
    """
    # Configuración de la base de datos
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///biospace.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuración para la API de OSDR
    OSDR_API_BASE_URL = os.getenv("OSDR_API_BASE_URL", "https://osdr.nasa.gov/osdr/data/osd/files/")
    OSDR_API_KEY = os.getenv("JDTgtIRdLcxRDB5eMsl2V6Nh89ikU0RVgeDfcNAk", "")  # Si la API requiere autenticación

    # Configuración general
    DEBUG = os.getenv("DEBUG", "True") == "True"
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

class ProductionConfig(Config):
    """Configuración específica para el entorno de producción."""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI_PROD", "sqlite:///biospace_prod.db")

class DevelopmentConfig(Config):
    """Configuración específica para el entorno de desarrollo."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI_DEV", "sqlite:///biospace_dev.db")

# Mapeo de configuraciones
config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
