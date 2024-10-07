import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import logging

nltk.download('punkt')
nltk.download('stopwords')

# Configuración del logger para registrar información
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class NLPProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer()

    def preprocess_text(self, text):
        """
        Preprocesa el texto eliminando caracteres especiales, convirtiendo a minúsculas y eliminando stopwords.
        """
        try:
            # Eliminación de caracteres especiales
            text_cleaned = re.sub(r'[^a-zA-Z0-9\s]', '', text)
            # Conversión a minúsculas
            text_lower = text_cleaned.lower()
            # Tokenización
            tokens = word_tokenize(text_lower)
            # Eliminación de stopwords
            filtered_tokens = [word for word in tokens if word not in self.stop_words]
            return ' '.join(filtered_tokens)
        except Exception as e:
            logger.error(f"Error durante la preprocesamiento del texto: {e}")
            return None

    def vectorize_text(self, texts):
        """
        Convierte una lista de textos en una matriz TF-IDF.
        """
        try:
            return self.vectorizer.fit_transform(texts)
        except Exception as e:
            logger.error(f"Error durante la vectorización del texto: {e}")
            return None

# Ejemplo de uso
def main():
    nlp_processor = NLPProcessor()
    sample_texts = [
        "The effects of space travel on the human body are complex.",
        "This experiment aims to measure the physiological changes in microgravity."
    ]
    preprocessed_texts = [nlp_processor.preprocess_text(text) for text in sample_texts]
    tfidf_matrix = nlp_processor.vectorize_text(preprocessed_texts)

    logger.info("Textos preprocesados:")
    for text in preprocessed_texts:
        logger.info(text)

    logger.info("Matriz TF-IDF:")
    logger.info(tfidf_matrix)

if __name__ == "__main__":
    main()