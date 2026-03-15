import React from 'react';
import './styles/App.css';
import Visualizer from './components/Visualizer';

const App: React.FC = () => {
    return (
        <div className="app">
            <header className="app-header">
                <h1>Algorithm Visualizer</h1>
                <p>Watch sorting algorithms work step by step</p>
            </header>
            <main>
                <Visualizer />
            </main>
        </div>
    );
};

export default App;
