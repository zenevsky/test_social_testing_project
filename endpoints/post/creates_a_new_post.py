import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.post.models.post_model import Post
from endpoints.post.models.post_object import PostPayload


class CreatePost(Endpoint):

    @allure.step('Run "Creates a new post" request to create a new post')
    def create_post(self, payload: PostPayload, container_id=None, headers=None) -> Response:
        payload = payload.to_dict()
        headers = headers if headers else self.headers
        self.response = requests.post(
            url=f'{self.url}/api/v1/post/container/{container_id}',
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
