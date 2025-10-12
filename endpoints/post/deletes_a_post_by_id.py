import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint


class DeletePost(Endpoint):

    @allure.step('Run "Deletes a post by id" request to delete a post by id')
    def delete_post(self, post_id=None, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.delete(
            url=f'{self.url}/api/v1/post/{post_id}',
            headers=headers,
        )
        try:
            if self.response.status_code != 200:
                return self.response
            self.json = self.response.json()
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
