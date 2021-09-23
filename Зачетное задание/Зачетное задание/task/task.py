from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
#    def __init__(self):
    ...


class DoubleLinkedNode(Node):
    def __init__(self):
        super().__init__(self)
        self.prev = self.value


if __name__ == "__main__":
    ...
