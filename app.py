import logging

from flask import Flask, jsonify, request, abort, make_response

import models


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


app = Flask(__name__)


def format_user(result):
    user_id, username, name, email = result

    user = {
        'id': user_id,
        'username': username,
        'name': name,
        'email': email}

    return user


@app.route('/user', methods=['GET'])
@app.route('/user/<username>', methods=['GET'])
def get_users(username=None):
    if username is None:
        # Quando o usuário não é informado, retorna todos os usuários...
        users = models.select_all()

        # ... em formato de lista.
        response = list()

        for u in users:
            user = format_user(u)

            response.append(user)

    else:
        # Quando é informado o usuário, retorna somente este.
        u = models.select_by_username(username)

        if u is None:
            abort(404)

        response = format_user(u)

    return jsonify(response)


@app.route('/user', methods=['POST'])
def create_user():
    user = request.get_json()

    if user is None:
        abort(404)

    logger.debug(user)

    result = models.insert_user(user['username'], user['name'], user['email'])

    if not result:
        abort(409)

    return make_response(jsonify('OK'), 201)


@app.route('/user/<username>', methods=['PUT'])
def update_user(username=None):
    user = request.get_json()

    if user is None:
        abort(404)

    logger.debug(user)

    result = models.update_user(username, user['name'], user['email'])

    if not result:
        abort(409)

    return make_response(jsonify('OK'), 204)


@app.route('/user/<username>', methods=['DELETE'])
def delete_user(username=None):
    if username is None:
        abort(404)

    logger.debug(username)

    result = models.delete_user(username)

    if not result:
        abort(404)

    return make_response(jsonify('OK'), 204)


@app.errorhandler(404)
def not_found(error):
    msg = {'error': 'Not found'}

    return make_response(jsonify(msg), 404)


@app.errorhandler(409)
def already_exists(error):
    msg = {'error': 'Already exists'}

    return make_response(jsonify(msg), 409)


if __name__ == '__main__':
    logger.info('Starting app...')

    app.run(debug=True)
