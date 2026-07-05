import unittest
import os
import csv
import tempfile
from secret_santa.io_handlers import CSVHandler
from secret_santa.models import Employee, Assignment

class TestIOHandlers(unittest.TestCase):
    def test_read_employees(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as f:
            f.write("Employee_Name,Employee_EmailID\nA,a@test.com\nB,b@test.com\n")
            temp_path = f.name
            
        try:
            handler = CSVHandler(temp_path, "dummy.csv")
            employees = handler.read_employees()
            self.assertEqual(len(employees), 2)
            self.assertEqual(employees[0].name, "A")
            self.assertEqual(employees[0].email, "a@test.com")
        finally:
            os.remove(temp_path)

    def test_write_assignments(self):
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv') as f:
            temp_path = f.name
            
        try:
            assignments = [
                Assignment(Employee("A", "a@t.com"), Employee("B", "b@t.com"))
            ]
            handler = CSVHandler("dummy.csv", temp_path)
            handler.write_assignments(assignments)
            
            self.assertTrue(os.path.exists(temp_path))
            with open(temp_path, 'r') as f2:
                reader = csv.DictReader(f2)
                rows = list(reader)
                self.assertEqual(len(rows), 1)
                self.assertEqual(rows[0]['Employee_Name'], "A")
                self.assertEqual(rows[0]['Employee_EmailID'], "a@t.com")
                self.assertEqual(rows[0]['Secret_Child_Name'], "B")
                self.assertEqual(rows[0]['Secret_Child_EmailID'], "b@t.com")
        finally:
            os.remove(temp_path)

if __name__ == '__main__':
    unittest.main()
