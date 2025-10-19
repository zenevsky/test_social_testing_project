import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.comment.models.comment_model import Comment
from endpoints.comment.models.comment_object import CreateCommentPayload


class CreateComment(Endpoint):

    @allure.step('Run "Create a comment" request to create a new comment')
    def create_comment(self, payload: CreateCommentPayload, headers=None) -> Response:
        payload = payload.to_dict()
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/api/v1/comment',
            headers=headers,
            json=payload
        )
        try:
            if self.response.status_code != 200:
                return self.response
            self.json = self.response.json()
            self.data = Comment(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
