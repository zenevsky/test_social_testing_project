import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.comment.models.comment_model import Comment


class GetComment(Endpoint):

    @allure.step('Run "Get comment by id" request to get comment by id')
    def get_comment(self, comment_id=None, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/api/v1/comment/{comment_id}',
            headers=headers
        )
        try:
            if self.response.status_code != 200:
                return self.response
            self.json = self.response.json()
            self.data = Comment(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response

    @allure.step("Check that ID is correct")
    def check_that_id_is_correct(self, comment_id):
        assert self.data.id == comment_id
