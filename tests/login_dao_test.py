from daos.employee_dao import EmployeeDao
from daos.employee_dao_post import EmployeeDaoPostgres
from daos.login_dao_post import LoginDaoPostgres
from entities.employee import Employee
from entities.login import Login
from daos.login_dao import LoginDao
from exceptions.uniqueness_error import UniquenessError


login_dao: LoginDao = LoginDaoPostgres()
employee_dao: EmployeeDao = EmployeeDaoPostgres()

test_employee_id = 0
test2_employee_id = 0


def test_create_login():
    global test_employee_id
    global test2_employee_id
    employee = Employee(0, 'Jerry', 'Smith', 15)
    employee2 = Employee(0, 'Jerry', 'Smith', 15)
    employee = employee_dao.create_employee(employee)
    employee2 = employee_dao.create_employee(employee2)
    login = Login("Stever", "Ochinang", employee.emp_id)
    test_employee_id = employee.emp_id
    test2_employee_id = employee2.emp_id
    login = login_dao.create_login(login)
    assert login is not None


def test_get_login():
    global test_employee_id
    login2 = login_dao.get_login_by_id(test_employee_id)
    assert login2.user_name == "Stever"


def test_get_login2():
    login = Login("asdf", "asdf", 7)
    login_dao.create_login(login)
    login2 = login_dao.get_login_by_user_name("asdf")
    assert login2.employee_id == 7


def test_get_all_logins():
    global test2_employee_id
    login_dao.create_login(Login("StiSti2", "rich", test2_employee_id))
    logins = login_dao.get_all_logins()
    assert len(logins) >= 2


def test_update_login():
    global test_employee_id
    login1 = login_dao.get_login_by_id(test_employee_id)
    login1.user_name == "jack"
    login2 = login_dao.update_login(login1)
    assert login1.user_name == login2.user_name


def test_delete_login():
    assert login_dao.delete_login(test_employee_id)
    assert login_dao.delete_login(7)
    assert login_dao.delete_login(test2_employee_id)



