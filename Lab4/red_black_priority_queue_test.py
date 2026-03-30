import unittest
from red_black_priority_queue import RedBlackPriorityQueue


if __name__ == '__main__':
    if __name__ == '__main__':
        pq = RedBlackPriorityQueue()
    
    tasks_to_add = [
        ("Заварити чай", 10),
        ("Поспати", 100),
        ("Погодувати кота", 50),
        ("Помити посуд", 5),
        ("Перевірити пошту", 20),
        ("Зателефонувати мамі", 50)
    ]
    
    print("--- ДОДАВАННЯ В ЧЕРГУ ---")
    for task, priority in tasks_to_add:
        pq.insert(task, priority)
        print(f"Додано: '{task}' (Пріоритет: {priority})")
        
    print("\n--- ВИКОНАННЯ ЗАВДАНЬ (від найважливішого до найменшого) ---")
    
    place = 1
    while True:
        top_task = pq.extract_max()
        
        if top_task is None:
            break
            
        print(f"{place}. Виконується: '{top_task.value}' [Пріоритет: {top_task.priority}]")
        place += 1
        
    print("\nЧерга порожня! Всі завдання виконано.")