export interface Algorithm {
    id: string;
    name: string;
    description: string;
    complexity: {
        time: string;
        space: string;
    };
}

export interface VisualizationProps {
    algorithm: Algorithm;
    data: number[];
    speed: number;
}

export interface AppState {
    algorithms: Algorithm[];
    selectedAlgorithm: Algorithm | null;
    visualizationData: number[];
}