from abc import ABC, abstractmethod

from entities.reimbursement import Reimbursement


class ReimbursementDao(ABC):

    # CRUD methods
    @abstractmethod
    def create_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def get_reimbursement(self, reimbursement_id) -> Reimbursement:
        pass

    @abstractmethod
    def get_all_reimbursements(self) -> list[Reimbursement]:
        pass

    @abstractmethod
    def update_reimbursement(self, reimbursement: Reimbursement) -> Reimbursement:
        pass

    @abstractmethod
    def delete_reimbursement(self, reimbursement_id: int) -> bool:
        pass
