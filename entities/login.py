
class Login:

    def __init__(self, user_name: str, pass_word: str, employee_id: int):
        self.user_name = user_name
        self.employee_id = employee_id
        self.pass_word = pass_word

    def as_json_dict(self):
        return {'userName': self.user_name, 'passWord': self.pass_word, 'employeeId': self.employee_id}
