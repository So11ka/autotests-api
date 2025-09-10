from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import TokenResponseSchema
from http import HTTPStatus
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.storys import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.json_schema import validate_json_schema
from pytest import mark
from fixtures.users import UserFixture
import allure


@mark.authentication
@allure.tag(AllureTag.AUTHENTICATION, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.parent_suite(AllureEpic.LMS)
@allure.suite(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @mark.regression
    @allure.title('Логирование пользователя')
    @allure.story(AllureStory.LOGIN)
    @allure.sub_suite(AllureStory.LOGIN)
    def test_login(self, authentication_client: AuthenticationClient, function_user: UserFixture):
        response = authentication_client.login_api(function_user.authentication_user)
        response_data = TokenResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())