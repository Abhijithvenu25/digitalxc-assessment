import unittest
from secret_santa.models import Employee, Assignment
from secret_santa.assigner import SecretSantaAssigner
from secret_santa.exceptions import AssignmentImpossibleError

class TestAssigner(unittest.TestCase):
    def test_generate_assignments_success(self):
        employees = [
            Employee("A", "a@acme.com"),
            Employee("B", "b@acme.com"),
            Employee("C", "c@acme.com")
        ]
        assigner = SecretSantaAssigner(employees)
        assignments = assigner.generate_assignments()
        
        self.assertEqual(len(assignments), 3)
        for a in assignments:
            self.assertNotEqual(a.employee, a.secret_child)
            
        givers = {a.employee.email for a in assignments}
        receivers = {a.secret_child.email for a in assignments}
        self.assertEqual(len(givers), 3)
        self.assertEqual(len(receivers), 3)

    def test_generate_assignments_with_previous(self):
        employees = [
            Employee("A", "a@acme.com"),
            Employee("B", "b@acme.com"),
            Employee("C", "c@acme.com")
        ]
        previous = {"a@acme.com": "b@acme.com"}
        assigner = SecretSantaAssigner(employees, previous)
        assignments = assigner.generate_assignments()
        
        a_assignment = next(a for a in assignments if a.employee.email == "a@acme.com")
        self.assertEqual(a_assignment.secret_child.email, "c@acme.com")
        
    def test_impossible_assignment(self):
        employees = [
            Employee("A", "a@acme.com"),
            Employee("B", "b@acme.com")
        ]
        previous = {"a@acme.com": "b@acme.com"}
        
        assigner = SecretSantaAssigner(employees, previous, max_retries=10)
        with self.assertRaises(AssignmentImpossibleError):
            assigner.generate_assignments()

if __name__ == '__main__':
    unittest.main()
