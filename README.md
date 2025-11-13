@"
# Банковский виджет операций

## Описание проекта
Проект предназначен для обработки и анализа банковских операций клиента.
Включает функции для фильтрации и сортировки операций по различным параметрам.

## Установка
1. Клонируйте репозиторий:
\`\`\`bash
git clone <url-вашего-репозитория>
\`\`\`

2. Перейдите в директорию проекта:
\`\`\`bash
cd <название-репозитория>
\`\`\`

3. Установите зависимости с помощью Poetry:
\`\`\`bash
poetry install --no-root
\`\`\`

4. Активируйте виртуальное окружение:
\`\`\`bash
poetry shell
\`\`\`

## Использование

### Функция filter_by_state
Фильтрует операции по статусу (EXECUTED, CANCELED и т.д.)

\`\`\`python
from src.processing import filter_by_state

operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'}
]

# Фильтрация выполненных операций
executed_ops = filter_by_state(operations)
print(executed_ops)
\`\`\`

### Функция sort_by_date
Сортирует операции по дате

\`\`\`python
from src.processing import sort_by_date

operations = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-02'},
    {'id': 2, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2023-01-03'}
]

# Сортировка по убыванию
sorted_desc = sort_by_date(operations)
print(sorted_desc)
\`\`\`

## Структура проекта
\`\`\`
project/
├── src/
│   └── processing.py
├── README.md
├── .gitignore
├── pyproject.toml
└── poetry.lock
\`\`\`
"@ | Out-File -FilePath README.md -Encoding UTF8
