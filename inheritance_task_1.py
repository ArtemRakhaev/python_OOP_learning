class Animal:

    def __init__(self, name: str, old: int) -> None:
        self.name = name
        self.old = old


class Cat(Animal):

    def __init__(self, name: str, old: int, color: str, weight: (int, float)) -> None:
        super().__init__(name, old)
        self.color = color
        self.weight = weight

    def get_info(self) -> str:
        return f'{self.name}: {self.old}, {self.color}, {self.weight}'


class Dog(Animal):

    def __init__(self, name: str, old: int, breed: str, size: tuple) -> None:
        super().__init__(name, old)
        self.breed = breed
        self.size = size

    def get_info(self) -> str:
        return f'{self.name}: {self.old}, {self.breed}, {self.size}'
