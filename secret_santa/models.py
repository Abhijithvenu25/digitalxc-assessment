from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    email: str

    def __hash__(self):
        return hash(self.email)

    def __eq__(self, other):
        if not isinstance(other, Employee):
            return False
        return self.email == other.email


@dataclass
class Assignment:
    employee: Employee
    secret_child: Employee
