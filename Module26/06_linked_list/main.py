from collections.abc import Iterable
from typing import Any


class LinkedList:
    """
    Класс, создающий "список" из передаваемых объектов

    """

    def __init__(self):
        self.head = None
        self.length = 0
        self.step = 0

    class Node:
        """
        Вложенный класс, создающий "узлы" из данных
        атрибуты:
        element = по умолчанию None, иначе = передается само значение (Any)
        next_node = ссылка на следующий узел
        """

        element = None
        next_node = None

        def __init__(self, element: Any, next_node=None) -> None:
            self.element = element
            self.next_node = next_node

    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> Iterable[int]:
        node = self.head
        ret_element = node.element
        for _ in range(self.step+1):
            if node is None:
                raise StopIteration
            else:
                ret_element = node.element
                node = node.next_node
        self.step += 1
        return ret_element

    def append(self, new_element: Any) -> Iterable[Any]:
        """
        Метод, "добавляющий" новый элемент в "список"
        :param new_element: добавляемый элемент
        :return: значение элемента
        """
        if not self.head:
            self.head = self.Node(new_element)
            return new_element
        node = self.head
        while node.next_node:
            node = node.next_node
            self.length += 1
        node.next_node = self.Node(new_element)
        self.length += 1

    def get(self, find_index: int) -> Iterable[int]:
        """
        Метод, возвращающий значение элемента по индексу
        :param find_index: индекс элемента в списке
        :return: значение элемента
        """
        node = self.head
        step = 0
        while step != find_index:
            node = node.next_node
            step += 1
        return node.element

    def remove(self, delete_index: int) -> Iterable[int]:
        """
        Метод, удаляющий элемент из списка по индексу
        :param delete_index: индекс элемента
        :return: значение элемента
        """
        node = self.head
        step = 0
        previous_node = node
        if delete_index == 0:
            self.head = self.head.next_node
            return node.element
        while step != delete_index:
            previous_node = node
            node = node.next_node
            step += 1
        previous_node.next_node = node.next_node
        ret_element = node.element
        del node
        self.length -= 2
        return ret_element

    def __str__(self):
        my_string = '['
        node = self.head
        while node.next_node:
            my_string += f'{str(node.element)}, '
            node = node.next_node
        my_string += str(node.element) + ']'
        return my_string


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append("'Future'")
my_list.append("'Minsk'")
print()
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
print('Элементы первого списка: ')
for j in my_list:
    print(j)

print()
new_list = LinkedList()
new_list.append(100)
new_list.append("'swimming'")
new_list.append(45)
new_list.append(75)
print('Текущий второй список:', new_list)
print('Удаление второго элемента.')
new_list.remove(1)
print('Новый второй список:', new_list)
print('Получение третьего элемента:', new_list.get(2))
print('Элементы второго списка: ')
for i in new_list:
    print(i)



