from pytest import fixture

@fixture(autouse=True)
def auto_use():
    print('[AUTOUSE] Автоматически подставляется в аргументы')

@fixture(scope='session')
def settings():
    print('[SESSION] Один раз в сессию')

@fixture(scope='class')
def user():
    print('[CLASS] В каждом классе')

@fixture(scope='function')
def users_client():
    print('[FUNCTION] В каждом тесте')

class TestUserFlow:
    def test_user_update(self, users_client, settings, user):
        ...
    def test_user_can_create_course(self, users_client, settings, user):
        ...

class TestUserAccount:
    def test_user_account(self, users_client, settings, user):
        ...

