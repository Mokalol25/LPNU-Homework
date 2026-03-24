import unittest
import os
from lab3_dop import build_tree_from_preorder, get_top_view, draw_dynamic_view

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        filename = "values.txt"
        
        if not os.path.exists(filename):
            self.fail(f"ПОМИЛКА: Файл '{filename}' не знайдено! Створіть його поруч зі скриптом.")
            
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            
        try:
            self.data = [int(x) for x in content.replace(',', ' ').split()]
        except ValueError:
            self.fail("ПОМИЛКА: У файлі 'values.txt' мають бути лише числа!")
            
        if not self.data:
            self.fail("ПОМИЛКА: Файл 'values.txt' порожній!")

        self.root = build_tree_from_preorder(self.data)

    def test_dynamic_render(self):
        print(f"\n[Прочитано з файлу values.txt]: {self.data}")
        
        view = get_top_view(self.root)
        print(f"Послідовність (Вид зверху): {view}")
        
        draw_dynamic_view(self.root)

if __name__ == "__main__":
    t = TestBinaryTree()
    t.setUp()
    t.test_dynamic_render()