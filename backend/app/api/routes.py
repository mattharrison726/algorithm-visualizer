from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from app.algorithms.sorting import bubble_sort_steps, selection_sort_steps

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
]


class VisualizeRequest(BaseModel):
    algorithm: str
    data: List[int]


@router.get("/algorithms")
async def get_algorithms():
    return ALGORITHMS


@router.post("/visualize")
async def visualize_algorithm(body: VisualizeRequest):
    if body.algorithm == "bubble_sort":
        steps = bubble_sort_steps(body.data)
    elif body.algorithm == "selection_sort":
        steps = selection_sort_steps(body.data)
    else:
        raise HTTPException(status_code=400, detail=f"Unknown algorithm: {body.algorithm}")

    return {"algorithm": body.algorithm, "steps": steps}
