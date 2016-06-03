import pytest
from pydojo import create_app
from pydojo.ext import db as db_test
from pydojo.config import TestConfig


@pytest.fixture(scope='session')
def app(request):
    app = create_app(TestConfig)
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(app, request):
    def teardown():
        db_test.drop_all()

    db_test.app = app
    db_test.create_all()

    request.addfinalizer(teardown)
    return db_test


@pytest.fixture(scope='function')
def session(db, request):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
