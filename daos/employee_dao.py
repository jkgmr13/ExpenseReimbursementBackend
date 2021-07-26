from abc import ABC, abstractmethod

from entities.employee import Employee


class EmployeeDao(ABC):

    # CRUD methods
    @abstractmethod
    def create_employee(self, employee: Employee) -> Employee:
        pass

    @abstractmethod
    def get_employee(self, employee_id) -> Employee:
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
