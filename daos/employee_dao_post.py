from daos.employee_dao import EmployeeDao
from entities.employee import Employee
from exceptions.resource_error import ResourceNotFoundError
from util.postgres_con import connection


class EmployeeDaoPostgres(EmployeeDao):
    def create_employee(self, employee: Employee) -> Employee:
        sql = """insert into employee values(default, %s, %s, %s) returning employee_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (employee.first_name, employee.last_name, employee.role_id))
        connection.commit()
        employee_id = cursor.fetchone()[0]
        employee.emp_id = employee_id
        return employee

    def get_employee(self, employee_id: int) -> Employee:
        sql = """select * from employee where employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError(f'No employee with the id {employee_id} exists')
        else:
            return Employee(*record)

    def get_all_employees(self) -> list[Employee]:
        sql = """select * from employee"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        employees = [Employee(*record) for record in records]
        if len(employees) == 0:
            raise ResourceNotFoundError("No employees exist")
        else:
            return employees

    def update_employee(self, employee: Employee) -> Employee:
        self.get_employee(employee.emp_id)
        sql = """update employee set first_name = %s, last_name = %s, role_id = %s where employee_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (employee.first_name, employee.last_name, employee.role_id, employee.emp_id))
        connection.commit()
        return employee

    def delete_employee(self, employee_id: int) -> bool:
        self.get_employee(employee_id)
        sql = """delete from employee where employee_id=%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        return True
