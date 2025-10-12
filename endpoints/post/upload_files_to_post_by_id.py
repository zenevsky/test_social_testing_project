import json
import os

import allure
import requests
from requests import Response

from endpoints.endpoint import Endpoint
from endpoints.post.models.file_object import UploadFilePayload


class UploadFilesToPost(Endpoint):

    @allure.step('Run "Upload files to Post by id" request')
    def upload_files(self, payload: UploadFilePayload, post_id: int, headers=None) -> Response:
        upload_files_headers = {'Authorization': os.getenv("API_TOKEN")}
        headers = headers if headers else upload_files_headers

        files = [
            ("files", (file_item.file_name, open(file_item.path, "rb"), file_item.mime_type))
            for file_item in payload.files
        ]

        data = {}
        if payload.hidden_in_stream:
            data["hiddenInStream"] = json.dumps(payload.hidden_in_stream)

        self.response = requests.post(
            url=f"{self.url}/api/v1/post/{post_id}/upload-files",
            headers=headers,
            files=files,
            data=data,
        )

        try:
            if self.response.status_code != 200:
                return self.response
            self.json = self.response.json()
        except json.JSONDecodeError as e:
            print(f"JSON Decode Error: {e}")
        return self.response
