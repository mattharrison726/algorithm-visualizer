import React from 'react';
import './styles/App.css';
import Visualizer from './components/Visualizer';

const App: React.FC = () => {
    return (
        <div className="App">
            <h1>Algorithm Visualizer</h1>
            <Visualizer />
        </div>
    );
};

export default App;