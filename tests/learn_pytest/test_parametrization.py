from _pytest.fixtures import fixture
from pytest import mark
from _pytest.fixtures import SubRequest

@mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

@mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@mark.parametrize("host", ["https://dev.company.com", "https://stable.company.com", "https://prod.company.com"])
@mark.parametrize("os", ["macos", "windows", "linux", "debian"])
def test_host1(host: str, os: str):
    assert len(os + host) != 0

@fixture(params=["https://dev.company.com", "https://stable.company.com", "https://prod.company.com"])
def host(request: SubRequest):
    return request.param

def test_host(host: str):
    print(host)

users = {
    '+7000000012': 'Account with a lot of money',
    '+7000000022': 'Account without money',
    '+7000000032': 'Banned account'
}

@mark.parametrize('phone_number', users.keys(), ids=lambda phone_number: f'{phone_number} - {users[phone_number]}')
def test_user_account(phone_number: str):
    pass

@mark.parametrize("user", ["Alice", "Bob"])
class TestUserOperations:
    def test_balance(self, user):
        pass

    @mark.parametrize("operation", ["deposit", "withdraw"])
    def test_operations(self, user, operation):
        pass