class Teacher:
    def __init__(self, name: str) -> None:
        self.__name: str = name  # Private

    def get_name(self) -> str:
        return self.__name

    def teach(self, s: "Student") -> None:
        print(f"{self.__name} is teaching {s.get_name()}")


class Student:
    def __init__(self, name: str) -> None:
        self.__name: str = name  # Private

    def get_name(self) -> str:
        return self.__name


teacher1 = Teacher("Sharma Sir")
student1 = Student("Rahul")

teacher1.teach(student1)  # teach() takes Student type as parameter
