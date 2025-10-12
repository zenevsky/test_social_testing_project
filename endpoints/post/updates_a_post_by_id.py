import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.post.models.post_model import Post
from endpoints.post.models.post_object import PostPayload


class UpdatePost(Endpoint):

    @allure.step('Run "Updates a post by id" request to update a post by id')
    def update_post(self, payload: PostPayload, post_id=None, headers=None) -> Response:
        payload = payload.to_dict()
        headers = headers if headers else self.headers
        self.response = requests.put(
            url=f'{self.url}/api/v1/post/{post_id}',
            headers=headers,
            json=payload
        )
        try:
            if self.response.status_code != 200:
                return self.response
            self.json = self.response.json()
            self.data = Post(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
