from typing import Iterable
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Iterable:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Iterable) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    # реализовать драйвер работы с текстовым файлом
    def __init__(self, filename: str):
        self.filename = filename

    # реализовать метод чтения данных из файла
    def read(self) -> list:
        with open(self.filename) as f:
            return [int(line.strip()) for line in f]

    #реализовать метод записи в файл построчно
    def write(self, data: Iterable) -> None:
        with open(self.filename, "w") as f:
            for item in data:
                f.write(repr(item))
                f.write("\n")

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


if __name__ == '__main__':
    write_data = [1, 2, 3]
    driver = SimpleFileDriver('tmp.txt')
    driver.write(write_data)

    read_data = driver.read()
    print(read_data)
