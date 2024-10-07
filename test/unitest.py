import unittest
from app import app # type: ignore
from models import data_ingestion, data_processing, ml_models
from utils import database

# test_app.py - Pruebas unitarias para el archivo principal app.py
class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Biospace', response.data)

    def test_search_experiment(self):
        response = self.client.get('/api/search?query=experiment')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['results'])

if __name__ == '__main__':
    unittest.main()


# test_models.py - Pruebas unitarias para los modelos de datos y procesos de ML
class TestDataModels(unittest.TestCase):
    def test_data_ingestion(self): 
        result = data_ingestion.ingest_data('test_source')
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)

    def test_data_processing(self):
        raw_data = {'data': [1, 2, 3]}
        processed_data = data_processing.process_data(raw_data)
        self.assertIsInstance(processed_data, list)
        self.assertEqual(len(processed_data), 3)

    def test_ml_models(self):
        training_data = {'features': [[1], [2]], 'labels': [0, 1]}
        model = ml_models.train_model(training_data)
        prediction = model.predict([[1.5]])
        self.assertIn(prediction[0], [0, 1])

if __name__ == '__main__':
    unittest.main()


# test_utils.py - Pruebas unitarias para utilidades como la conexión a la base de datos
class TestUtils(unittest.TestCase):
    def test_database_connection(self):
        db = database.connect()
        self.assertIsNotNone(db)
        self.assertTrue(db.is_connected())

    def test_database_crud(self):
        db = database.connect()
        record_id = db.insert({'name': 'Test Record'})
        record = db.get(record_id)
        self.assertEqual(record['name'], 'Test Record')
        db.update(record_id, {'name': 'Updated Record'})
        updated_record = db.get(record_id)
        self.assertEqual(updated_record['name'], 'Updated Record')
        db.delete(record_id)
        deleted_record = db.get(record_id)
        self.assertIsNone(deleted_record)

if __name__ == '__main__':
    unittest.main()