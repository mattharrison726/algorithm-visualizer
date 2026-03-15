from typing import List, Dict, Any


def bubble_sort_steps(data: List[int]) -> List[Dict[str, Any]]:
    arr = data[:]
    steps = [{"array": arr[:], "comparing": [], "swapped": []}]

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            steps.append({"array": arr[:], "comparing": [j, j + 1], "swapped": []})
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append({"array": arr[:], "comparing": [], "swapped": [j, j + 1]})

    steps.append({"array": arr[:], "comparing": [], "swapped": []})
    return steps


def selection_sort_steps(data: List[int]) -> List[Dict[str, Any]]:
    arr = data[:]
    steps = [{"array": arr[:], "comparing": [], "swapped": []}]

    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps.append({"array": arr[:], "comparing": [min_idx, j], "swapped": []})
            if arr[j] < arr[min_idx]:
                min_idx = j

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            steps.append({"array": arr[:], "comparing": [], "swapped": [i, min_idx]})

    steps.append({"array": arr[:], "comparing": [], "swapped": []})
    return steps
