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
        assert self.response.status_code == 200

    @allure.step('Check that 400 error received')
    def check_that_status_is_400(self):
        assert self.response.status_code == 400

    @allure.step('Check that response is 401')
    def check_that_status_is_401(self):
        assert self.response.status_code == 401

    @allure.step('Check that response is 403')
    def check_that_status_is_403(self):
        assert self.response.status_code == 403

    @allure.step('Check that 404 error received')
    def check_that_status_is_404(self):
        assert self.response.status_code == 404

    @allure.step('Check that response data corresponds request payload')
    def check_response_data(self, payload):
        payload_dict = payload.to_dict()
        for field, value in payload_dict.items():
            assert getattr(self.data, field) == value
