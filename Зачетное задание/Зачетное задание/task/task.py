from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value
        self.next = next_  # вызовется setter

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)


    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

class DoubleLinkedNode(Node):
    def __init__(self, value, next_, prev_: Optional["Node"] = None):
        super().__init__(value, next_)

        self.prev = prev_

    # @property
    # def prev(self):
    #     return self.prev
    #
    # @prev.setter
    # def prev(self, prev_: Optional["Node"]):
    #     self.is_valid(prev_)
    #     self.prev = prev_

if __name__ == "__main__":
    # list_ = [1, 2, 3]
    # linked_list = DoubleLinkedNode(, None)
    # print(linked_list)

    # first_node = Node("Hello, ")
    # print(first_node)

    first_node = DoubleLinkedNode("Hello,", None)
    third_node = DoubleLinkedNode("World!", None, None)
    second_node = DoubleLinkedNode("My", third_node, first_node)

    print(first_node)
    print(second_node)
    print(third_node)
    print(second_node.prev, second_node, second_node.next)
