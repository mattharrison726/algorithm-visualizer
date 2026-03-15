export interface Algorithm {
    id: string;
    name: string;
    description: string;
    complexity: {
        time: string;
        space: string;
    };
}

export interface Step {
    array: number[];
    comparing: number[];
    swapped: number[];
}
