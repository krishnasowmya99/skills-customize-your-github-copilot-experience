from typing import List, Any


def find_item_index(items: List[Any], target: Any) -> int:
    for index, item in enumerate(items):
        if item == target:
            return index
    return -1


def count_occurrences(items: List[Any], target: Any) -> int:
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count


def sort_numbers(numbers: List[float]) -> List[float]:
    return sorted(numbers)


def unique_sorted_values(items: List[Any]) -> List[Any]:
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    return sorted(unique_items)


if __name__ == "__main__":
    sample_items = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    print(find_item_index(sample_items, 5))
    print(count_occurrences(sample_items, 1))
    print(sort_numbers([5, 3, 8, 1]))
    print(unique_sorted_values([3, 1, 4, 1, 5, 3]))
