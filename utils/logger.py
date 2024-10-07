import logging

# Configuración del logger
logger = logging.getLogger("biospace_logger")
logger.setLevel(logging.DEBUG)

# Formato del mensaje
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Consola (StreamHandler)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Archivo de registro (FileHandler)
file_handler = logging.FileHandler("biospace.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)