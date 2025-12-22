# Algorithm Visualizer Backend

This is the backend for the Algorithm Visualizer application, built using FastAPI. The backend serves as the API layer that handles requests from the frontend and processes data related to various algorithms.

## Project Structure

- **app/**: Contains the main application code.
  - **main.py**: Entry point of the FastAPI application.
  - **api/**: Contains the API routes.
    - **routes.py**: Defines the API endpoints and their handlers.
  - **core/**: Contains configuration settings.
    - **config.py**: Configuration settings for the application.
  - **models/**: Contains data models for the application.
    - **__init__.py**: Initializes the models package.

## Installation

To install the required dependencies, run:

```
pip install -r requirements.txt
```

## Running the Application

To start the FastAPI application, run:

```
uvicorn app.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## API Documentation

The automatically generated API documentation can be accessed at `http://127.0.0.1:8000/docs`. This provides an interactive interface to test the API endpoints.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.