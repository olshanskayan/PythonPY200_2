from collections.abc import MutableSequence
from node import Node
from typing import Any, Iterable, Optional


class LinkedList(MutableSequence):
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        super().__init__()

        self.__len = 0
        self.__head: Optional[Node] = None
        self._tail = self.__head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.__head is None:
            self.__head = self._tail = append_node
        else:
            self.linked_nodes(self._tail, append_node)
            self._tail = append_node

        self.__len += 1


    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        super().__getitem__(index)
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        super().__setitem__(index, value)
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def __delitem__(self, index: int):
        super().__delitem__(index)
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.__len:  # для for
            raise IndexError()

        if index == 0:
            self.__head = self.__head.next
        elif index == self.__len - 1:
            _tail = self.step_by_step_on_nodes(index-1)
            _tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index-1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self.__len -= 1

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.__head}\")(\"{self._tail}\")"

    def __str__(self) -> str:
        return f"{self.to_list()}"


    def __len__(self, data: Iterable = None):
        ...


    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()

        insert_node = Node(value)

        if index == 0:
            insert_node.next = self.__head
            self.__head = insert_node
            self.__len += 1
        elif index >= self.__len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self.__len += 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def linked_nodes(self, left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node
        # self.left_node.next = right_node

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.__len:  # для for
            raise IndexError()

        current_node = self.__head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head_: Optional["Node"]):
        self.is_valid(head_)
        self.__head = head_

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, tail_: Optional["Node"]):
        self.is_valid(tail_)
        self._tail = tail_

class DoubleLinkedList(LinkedList):
    def __init__(self, value, next_, prev_: Optional["Node"] = None):
        super().__init__(value, next_)

        self.prev = prev_

    def __repr__(self) -> str:
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self.prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"
        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"

    @property
    def prev(self):
        return self._prev

    @prev.setter
    def prev(self, prev_: Optional["Node"]):
        self.is_valid(prev_)
        self._prev = prev_


if __name__ == "__main__":
    ...
    list_ = [1, 2, 3]
    linked_list = LinkedList(list_)
    print(linked_list)

    # print(linked_list.__str__())
    # print(linked_list.__repr__())

    linked_list.insert(0, 1)
    print(linked_list)
