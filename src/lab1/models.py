from abc import ABC


class EventNotifier:
    def __init__(self):
        self._subscribers = []

    def subscribe(self, callback):
        self._subscribers.append(callback)

    def notify(self, message: str):
        for callback in self._subscribers:
            callback(message)


class Equipment(ABC):
    def __init__(self, name: str):
        self.name = name


class AudioEquipment(Equipment):
    def __init__(self):
        super().__init__("Звуковідтворююче обладнання")


class Laboratory(Equipment):
    def __init__(self):
        super().__init__("Лабораторія фізики")


class Computer(Equipment):
    def __init__(self):
        super().__init__("Комп'ютер для симуляцій")


class StudentGroup:
    def __init__(self, name: str, course: int, size: int):
        if size < 13:
            raise ValueError(
                f"Група {name} замала! Не може бути менше 13 чол. (Зараз: {size})"
            )

        self.name = name
        self.course = course
        self.size = size

    def get_subgroups_count(self) -> int:
        count = self.size // 10
        if count == 0:
            raise ValueError(
                f"Група {self.name} не може утворити жодної підгрупи по 10+ чол."
            )
        return count


class Teacher:
    def __init__(self, name: str):
        self.name = name
        self.current_discipline = None

    def assign_to_discipline(self, discipline_name: str):
        if self.current_discipline and self.current_discipline != discipline_name:
            raise ValueError(
                f"Викладач {self.name} вже веде дисципліну {self.current_discipline}. Не можна вести кілька одночасно!"
            )
        self.current_discipline = discipline_name

    def release(self):
        self.current_discipline = None
