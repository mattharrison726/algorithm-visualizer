from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.algorithms.sorting import (
    bubble_sort_steps,
    selection_sort_steps,
    insertion_sort_steps,
    merge_sort_steps,
    quick_sort_steps,
)

router = APIRouter()

ALGORITHMS = [
    {
        "id": "bubble_sort",
        "name": "Bubble Sort",
        "description": "Repeatedly steps through the list, compares adjacent elements, and swaps them if out of order.",
        "complexity": {"time": "O(n²)", "space": "O(1)"},
    },
    {
        "id": "selection_sort",
        "name": "Selection Sort",
        "description": "Finds the minimum element from the unsorted portion and places it at the beginning.",
        "complexity": {"time": "O(n²)", "space": "O(1)"},
    },
    {
        "id": "insertion_sort",
        "name": "Insertion Sort",
        "description": "Builds a sorted list one element at a time by inserting each into its correct position.",
        "complexity": {"time": "O(n²)", "space": "O(1)"},
    },
    {
        "id": "merge_sort",
        "name": "Merge Sort",
        "description": "Divides the list in half recursively, then merges the sorted halves back together.",
        "complexity": {"time": "O(n log n)", "space": "O(n)"},
    },
    {
        "id": "quick_sort",
        "name": "Quick Sort",
        "description": "Picks a pivot element and partitions the array so smaller values are left and larger are right.",
        "complexity": {"time": "O(n log n) avg", "space": "O(log n)"},
    },
]


class VisualizeRequest(BaseModel):
    algorithm: str
    data: List[int]


@router.get("/algorithms")
async def get_algorithms():
    return ALGORITHMS


@router.post("/visualize")
async def visualize_algorithm(body: VisualizeRequest):
    dispatch = {
        "bubble_sort": bubble_sort_steps,
        "selection_sort": selection_sort_steps,
        "insertion_sort": insertion_sort_steps,
        "merge_sort": merge_sort_steps,
        "quick_sort": quick_sort_steps,
    }
    if body.algorithm not in dispatch:
        raise HTTPException(status_code=400, detail=f"Unknown algorithm: {body.algorithm}")
    steps = dispatch[body.algorithm](body.data)

    return {"algorithm": body.algorithm, "steps": steps}
