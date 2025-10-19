import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.comment.models.comment_model import DataContainerModel


class FindCommentsByContent(Endpoint):

    @allure.step('Run "Find comments by content" request to get comments by content')
    def find_comments_by_content(self, content_id=None, params=None, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/api/v1/comment/content/{content_id}',
            headers=headers,
            params=params
        )
        try:
            if self.response.status_code != 200:
                return self.response
            self.json = self.response.json()
            self.data = DataContainerModel(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response

    @allure.step("Check that ID is correct")
    def check_that_id_is_correct(self, comment_id):
        assert self.data.id == comment_id
