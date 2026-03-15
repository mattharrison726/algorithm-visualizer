import React, { useCallback, useEffect, useRef, useState } from 'react';
import { Algorithm, Step } from '../types';

const API = '';
const BAR_COUNT = 20;

function randomArray(n: number): number[] {
    return Array.from({ length: n }, () => Math.floor(Math.random() * 90) + 10);
}

const Visualizer: React.FC = () => {
    const [algorithms, setAlgorithms] = useState<Algorithm[]>([]);
    const [selected, setSelected] = useState<string>('bubble_sort');
    const [array, setArray] = useState<number[]>(randomArray(BAR_COUNT));
    const [steps, setSteps] = useState<Step[]>([]);
    const [stepIndex, setStepIndex] = useState<number>(-1);
    const [playing, setPlaying] = useState(false);
    const [speed, setSpeed] = useState(100); // ms per step
    const [loading, setLoading] = useState(false);
    const intervalRef = useRef<ReturnType<typeof setInterval> | null>(null);

    useEffect(() => {
        fetch(`${API}/algorithms`)
            .then(r => r.json())
            .then(setAlgorithms)
            .catch(console.error);
    }, []);

    const stop = useCallback(() => {
        if (intervalRef.current) clearInterval(intervalRef.current);
        intervalRef.current = null;
        setPlaying(false);
    }, []);

    const reset = useCallback(() => {
        stop();
        setSteps([]);
        setStepIndex(-1);
        setArray(randomArray(BAR_COUNT));
    }, [stop]);

    const fetchSteps = useCallback(async (algoId: string, data: number[]) => {
        setLoading(true);
        stop();
        try {
            const res = await fetch(`${API}/visualize`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ algorithm: algoId, data }),
            });
            const json = await res.json();
            setSteps(json.steps);
            setStepIndex(0);
        } finally {
            setLoading(false);
        }
    }, [stop]);

    // auto-play
    useEffect(() => {
        if (!playing || steps.length === 0) return;
        intervalRef.current = setInterval(() => {
            setStepIndex(prev => {
                if (prev >= steps.length - 1) {
                    stop();
                    return prev;
                }
                return prev + 1;
            });
        }, speed);
        return () => { if (intervalRef.current) clearInterval(intervalRef.current); };
    }, [playing, steps, speed, stop]);

    const handleVisualize = () => {
        fetchSteps(selected, array);
    };

    const handlePlayPause = () => {
        if (steps.length === 0) return;
        if (stepIndex >= steps.length - 1) {
            setStepIndex(0);
            setPlaying(true);
        } else {
            setPlaying(p => !p);
        }
    };

    const currentStep: Step | null = stepIndex >= 0 && steps[stepIndex] ? steps[stepIndex] : null;
    const displayArray = currentStep ? currentStep.array : array;
    const maxVal = Math.max(...displayArray);
    const selectedAlgo = algorithms.find(a => a.id === selected);
    const isDone = steps.length > 0 && stepIndex === steps.length - 1;

    return (
        <div className="visualizer-wrapper">
            {/* Controls */}
            <div className="controls">
                <div className="control-group">
                    <label>Algorithm</label>
                    <select
                        value={selected}
                        onChange={e => { stop(); setSelected(e.target.value); setSteps([]); setStepIndex(-1); }}
                    >
                        {algorithms.map(a => (
                            <option key={a.id} value={a.id}>{a.name}</option>
                        ))}
                    </select>
                </div>

                <div className="control-group">
                    <label>Speed</label>
                    <input
                        type="range" min={20} max={500} step={10}
                        value={500 - speed + 20}
                        onChange={e => setSpeed(500 - Number(e.target.value) + 20)}
                    />
                </div>

                <div className="button-group">
                    <button className="btn btn-secondary" onClick={reset}>New Array</button>
                    <button className="btn btn-primary" onClick={handleVisualize} disabled={loading}>
                        {loading ? 'Loading…' : 'Generate Steps'}
                    </button>
                    {steps.length > 0 && (
                        <button className="btn btn-play" onClick={handlePlayPause}>
                            {playing ? '⏸ Pause' : isDone ? '↺ Replay' : '▶ Play'}
                        </button>
                    )}
                </div>
            </div>

            {/* Info bar */}
            {selectedAlgo && (
                <div className="algo-info">
                    <span className="algo-desc">{selectedAlgo.description}</span>
                    <span className="badge">Time: {selectedAlgo.complexity.time}</span>
                    <span className="badge">Space: {selectedAlgo.complexity.space}</span>
                </div>
            )}

            {/* Bar chart */}
            <div className="chart">
                {displayArray.map((val, i) => {
                    const isComparing = currentStep?.comparing.includes(i);
                    const isSwapped = currentStep?.swapped.includes(i);
                    let barClass = 'bar';
                    if (isSwapped) barClass += ' bar-swapped';
                    else if (isComparing) barClass += ' bar-comparing';
                    else if (isDone) barClass += ' bar-done';

                    return (
                        <div key={i} className="bar-col">
                            <div
                                className={barClass}
                                style={{ height: `${(val / maxVal) * 100}%` }}
                            />
                            {displayArray.length <= 25 && (
                                <span className="bar-label">{val}</span>
                            )}
                        </div>
                    );
                })}
            </div>

            {/* Step counter */}
            <div className="step-info">
                {steps.length > 0
                    ? `Step ${stepIndex + 1} / ${steps.length}`
                    : 'Press "Generate Steps" then Play to start'}
            </div>
        </div>
    );
};

export default Visualizer;
