from daos.employee_dao import EmployeeDao
from daos.login_dao import LoginDao
from daos.reimbursement_dao import ReimbursementDao
from entities.employee import Employee
from entities.login import Login
from entities.reimbursement import Reimbursement
from exceptions.abuse_power import AbuseOfPowerError
from services.service import Service


class ServiceImpl(Service):

    def __init__(self, employee_dao: EmployeeDao, reimbursement_dao: ReimbursementDao, login_dao: LoginDao):
        self.employee_dao = employee_dao
        self.reimbursement_dao = reimbursement_dao
        self.login_dao = login_dao

    def get_employee(self, employee_id: int) -> Employee:
        return self.employee_dao.get_employee(employee_id)

    def create_employee(self, employee: Employee) -> Employee:
        return self.employee_dao.create_employee(employee)

    def get_all_employees(self) -> list[Employee]:
        return self.employee_dao.get_all_employees()

    def update_employee(self, employee: Employee) -> Employee:
        return self.employee_dao.update_employee(employee)

    def delete_employee(self, employee_id: int) -> bool:
        return self.employee_dao.delete_employee(employee_id)

    def get_all_reimbursements(self) -> list[Reimbursement]:
        return self.reimbursement_dao.get_all_reimbursements()

    def get_all_employee_reimbursements(self, employee_id: int) -> list[Reimbursement]:
        reimbursements = self.reimbursement_dao.get_all_reimbursements()
        result = [reimbursement for reimbursement in reimbursements if reimbursement.employee_id == employee_id]
        return result

    def get_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        return self.reimbursement_dao.get_reimbursement(reimbursement_id)

    def create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        # This should also raise resource not found if that employee doesn't exist
        if self.employee_dao.get_employee(reimbursement.employee_id).role_id == 1:
            raise AbuseOfPowerError(f'Managers should not make reimbursement requests')
        else:
            reimbursement.status = 'pending'
            return self.reimbursement_dao.create_reimbursement(reimbursement)

    def assert_reimbursement(self, reimbursement_id: int, status: str) -> Reimbursement:
        reimbursement = self.reimbursement_dao.get_reimbursement(reimbursement_id)
        reimbursement.status = status
        self.reimbursement_dao.update_reimbursement(reimbursement)
        return reimbursement

    def login(self, login: Login) -> Employee:
        login_check = self.login_dao.get_login_by_user_name(login.user_name)
        if login.pass_word == login_check.pass_word:
            return self.employee_dao.get_employee(login_check.employee_id)
        else:
            raise ValueError('Incorrect Username or password')

    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        self.get_reimbursement(reimbursement.re_id)
        return self.reimbursement_dao.update_reimbursement(reimbursement)
