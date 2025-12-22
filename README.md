# Algorithm Visualizer

This project is an Algorithm Visualizer application that consists of a frontend built with React and TypeScript, and a backend powered by FastAPI in Python. The application aims to provide an interactive platform for visualizing various algorithms.

## Project Structure

The project is organized into two main directories: `backend` and `frontend`.

### Backend

- **app**: Contains the FastAPI application code.
  - **main.py**: Entry point of the FastAPI application.
  - **api/routes.py**: Defines the API routes for the application.
  - **core/config.py**: Contains configuration settings for the FastAPI application.
  - **models**: Package for model definitions.
- **requirements.txt**: Lists the dependencies required for the backend.
- **README.md**: Documentation specific to the backend.

### Frontend

- **src**: Contains the source code for the React application.
  - **App.tsx**: Main component of the React application.
  - **index.tsx**: Entry point for the React application.
  - **components/Visualizer.tsx**: Component that visualizes algorithms.
  - **styles/App.css**: CSS styles for the React application.
  - **types/index.ts**: TypeScript types and interfaces used throughout the frontend.
- **public**: Contains static files.
  - **index.html**: Main HTML file for the React application.
- **package.json**: Configuration file for npm.
- **tsconfig.json**: Configuration file for TypeScript.
- **README.md**: Documentation specific to the frontend.

## Setup Instructions

### Backend Setup

1. Navigate to the `backend` directory.
2. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
3. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install the required dependencies using:
   ```
   npm install
   ```
3. Start the React application:
   ```
   npm start
   ```

## Usage

Once both the backend and frontend are running, you can access the application in your web browser. The frontend will communicate with the backend to fetch and visualize algorithm data.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.