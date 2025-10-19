import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.comment.models.comment_model import Comment
from endpoints.comment.models.comment_object import UpdateCommentPayload


class UpdateComment(Endpoint):

    @allure.step('Run "Update a comment by id" request to update a comment by id')
    def update_comment(self, payload: UpdateCommentPayload, comment_id=None, headers=None) -> Response:
        payload = payload.to_dict()
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/api/v1/comment/{comment_id}',
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
