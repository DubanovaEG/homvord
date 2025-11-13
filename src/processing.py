from typing import List, Dict, Any, Optional


def filter_by_state(operations: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список операций по статусу.

    Args:
        operations: Список словарей с данными о банковских операциях
        state: Статус операций для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Новый список словарей, содержащий только операции с указанным статусом
    """
    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date(operations: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Сортирует список операций по дате.

    Args:
        operations: Список словарей с данными о банковских операциях
        reverse: Порядок сортировки (True - по убыванию, False - по возрастанию)

    Returns:
        Новый список словарей, отсортированный по дате
    """
    return sorted(operations, key=lambda x: x['date'], reverse=reverse
