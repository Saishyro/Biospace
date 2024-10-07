# Biospace Backend

Biospace is an innovative tool that allows the visualization of biological experiments in space, connecting to the NASA OSDR API to retrieve data and providing analysis and visualizations using Machine Learning and NLP technologies.

## Project Structure

```
backend/
  app.py                    # Main entry point of the backend application.
  requirements.txt          # List of dependencies required for the backend.
  config.py                 # Application configurations, such as routes and specific variable settings.

  models/
    __init__.py             # Initializes the models module.
    data_ingestion.py       # Module responsible for data ingestion from various sources.
    data_processing.py      # Logic for processing the obtained data.
    ml_models.py            # Machine Learning model training and prediction.
    nlp_processing.py       # NLP processing related to experimental data.
    visualization_data.py   # Data generation for visualization by the frontend.

  utils/
    database.py             # Database connection and CRUD logic.
    api_client.py           # Client to connect to external services, such as APIs.

  data/
    raw/                    # Stores raw or unprocessed data.
    processed/              # Stores processed data ready for analysis and visualization.

  tests/
    test_app.py             # Unit tests for the main app.py file.
    test_models.py          # Unit tests for data models and ML processes.
    test_utils.py           # Unit tests for utilities like database connection.

  README.md                 # Documentation on how to install and run the backend.
```

## Installation

To install and run the backend, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/user/biospace-backend.git
   cd biospace-backend
   ```

2. Create a virtual environment and install the dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Set up environment variables:

   Create a `.env` file in the root of the project with the following variables:

   ```env
   DATABASE_URI=sqlite:///biospace.db
   OSDR_API_BASE_URL=https://osdr.nasa.gov/osdr/data/osd/files/
   OSDR_API_KEY=your_api_key
   DEBUG=True
   SECRET_KEY=supersecretkey
   ```

## Usage

To run the application, use the following command:

```bash
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

## Testing

To run unit tests:

```bash
python -m unittest discover tests
```

## Configuration

Configurations are found in `config.py`, where you can define different settings for development and production environments.

## Dependencies

The main dependencies used in this project include:

- Flask: Web framework for creating the API.
- SQLAlchemy: ORM for database connection and management.
- requests: HTTP client for connecting to the OSDR API.
- numpy, pandas, scikit-learn: Tools for Machine Learning and data processing.
- nltk: Library for natural language processing.
- matplotlib: For generating visualizations.

## Contributions

Contributions are not accepted. This project is being evaluated, and we do not allow modifications to ensure consistency.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.