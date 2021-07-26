from abc import ABC, abstractmethod

from entities.employee import Employee
from entities.login import Login
from entities.reimbursement import Reimbursement


class Service(ABC):

    # CRUD methods
    @abstractmethod
    def get_employee(self, employee_id: int) -> Employee:
        pass

    @abstractmethod
    def create_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def get_all_employees(self) -> list[Employee]:
        pass

    @abstractmethod
    def update_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def delete_employee(self, employee_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_reimbursements(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def get_all_employee_reimbursements(self, employee_id: int) -> list[Reimbursement]:
        pass

    @abstractmethod
    def get_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement_id: int) -> Reimbursement:
        pass

    # business Logic methods
    @abstractmethod
    def create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def assert_reimbursement(self, reimbursement_id: int, status: str) -> Reimbursement:
        pass

    @abstractmethod
    def login(self, user_name: str, pass_word: str) -> Employee:
        pass

