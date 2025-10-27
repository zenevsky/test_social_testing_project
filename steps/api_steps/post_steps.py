import allure
from endpoints.post.creates_a_new_post import CreatePost
from endpoints.post.deletes_a_post_by_id import DeletePost
from endpoints.post.updates_a_post_by_id import UpdatePost
from endpoints.post.get_post_by_id import GetPost
from endpoints.post.find_all_posts import FindAllPosts
from endpoints.post.find_all_posts_by_container import FindAllPostsByContainer
from endpoints.post.upload_files_to_post_by_id import UploadFilesToPost
from endpoints.post.models.post_object import PostPayload
from endpoints.post.models.file_object import UploadFilePayload


class PostSteps:

    def __init__(
            self,
            create_post_endpoint: CreatePost,
            delete_post_endpoint: DeletePost,
            update_post_endpoint: UpdatePost = None,
            get_post_endpoint: GetPost = None,
            find_all_posts_endpoint: FindAllPosts = None,
            find_all_by_container_endpoint: FindAllPostsByContainer = None,
            upload_files_endpoint: UploadFilesToPost = None
    ):
        self.create_post_endpoint = create_post_endpoint
        self.delete_post_endpoint = delete_post_endpoint
        self.update_post_endpoint = update_post_endpoint
        self.get_post_endpoint = get_post_endpoint
        self.find_all_posts_endpoint = find_all_posts_endpoint
        self.find_all_by_container_endpoint = find_all_by_container_endpoint
        self.upload_files_endpoint = upload_files_endpoint

    # ================= CREATE POST =================
    @allure.step('Create a new post successfully')
    def create_post_successful(self, payload: PostPayload):
        self.create_post_endpoint.create_post(payload, 2)
        self.create_post_endpoint.check_that_status_is_200()
        self.create_post_endpoint.check_message_value(payload)
        return self.create_post_endpoint.data

    @allure.step('Create a new post without auth')
    def create_post_without_auth(self, payload: PostPayload):
        self.create_post_endpoint.create_post(payload, 2, headers={'Content-type': 'application/json'})
        self.create_post_endpoint.check_that_status_is_401()

    @allure.step('Create a new post with invalid payload')
    def create_post_invalid_payload(self, payload: PostPayload):
        self.create_post_endpoint.create_post(payload, 2)
        self.create_post_endpoint.check_that_status_is_400()
        self.create_post_endpoint.check_error_message_is('Validation failed')

    # ================= DELETE POST =================
    @allure.step('Delete post successfully')
    def delete_post_successful(self, post_id: int):
        self.delete_post_endpoint.delete_post(post_id)
        self.delete_post_endpoint.check_that_status_is_200()

    @allure.step('Delete post without auth')
    def delete_post_without_auth(self, post_id: int):
        self.delete_post_endpoint.delete_post(post_id, headers={'Content-type': 'application/json'})
        self.delete_post_endpoint.check_that_status_is_401()

    @allure.step('Delete post created by another user')
    def delete_post_by_another_user(self, post_id: int):
        self.delete_post_endpoint.delete_post(post_id)
        self.delete_post_endpoint.check_that_status_is_403()
        self.delete_post_endpoint.check_error_message_is('You are not allowed to delete this content!')

    @allure.step('Delete non-existing post')
    def delete_post_non_existing(self, post_id: int):
        self.delete_post_endpoint.delete_post(post_id)
        self.delete_post_endpoint.check_that_status_is_404()
        self.delete_post_endpoint.check_error_message_is('Content record not found!')

    # ================= GET POST =================
    @allure.step('Get post successfully')
    def get_post_successful(self, post_id: int):
        self.get_post_endpoint.get_post(post_id)
        self.get_post_endpoint.check_that_status_is_200()
        self.get_post_endpoint.check_that_id_is_correct(post_id)
        return self.get_post_endpoint.data

    @allure.step('Get post without auth')
    def get_post_without_auth(self, post_id: int):
        self.get_post_endpoint.get_post(post_id, headers={'Content-type': 'application/json'})
        self.get_post_endpoint.check_that_status_is_401()

    @allure.step('Get non-existing post')
    def get_post_non_existing(self, post_id: int):
        self.get_post_endpoint.get_post(post_id)
        self.get_post_endpoint.check_that_status_is_404()

    # ================= UPDATE POST =================
    @allure.step('Update post successfully')
    def update_post_successful(self, post_id: int, payload: PostPayload):
        self.update_post_endpoint.update_post(payload, post_id)
        self.update_post_endpoint.check_that_status_is_200()
        self.update_post_endpoint.check_message_value(payload)

    @allure.step('Update post with invalid payload')
    def update_post_invalid_payload(self, post_id: int, payload: PostPayload):
        self.update_post_endpoint.update_post(payload, post_id)
        self.update_post_endpoint.check_that_status_is_400()
        self.update_post_endpoint.check_error_message_is('Validation failed')

    @allure.step('Update post created by another user')
    def update_post_by_another_user(self, post_id: int, payload: PostPayload):
        self.update_post_endpoint.update_post(payload, post_id)
        self.update_post_endpoint.check_that_status_is_403()
        self.update_post_endpoint.check_error_message_is('You are not allowed to update this content!')

    @allure.step('Update non-existing post')
    def update_post_non_existing(self, post_id: int, payload: PostPayload):
        self.update_post_endpoint.update_post(payload, post_id)
        self.update_post_endpoint.check_that_status_is_404()
        self.update_post_endpoint.check_error_message_is('Request object not found!')

    @allure.step('Update post without auth')
    def update_post_without_auth(self, post_id: int, payload: PostPayload):
        self.update_post_endpoint.update_post(payload, post_id, headers={'Content-type': 'application/json'})
        self.update_post_endpoint.check_that_status_is_401()

    # ================= FIND ALL POSTS =================
    @allure.step('Find all posts successfully')
    def find_all_posts_successful(self):
        self.find_all_posts_endpoint.find_all_posts()
        self.find_all_posts_endpoint.check_that_status_is_200()

    @allure.step('Find all posts without auth')
    def find_all_posts_without_auth(self):
        self.find_all_posts_endpoint.find_all_posts(headers={'Content-type': 'application/json'})
        self.find_all_posts_endpoint.check_that_status_is_401()

    # ================= FIND ALL POSTS BY CONTAINER =================
    @allure.step('Find all posts by container successfully')
    def find_all_posts_by_container_successful(self, container_id: int):
        self.find_all_by_container_endpoint.find_all_posts_by_container(container_id)
        self.find_all_by_container_endpoint.check_that_status_is_200()
        self.find_all_by_container_endpoint.check_content_container_id_value(container_id)

    @allure.step('Find posts by non-existing container')
    def find_all_posts_by_container_non_existing(self, container_id: int):
        self.find_all_by_container_endpoint.find_all_posts_by_container(container_id)
        self.find_all_by_container_endpoint.check_that_status_is_404()

    @allure.step('Find posts by container without auth')
    def find_all_posts_by_container_without_auth(self, container_id: int):
        self.find_all_by_container_endpoint.find_all_posts_by_container(container_id,
                                                                        headers={'Content-type': 'application/json'})
        self.find_all_by_container_endpoint.check_that_status_is_401()

    # ================= UPLOAD FILES =================
    @allure.step('Upload files successfully')
    def upload_files_successful(self, payload: UploadFilePayload, post_id: int):
        self.upload_files_endpoint.upload_files(payload, post_id)
        self.upload_files_endpoint.check_that_status_is_200()

    @allure.step('Upload files without auth')
    def upload_files_without_auth(self, payload: UploadFilePayload, post_id: int):
        self.upload_files_endpoint.upload_files(payload, post_id, headers={'Content-Type': 'multipart/form-data'})
        self.upload_files_endpoint.check_that_status_is_401()
