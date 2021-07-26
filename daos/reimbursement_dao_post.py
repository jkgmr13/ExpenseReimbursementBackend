from daos.reimbursement_dao import ReimbursementDao
from entities.reimbursement import Reimbursement
from exceptions.resource_error import ResourceNotFoundError
from util.postgres_con import connection


class ReimbursementDaoPostgres(ReimbursementDao):
    def create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        sql = """insert into reimbursement values(default, %s, %s, %s, %s) returning re_id"""
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.employee_id, reimbursement.amount, reimbursement.status, reimbursement.reason))
        reimbursement.re_id = cursor.fetchone()[0]
        connection.commit()
        return reimbursement

    def get_reimbursement(self, reimbursement_id) -> Reimbursement:
        sql = """select * from reimbursement where re_id=%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError(f'No reimbursement with id {reimbursement_id} exists')
        reimbursement = Reimbursement(*record)
        return reimbursement

    def get_all_reimbursements(self) -> list[Reimbursement]:
        sql = """select * from reimbursement"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        if len(records) == 0:
            raise ResourceNotFoundError('No reimbursements exist')
        reimbursements = [Reimbursement(*record) for record in records]
        return reimbursements

    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        self.get_reimbursement(reimbursement.re_id)
        sql = """update reimbursement set e_id=%s, amount=%s, status=%s, reason=%s  where re_id=%s"""
        cursor = connection.cursor()
        cursor.execute(sql, (reimbursement.employee_id, reimbursement.amount, reimbursement.status, reimbursement.reason, reimbursement.re_id))
        connection.commit()
        return reimbursement

    def delete_reimbursement(self, reimbursement_id: int) -> bool:
        self.get_reimbursement(reimbursement_id)
        sql = """delete from reimbursement where re_id=%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        connection.commit()
        return True
