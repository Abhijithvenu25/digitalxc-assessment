import random
from typing import List, Dict
from .models import Employee, Assignment
from .exceptions import AssignmentImpossibleError, InvalidInputError


class SecretSantaAssigner:
    """Core logic to generate valid Secret Santa assignments based on constraints."""
    def __init__(self, employees: List[Employee], previous_assignments: Dict[str, str] = None, max_retries: int = 1000):
        if len(employees) < 2:
            raise InvalidInputError("At least two employees are required.")
            
        self.employees = employees
        self.previous_assignments = previous_assignments or {}
        self.max_retries = max_retries
        
    def generate_assignments(self) -> List[Assignment]:
        employees_copy = list(self.employees)
        
        for _ in range(self.max_retries):
            random.shuffle(employees_copy)
            
            # Check if the generated cycle violates the previous year's constraints
            collision = any(
                self.previous_assignments.get(employees_copy[i].email) == employees_copy[(i + 1) % len(employees_copy)].email 
                for i in range(len(employees_copy))
            )
            
            if not collision:
                return [
                    Assignment(employees_copy[i], employees_copy[(i + 1) % len(employees_copy)]) 
                    for i in range(len(employees_copy))
                ]
                
        raise AssignmentImpossibleError("Could not find a valid assignment satisfying all constraints.")
