from flask import request, jsonify

from entities.login import Login
from entities.reimbursement import Reimbursement
from exceptions.resource_error import ResourceNotFoundError
from services import service
from services.service import Service


class Routes:

    def __init__(self, service: Service):
        self.service = service

    def check_login(self):
        body = request.json
        try:
            login = Login(body['userName'], body['passWord'], 0)
        except ValueError as e:
            return str(e)
        except ResourceNotFoundError as e:
            return str(e), 404
        employee = self.service.login(login)
        print(jsonify(employee.as_json_dict()))
        return jsonify(employee.as_json_dict())

    def get_all_reimbursements(self):
        try:
            reimbursements = self.service.get_all_reimbursements()
            json_reimbs = [reimbursement.as_json_dict() for reimbursement in reimbursements]
            return jsonify(json_reimbs)
        except ResourceNotFoundError as e:
            return str(e), 404

    def get_all_employee_reimbursements(self, employee_id: str):
        try:
            reimbursements = self.service.get_all_employee_reimbursements(int(employee_id))
            json_reimbs = [reimbursement.as_json_dict() for reimbursement in reimbursements]
            return jsonify(json_reimbs)
        except ResourceNotFoundError as e:
            return str(e), 404

    def get_employees(self):
        try:
            employees = self.service.get_all_employees()
            json_employees = [employee.as_json_dict() for employee in employees]
            return jsonify(json_employees)
        except ResourceNotFoundError as e:
            return str(e), 404

    def approve_or_deny_reimbursement(self, re_id: str):
        body = request.json
        body["reId"] = int(re_id)
        try:
            reimbursement = self.service.update_reimbursement(
                Reimbursement(body["reId"], body["employeeId"], body["amount"], body["status"], body["reason"]))
            return reimbursement.as_json_dict(), 200
        except ResourceNotFoundError as e:
            return str(e), 404

    def get_reimbursement(self, re_id: str):
        try:
            reimbursement = self.service.get_reimbursement(int(re_id))
            return reimbursement.as_json_dict(), 200
        except ResourceNotFoundError as e:
            return str(e), 404

    def create_reimbursement(self):
        body = request.json
        reimbursement = self.service.create_reimbursement(Reimbursement(*body.values()))
        return reimbursement.as_json_dict(), 201
