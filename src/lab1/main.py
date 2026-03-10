class Teacher:
    def __init__(self, name):
        self.name = name


class StudentGroup:
    def __init__(self, name, size):
        if size < 13:
            raise ValueError("Група має бути не менше 13 чол.")
        self.name = name
        self.size = size


class Activity:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

    def conduct(self, group):
        print(
            f"[{self.name}] проводиться для групи {group.name}. Викладач: {self.teacher.name}"
        )


class Discipline:
    def __init__(self, name):
        self.name = name
        self.activities = []

    def add_activity(self, activity):
        self.activities.append(activity)

    def study(self, group):
        print(f"\n--- Початок вивчення: {self.name} ---")
        for activity in self.activities:
            activity.conduct(group)


class HigherMath(Discipline):
    def __init__(self, lecture_teacher, practice_teacher):
        super().__init__("Вища математика")
        self.add_activity(Activity("Лекція", lecture_teacher))
        self.add_activity(Activity("Практична", practice_teacher))
        self.add_activity(Activity("Курсова робота", practice_teacher))
        self.add_activity(Activity("МКР", lecture_teacher))
        self.add_activity(Activity("Екзамен", lecture_teacher))


class English(Discipline):
    def __init__(self, practice_teacher):
        super().__init__("Англійська")
        self.add_activity(Activity("Практична", practice_teacher))
        self.add_activity(Activity("МКР", practice_teacher))
        self.add_activity(Activity("Залік", practice_teacher))


class Physics(Discipline):
    def __init__(self, lecture_teacher, lab_teacher):
        super().__init__("Фізика")
        self.add_activity(Activity("Лекція", lecture_teacher))
        self.add_activity(Activity("Лабораторна робота", lab_teacher))
        self.add_activity(Activity("Курсова робота", lecture_teacher))
        self.add_activity(Activity("МКР", lecture_teacher))
        self.add_activity(Activity("Екзамен", lecture_teacher))
