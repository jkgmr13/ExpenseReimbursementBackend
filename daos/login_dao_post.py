from daos.login_dao import LoginDao
from entities.login import Login
from exceptions.resource_error import ResourceNotFoundError
from exceptions.uniqueness_error import UniquenessError
from util.postgres_con import connection


class LoginDaoPostgres(LoginDao):

    def create_login(self, login: Login) -> Login:
        sql = """insert into login values(%s, %s, %s)"""
        cursor = connection.cursor()
        cursor.execute(sql, (login.user_name, login.pass_word, login.employee_id))
        connection.commit()
        return login

    def get_login_by_id(self, employee_id) -> Login:
        sql = """select * from login where e_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError(f'No login with the id {employee_id} exists')
        else:
            return Login(*record)

    def get_login_by_user_name(self, user_name: str) -> Login:
        sql = """select * from login where user_name = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, [user_name])
        record = cursor.fetchone()
        if record is None:
            raise ResourceNotFoundError(f'No login with the id {user_name} exists')
        else:
            return Login(*record)

    def get_all_logins(self) -> list[Login]:
        sql = """select * from login"""
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        logins = [Login(*record) for record in records]
        if len(logins) == 0:
            raise ResourceNotFoundError("No logins exist")
        else:
            return logins

    def update_login(self, login: Login) -> Login:
        self.get_login_by_id(login.employee_id)
        sql = """update login set user_name = %s, pass_word = %s where e_id = %s"""
        cursor = connection.cursor()
        cursor.execute(sql, (login.user_name, login.pass_word, login.employee_id))
        connection.commit()
        return login

    def delete_login(self, employee_id: int) -> bool:
        self.get_login_by_id(employee_id)
        sql = """delete from login where e_id=%s"""
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        return True
