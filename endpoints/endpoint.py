import os
import allure


class Endpoint:
    url = 'http://facetest.qa-practice.com'
    payload = None
    response = None
    json = None
    data = None
    headers = {'Content-type': 'application/json', 'Authorization': os.getenv("API_TOKEN")}

    @allure.step('Check that response is 200')
    def check_that_status_is_200(self):
        expected = 200
        actual = self.response.status_code
        assert actual == expected, f'Expected {expected}, but got {actual}'

    @allure.step('Check that response is 400')
    def check_that_status_is_400(self):
        expected = 400
        actual = self.response.status_code
        assert actual == expected, f'Expected {expected}, but got {actual}'

    @allure.step('Check that response is 401')
    def check_that_status_is_401(self):
        expected = 401
        actual = self.response.status_code
        assert actual == expected, f'Expected {expected}, but got {actual}'

    @allure.step('Check that response is 403')
    def check_that_status_is_403(self):
        expected = 403
        actual = self.response.status_code
        assert actual == expected, f'Expected {expected}, but got {actual}'

    @allure.step('Check that response is 404')
    def check_that_status_is_404(self):
        expected = 404
        actual = self.response.status_code
        assert actual == expected, f'Expected {expected}, but got {actual}'

    @allure.step('Check error message')
    def check_error_message_is(self, error_message):
        assert self.response.json()['message'] == error_message

    @allure.step('Check that response data corresponds request payload')
    def check_response_data(self, payload):
        payload_dict = payload.to_dict()
        for field, value in payload_dict.items():
            assert getattr(self.data, field) == value

    @allure.step('Check that message is correct')
    def check_message_value(self, payload):
        message_value = payload.data.message
        assert self.data.message == message_value


