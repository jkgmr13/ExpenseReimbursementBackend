from daos.employee_dao import EmployeeDao
from daos.employee_dao_post import EmployeeDaoPostgres
from daos.login_dao import LoginDao
from daos.login_dao_post import LoginDaoPostgres
from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao_post import ReimbursementDaoPostgres
from entities.employee import Employee
from entities.login import Login
from exceptions.abuse_power import AbuseOfPowerError
from services.service import Service
from entities.reimbursement import Reimbursement
from unittest.mock import MagicMock

from services.services_impl import ServiceImpl

employee_dao: EmployeeDao = EmployeeDaoPostgres()
reimbursement_dao: ReimbursementDao = ReimbursementDaoPostgres()
login_dao: LoginDao = LoginDaoPostgres()
service: Service = ServiceImpl(employee_dao, reimbursement_dao, login_dao)

employee_dao.get_employee = MagicMock(return_value=Employee(1, 'Joe', 'Kell', 0))
reimbursement_dao.get_reimbursement = MagicMock(return_value=Reimbursement(1, 1, 100, '', "Reasons"))
login_dao.get_login_by_user_name = MagicMock(return_value=Login("Jacque", "Coustoue",  1))
reimbursements = [Reimbursement(1, 1, 100, '', "Reason1"), Reimbursement(2, 1, 500, "", "Reason 2"), Reimbursement(3, 2, 500, '', "Reason3")]
reimbursement_dao.get_all_reimbursements = MagicMock(return_value=reimbursements)


def test_create_reimbursement():
    reimbursement = Reimbursement(0, 1, 100, '', 'cuz why not')
    result = service.create_reimbursement(reimbursement)
    assert result.status == 'pending'


def test_assert_reimbursement():
    reimbursement = service.assert_reimbursement(1, 'approved')
    assert reimbursement.status == 'approved'


def test_login():
    login = service.login(Login("Jacque", "Coustoue", 1))
    assert login.emp_id == 1


def test_get_employees_reimbursements():
    result = service.get_all_employee_reimbursements(1)
    assert len(result) == 2



