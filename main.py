from flask import Flask, request, jsonify
import logging

from daos.employee_dao import EmployeeDao
from daos.employee_dao_post import EmployeeDaoPostgres
from daos.login_dao import LoginDao
from daos.login_dao_post import LoginDaoPostgres
from daos.reimbursement_dao import ReimbursementDao
from daos.reimbursement_dao_post import ReimbursementDaoPostgres
from entities.login import Login
from entities.reimbursement import Reimbursement
from exceptions.resource_error import ResourceNotFoundError
from routes import Routes
from services.services_impl import ServiceImpl
from flask_cors import CORS, cross_origin

employee_dao: EmployeeDao = EmployeeDaoPostgres()
reimbursement_dao: ReimbursementDao = ReimbursementDaoPostgres()
login_dao: LoginDao = LoginDaoPostgres()

service = ServiceImpl(employee_dao, reimbursement_dao, login_dao)


app: Flask = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(message)s')

route = Routes(service)

@app.post('/login')
@ cross_origin()
def check_login():
    body = request.json
    try:
        login = Login(body['userName'], body['passWord'], 0)
    except ValueError as e:
        return str(e)
    except ResourceNotFoundError as e:
        return str(e), 404
    employee = service.login(login)
    print(jsonify(employee.as_json_dict()))
    return jsonify(employee.as_json_dict())
    # route.check_login()



@app.get('/reimbursements')
@ cross_origin()
def get_all_reimbursements():
    try:
        reimbursements = service.get_all_reimbursements()
        json_reimbs = [reimbursement.as_json_dict() for reimbursement in reimbursements]
        return jsonify(json_reimbs)
    except ResourceNotFoundError as e:
        return str(e), 404
    # route.get_all_reimbursements()


@app.get('/employees/<employee_id>/reimbursements')
@ cross_origin()
def get_all_employee_reimbursements(employee_id: str):
    try:
        reimbursements = service.get_all_employee_reimbursements(int(employee_id))
        json_reimbs = [reimbursement.as_json_dict() for reimbursement in reimbursements]
        return jsonify(json_reimbs)
    except ResourceNotFoundError as e:
        return str(e), 404
    # route.get_all_employee_reimbursements(employee_id)


@app.get('/employees')
@ cross_origin()
def get_employees():
    try:
        employees = service.get_all_employees()
        json_employees = [employee.as_json_dict() for employee in employees]
        return jsonify(json_employees)
    except ResourceNotFoundError as e:
        return str(e), 404
    # route.get_employees()


@app.patch('/reimbursements/<re_id>')
@ cross_origin()
def approve_or_deny_reimbursement(re_id: str):
    body = request.json
    body["reId"] = int(re_id)
    try:
        reimbursement = service.update_reimbursement(Reimbursement(body["reId"], body["employeeId"], body["amount"], body["status"], body["reason"]))
        return reimbursement.as_json_dict(), 200
    except ResourceNotFoundError as e:
        return str(e), 404
    # route.approve_or_deny_reimbursement(re_id)


@app.get('/reimbursements/<re_id>')
@ cross_origin()
def get_reimbursement(re_id: str):
    try:
        reimbursement = service.get_reimbursement(int(re_id))
        return reimbursement.as_json_dict(), 200
    except ResourceNotFoundError as e:
        return str(e), 404
    # route.get_reimbursement(re_id)


@app.post('/reimbursements')
@ cross_origin()
def create_reimbursement():
    body = request.json
    reimbursement = service.create_reimbursement(Reimbursement(*body.values()))
    return reimbursement.as_json_dict(), 201
    # route.create_reimbursement()


if __name__ == '__main__':
    app.run()
