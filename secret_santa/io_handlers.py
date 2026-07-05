import csv
from typing import List, Dict
from .models import Employee, Assignment
from .exceptions import InvalidInputError

class CSVHandler:
    """Handles reading and writing data to CSV files."""
    def __init__(self, input_file: str, output_file: str, previous_file: str = None):
        self.input_file = input_file
        self.output_file = output_file
        self.previous_file = previous_file

    def read_employees(self) -> List[Employee]:
        try:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                return [
                    Employee(row['Employee_Name'].strip(), row['Employee_EmailID'].strip()) 
                    for row in csv.DictReader(f) if row.get('Employee_EmailID')
                ]
        except Exception as e:
            raise InvalidInputError(f"Error reading employees from {self.input_file}: {e}")

    def read_previous_assignments(self) -> Dict[str, str]:
        if not self.previous_file:
            return {}
        try:
            with open(self.previous_file, 'r', encoding='utf-8') as f:
                return {
                    row['Employee_EmailID'].strip(): row['Secret_Child_EmailID'].strip() 
                    for row in csv.DictReader(f) if row.get('Employee_EmailID')
                }
        except Exception as e:
            raise InvalidInputError(f"Error reading previous assignments: {e}")

    def write_assignments(self, assignments: List[Assignment]) -> None:
        with open(self.output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=[
                'Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID'
            ])
            writer.writeheader()
            writer.writerows([{
                'Employee_Name': a.employee.name,
                'Employee_EmailID': a.employee.email,
                'Secret_Child_Name': a.secret_child.name,
                'Secret_Child_EmailID': a.secret_child.email
            } for a in assignments])
