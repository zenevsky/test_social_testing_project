import os
import allure


class Endpoint:
    url = 'http://facetest.qa-practice.com'
    payload = None
    response = None
    json = None
    data = None
    headers = {'Content-type': 'application/json', 'Authorization': os.getenv("API_TOKEN")}

    @allure.step('Check response status')
    def check_that_status_is(self, expected_status):
        actual_status = self.response.status_code
        assert actual_status == expected_status, f'Expected {expected_status}, but got {actual_status}'

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
