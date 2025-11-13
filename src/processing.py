from typing import List, Dict, Any


def filter_by_state(
        operations: List[Dict[str, Any]],
        state: str = 'EXECUTED'
) -> List[Dict[str, Any]]:
    """
    Фильтрует операции по статусу.

    Args:
        operations: Список операций
        state: Статус для фильтрации

    Returns:
        Отфильтрованный список операций
    """
    filtered_ops = []
    for operation in operations:
        if operation.get('state') == state:
            filtered_ops.append(operation)
    return filtered_ops


def sort_by_date(
        operations: List[Dict[str, Any]],
        reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует операции по дате.

    Args:
        operations: Список операций
        reverse: Порядок сортировки

    Returns:
        Отсортированный список операций
    """
    return sorted(
        operations,
        key=lambda x: x['date'],
        reverse=reverse
    )
