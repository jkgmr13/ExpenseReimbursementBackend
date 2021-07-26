
class Reimbursement:

    def __init__(self, re_id: int, employee_id: int, amount: int, status: str, reason: str):
        self.re_id = re_id
        self.employee_id = employee_id
        self.amount = amount
        self.status = status
        self.reason = reason

    def as_json_dict(self):
        return {"reId": self.re_id, "employeeId": self.employee_id, "amount": self.amount,
                                                                    "status": self.status, "reason": self.reason}

