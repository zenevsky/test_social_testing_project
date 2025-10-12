import allure
import pytest

from endpoints.post.models.file_object import UploadFilePayload, FileItem
from utils.file_helpers import get_test_file_path


@allure.feature('Post')
@allure.story('Upload files to Post by id')
@pytest.mark.api
class TestUploadFilesToPostById:
    @pytest.mark.high
    @allure.title('Upload files to Post by id')
    def test_upload_files_to_post_by_id(self, upload_files_to_post_endpoint, create_and_delete_post_fixture):
        test_file = get_test_file_path("test_image.jpg")

        payload = UploadFilePayload(
            files=[
                FileItem(
                    path=test_file,
                    file_name="test_image.jpg",
                    mime_type="image/jpeg"
                )
            ]
        )
        upload_files_to_post_endpoint.upload_files(payload, create_and_delete_post_fixture.data.id)
        upload_files_to_post_endpoint.check_that_status_is_200()

    @pytest.mark.high
    @allure.title('Upload files to Post by id without auth')
    def test_upload_files_to_post_by_id_without_auth(
            self,
            upload_files_to_post_endpoint,
            create_and_delete_post_fixture
    ):
        test_file = get_test_file_path("test_image.jpg")

        payload = UploadFilePayload(
            files=[
                FileItem(
                    path=test_file,
                    file_name="test_image.jpg",
                    mime_type="image/jpeg"
                )
            ]
        )
        upload_files_to_post_endpoint.upload_files(
            payload,
            create_and_delete_post_fixture.data.id,
            headers={'Content-Type': 'multipart/form-data'}
        )
        upload_files_to_post_endpoint.check_that_status_is_401()
