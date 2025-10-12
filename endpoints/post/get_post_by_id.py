import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.post.models.post_model import Post


class GetPost(Endpoint):

    @allure.step('Run "Get post by id" request to get post by id')
    def get_post(self, post_id=None, params=None, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/api/v1/post/{post_id}',
            headers=headers,
            params=params
        )
        try:
            if self.response.status_code != 200:
                return self.response
            self.json = self.response.json()
            self.data = Post(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response

    @allure.step("Check that ID is correct")
    def check_that_id_is_correct(self, post_id):
        assert self.data.id == post_id

    @allure.step("Check state value is")
    def check_state_value_is(self, state):
        assert self.data.content.metadata.state == state
