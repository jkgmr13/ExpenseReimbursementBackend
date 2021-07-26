from abc import ABC, abstractmethod

from entities.login import Login


class LoginDao(ABC):

    # CRUD methods
    @abstractmethod
    def create_login(self, login: Login) -> Login:
        pass

    @abstractmethod
    def get_login_by_id(self, employee_id: int) -> Login:
        pass

    @abstractmethod
    def get_login_by_user_name(self, user_name: str) -> Login:
        pass

    @abstractmethod
    def get_all_logins(self) -> list[Login]:
        pass

    @abstractmethod
    def update_login(self, login: Login) -> Login:
        pass

    @abstractmethod
    def delete_login(self, user_name: str) -> bool:
        pass
