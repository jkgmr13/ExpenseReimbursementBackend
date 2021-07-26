

from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao_post import ReimbursementDaoPostgres
from entities.reimbursement import Reimbursement

reimbursement_dao: ReimbursementDao = ReimbursementDaoPostgres()


def test_create_reimbursement():
    reimbursement = Reimbursement(0, 1, 100, 'pending', "Cuz why not")
    reimbursement = reimbursement_dao.create_reimbursement(reimbursement)
    assert reimbursement.re_id != 0


def test_get_reimbursement():
    reimbursement = Reimbursement(0, 1, 100, 'pending', "Cuz Why Not")
    reimbursement = reimbursement_dao.create_reimbursement(reimbursement)
    reimbursement2 = reimbursement_dao.get_reimbursement(reimbursement.re_id)
    assert reimbursement2.re_id == reimbursement.re_id


def test_get_all_reimbursement():
    assert len(reimbursement_dao.get_all_reimbursements()) >= 2


def test_update_reimbursement():
    reimbursement = Reimbursement(0, 2, 100, 'pending', "Cuz Why Not2")
    reimbursement = reimbursement_dao.create_reimbursement(reimbursement)
    reimbursement = reimbursement_dao.update_reimbursement(Reimbursement(reimbursement.re_id, 1, 500, 'Approved', "Cuz I said so"))
    assert reimbursement.employee_id == 1


def test_delete_reimbursement():
    reimbursement = Reimbursement(0, 2, 100, 'Approved', "Cuz I said so again")
    reimbursement = reimbursement_dao.create_reimbursement(reimbursement)
    assert reimbursement_dao.delete_reimbursement(reimbursement.re_id)
