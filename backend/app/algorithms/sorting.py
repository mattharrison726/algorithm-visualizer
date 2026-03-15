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


def insertion_sort_steps(data: List[int]) -> List[Dict[str, Any]]:
    arr = data[:]
    steps = [{"array": arr[:], "comparing": [], "swapped": []}]

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            steps.append({"array": arr[:], "comparing": [j, j + 1], "swapped": []})
            if arr[j] > key:
                arr[j + 1] = arr[j]
                steps.append({"array": arr[:], "comparing": [], "swapped": [j, j + 1]})
                j -= 1
            else:
                break
        arr[j + 1] = key

    steps.append({"array": arr[:], "comparing": [], "swapped": []})
    return steps


def merge_sort_steps(data: List[int]) -> List[Dict[str, Any]]:
    arr = data[:]
    steps: List[Dict[str, Any]] = [{"array": arr[:], "comparing": [], "swapped": []}]

    def merge(arr: List[int], left: int, mid: int, right: int) -> None:
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(left_part) and j < len(right_part):
            steps.append({"array": arr[:], "comparing": [left + i, mid + 1 + j], "swapped": []})
            if left_part[i] <= right_part[j]:
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            steps.append({"array": arr[:], "comparing": [], "swapped": [k]})
            k += 1
        while i < len(left_part):
            arr[k] = left_part[i]
            steps.append({"array": arr[:], "comparing": [], "swapped": [k]})
            i += 1
            k += 1
        while j < len(right_part):
            arr[k] = right_part[j]
            steps.append({"array": arr[:], "comparing": [], "swapped": [k]})
            j += 1
            k += 1

    def merge_sort(arr: List[int], left: int, right: int) -> None:
        if left < right:
            mid = (left + right) // 2
            merge_sort(arr, left, mid)
            merge_sort(arr, mid + 1, right)
            merge(arr, left, mid, right)

    merge_sort(arr, 0, len(arr) - 1)
    steps.append({"array": arr[:], "comparing": [], "swapped": []})
    return steps


def quick_sort_steps(data: List[int]) -> List[Dict[str, Any]]:
    arr = data[:]
    steps: List[Dict[str, Any]] = [{"array": arr[:], "comparing": [], "swapped": []}]

    def partition(arr: List[int], low: int, high: int) -> int:
        pivot_idx = high
        i = low - 1
        for j in range(low, high):
            steps.append({"array": arr[:], "comparing": [j, pivot_idx], "swapped": []})
            if arr[j] <= arr[pivot_idx]:
                i += 1
                if i != j:
                    arr[i], arr[j] = arr[j], arr[i]
                    steps.append({"array": arr[:], "comparing": [], "swapped": [i, j]})
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        steps.append({"array": arr[:], "comparing": [], "swapped": [i + 1, high]})
        return i + 1

    def quick_sort(arr: List[int], low: int, high: int) -> None:
        if low < high:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    quick_sort(arr, 0, len(arr) - 1)
    steps.append({"array": arr[:], "comparing": [], "swapped": []})
    return steps
