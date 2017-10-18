import logging

from connexion import NoContent

from orm import User, init_db


logging.basicConfig()
logger = logging.getLogger('api')
logger.setLevel(logging.DEBUG)

db_session = init_db('sqlite:///test.db')


def list_users():
    logger.info("List users.")

    response = list()

    users = db_session.query(User).all()

    for user in users:
        response.append(user.dump())

    logger.debug(response)

    return response


def create_user(body):
    logger.debug(body)

    user = User(**body)

    logger.debug(user.username)

    db_session.add(user)
    db_session.commit()


def get_user_by_username(username):
    logger.debug(username)

    user = db_session.query(User) \
                     .filter(User.username == username) \
                     .one_or_none()

    return user.dump() or (NoContent, 200)


def update_user(username, body):

    user = db_session.query(User) \
                     .filter(User.username == username) \
                     .one_or_none()

    user.update(**body)

    logger.debug(user.email)

    db_session.add(user)
    db_session.commit()

    return NoContent, 200


def delete_user(username):

    db_session.query(User).filter(User.username == username).delete()

    db_session.commit()

    return NoContent, 204
