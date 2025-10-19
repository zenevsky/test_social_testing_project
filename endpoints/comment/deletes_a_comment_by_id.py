import json

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint


class DeleteComment(Endpoint):

    @allure.step('Run "Delete a comment by id" request to delete a comment by id')
    def delete_comment(self, comment_id=None, headers=None) -> Response:
        headers = headers if headers else self.headers
        self.response = requests.delete(
            url=f'{self.url}/api/v1/comment/{comment_id}',
            headers=headers,
        )
        try:
            if self.response.status_code != 200:
                return self.response
            self.json = self.response.json()
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
