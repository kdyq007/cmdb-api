# -*- coding: utf-8 -*-


from flask import jsonify
from flask import make_response
from flask_script import Manager
from flask_script import prompt_bool

from __init__ import make_app
from extensions import db
from gunicornserver import GunicornServer
from lib.exception import InvalidUsageError


app = make_app('config.cfg')


@app.errorhandler(InvalidUsageError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'message': error.description}), 404)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'message': error.description}), 400)


@app.errorhandler(401)
def auth_lack(error):
    return make_response(jsonify({'message': error.description}), 401)


@app.errorhandler(403)
def exception_403(error):
    return make_response(jsonify({'message': error.description}), 403)


@app.errorhandler(405)
def exception_405(error):
    return make_response(jsonify({'message': error.description}), 405)


@app.errorhandler(500)
def server_error(error):
    return make_response(jsonify({"message": error.description}), 500)


manager = Manager(app)



@manager.command
def db_setup():
    "create all database tables"
    db.create_all()


@manager.command
def db_dropall():
    "drop all databse tables"
    if prompt_bool("Are you sure ? You will lose all your data !"):
        db.drop_all()


manager.add_command("run", GunicornServer())

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] != "runserver":
        manager.run(default_command="run")
    else:
        host = app.config.get("HOST")
        port = app.config.get("PORT")
        app.run(host=host, port=port, debug=True)
