import logging

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

logging.basicConfig()
logger = logging.getLogger('api')
logger.setLevel(logging.DEBUG)

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    firstname = Column(String(80), nullable=False)
    lastname = Column(String(80), nullable=False)
    email = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), nullable=False)

    def dump(self):
        # Pega as propriedades do objeto.
        props = vars(self).items()

        # Pega todas as propriedades que são públicas.
        public = [(k, v) for k, v in props if not k.startswith('_')]

        # Converte lista de tuplas em um dicionário.
        return dict(public)

    def update(self, **kwargs):
        items = kwargs

        logger.debug(items)

        if 'email' in items:
            self.email = items['email']

        if 'firstname' in items:
            self.firstname = items['firstname']

        if 'lastname' in items:
            self.lastname = items['lastname']

        if 'username' in items:
            self.username = items['username']


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True)
    db_session = scoped_session(sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)

    return db_session
