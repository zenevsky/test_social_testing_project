import pytest
import allure

from endpoints.post.models.file_object import UploadFilePayload, FileItem
from utils.file_helpers import get_test_file_path


@pytest.mark.api
@allure.feature('Post')
@allure.story('Upload files to Post by ID')
class TestUploadFilesToPostById:

    @pytest.mark.high
    @allure.title('Upload files to post successfully')
    def test_upload_files_successful(self, post_steps, create_and_delete_post):
        test_file = get_test_file_path("test_image.jpg")
        payload = UploadFilePayload(
            files=[FileItem(path=test_file, file_name="test_image.jpg", mime_type="image/jpeg")])
        post_steps.upload_files_successful(payload, create_and_delete_post.data.id)

    @pytest.mark.high
    @allure.title('Fail to upload files without authorization')
    def test_upload_files_without_auth(self, post_steps, create_and_delete_post):
        test_file = get_test_file_path("test_image.jpg")
        payload = UploadFilePayload(
            files=[FileItem(path=test_file, file_name="test_image.jpg", mime_type="image/jpeg")])
        post_steps.upload_files_without_auth(payload, create_and_delete_post.data.id)
