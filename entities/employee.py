

class Employee:

    def __init__(self, emp_id: int, first_name: str, last_name: str, role_id: int):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.role_id = role_id

    def as_json_dict(self):
        return {'employeeId': self.emp_id, 'firstName': self.first_name, 'lastName': self.last_name, 'roleId': self.role_id}
