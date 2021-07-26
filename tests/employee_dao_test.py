
from daos.employee_dao import EmployeeDao
from daos.employee_dao_post import EmployeeDaoPostgres
from entities.employee import Employee
from exceptions.resource_error import ResourceNotFoundError

employee_dao: EmployeeDao = EmployeeDaoPostgres()


def test_create_employee():
    employee = Employee(0, 'testyMc', 'test', 0)
    employee_dao.create_employee(employee)
    assert employee.emp_id != 0


def test_get_employee():
    employee = Employee(0, 'testyMc', 'secondTest', 0)
    employee = employee_dao.create_employee(employee)
    employee2 = employee_dao.get_employee(employee.emp_id)
    assert employee2.emp_id == employee.emp_id


def test_get_all_employee():
    assert len(employee_dao.get_all_employees()) >= 2


def test_update_employee():
    employee = Employee(0, 'testyMc', 'thirdTest', 0)
    employee = employee_dao.create_employee(employee)
    employee = employee_dao.update_employee(Employee(employee.emp_id, 'updated', 'questionmark?', 0))
    assert employee.first_name == "updated"


def test_delete_employee():
    employee = Employee(0, 'DeletedMc', 'DeletedFace', 0)
    employee = employee_dao.create_employee(employee)
    assert employee_dao.delete_employee(employee.emp_id)


def test_delete_invalid():
    try:
        employee_dao.delete_employee(9999)
        assert False
    except ResourceNotFoundError as e:
        assert True
