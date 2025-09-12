from pytest import fixture

from tools.allure.enviroment import create_allure_environment_file


@fixture(scope='session', autouse=True)
def save_allure_environment_file():
    yield
    create_allure_environment_file()