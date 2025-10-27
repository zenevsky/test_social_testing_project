import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.post.models.post_model import DataContainerModel


class FindAllPostsByContainer(Endpoint):

    @allure.step('Run "Find all posts by container" request to get all posts by container')
    def find_all_posts_by_container(self, container_id=None, params=None, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.get(
            url=f'{self.url}/api/v1/post/container/{container_id}',
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

    @allure.step('Check container_id value')
    def check_content_container_id_value(self, container_id):
        for post in self.data.results:
            assert post.content.metadata.contentcontainer_id == container_id
