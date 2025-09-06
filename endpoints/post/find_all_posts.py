import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.post.models.post_pydantic_model import DataContainerModel


class FindAllPosts(Endpoint):

    @allure.step('Run "Find all posts" request to get all posts')
    def find_all_posts(self, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/api/v1/post',
            headers=headers
        )
        try:
            if self.response.status_code != 200:
                return self.response
            self.json = self.response.json()
            self.data = DataContainerModel(**self.json)
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
