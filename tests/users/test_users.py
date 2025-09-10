from clients.users.private_users_client import PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, UserResponseSchema
from http import HTTPStatus
from pytest import mark
from allure_commons.types import Severity
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.storys import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.json_schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from fixtures.users import UserFixture
from tools.fakers import fake
import allure

@mark.api
@mark.users
@mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.USERS)
class TestUsers:
    @mark.parametrize('domain', ('mail.com', 'gmail.com', 'example.com'))
    @allure.title('Создание пользователя')
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.severity(Severity.BLOCKER)
    @allure.sub_suite(AllureStory.CREATE_ENTITY)
    def test_create_user(self, domain, public_user_client: PublicUsersClient):
        request = CreateUserRequestSchema(email=fake.email(domain))
        response = public_user_client.create_user_api(request)
        response_data = UserResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_user_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    @allure.title('Получение текущего пользователя')
    @allure.story(AllureStory.GET_ENTITY)
    @allure.sub_suite(AllureStory.GET_ENTITY)
    @allure.severity(Severity.CRITICAL)
    def test_get_user_me(self, private_user_client: PrivateUsersClient, function_user: UserFixture):
        response = private_user_client.get_user_api(function_user.response.user.id)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_user_response(UserResponseSchema.model_validate_json(response.text), function_user.response)

        validate_json_schema(response.json(), UserResponseSchema.model_json_schema())