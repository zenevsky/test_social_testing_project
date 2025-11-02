import allure
from endpoints.comment.create_a_comment import CreateComment
from endpoints.comment.deletes_a_comment_by_id import DeleteComment
from endpoints.comment.update_a_comment_by_id import UpdateComment
from endpoints.comment.get_comment_by_id import GetComment
from endpoints.comment.find_comments_by_content import FindCommentsByContent
from endpoints.comment.find_comments_by_object import FindCommentsByObject
from endpoints.comment.models.comment_object import CreateCommentPayload, UpdateCommentPayload


class CommentSteps:
    def __init__(
            self,
            create_comment_endpoint: CreateComment = None,
            delete_comment_endpoint: DeleteComment = None,
            update_comment_endpoint: UpdateComment = None,
            get_comment_endpoint: GetComment = None,
            find_by_content_endpoint: FindCommentsByContent = None,
            find_by_object_endpoint: FindCommentsByObject = None,
    ):
        self.create_comment_endpoint = create_comment_endpoint
        self.delete_comment_endpoint = delete_comment_endpoint
        self.update_comment_endpoint = update_comment_endpoint
        self.get_comment_endpoint = get_comment_endpoint
        self.find_by_content_endpoint = find_by_content_endpoint
        self.find_by_object_endpoint = find_by_object_endpoint

    # ================= CREATE =================
    @allure.step("Create comment successfully")
    def create_comment_successful(self, payload: CreateCommentPayload):
        self.create_comment_endpoint.create_comment(payload)
        self.create_comment_endpoint.check_that_status_is_200()
        return self.create_comment_endpoint.data

    @allure.step("Create comment without auth")
    def create_comment_without_auth(self, payload: CreateCommentPayload):
        self.create_comment_endpoint.create_comment(payload, headers={'Content-type': 'application/json'})
        self.create_comment_endpoint.check_that_status_is_401()

    # ================= DELETE =================
    @allure.step("Delete comment successfully")
    def delete_comment_successful(self, comment_id: int):
        self.delete_comment_endpoint.delete_comment(comment_id)
        self.delete_comment_endpoint.check_that_status_is_200()

    @allure.step("Delete comment without auth")
    def delete_comment_without_auth(self, comment_id: int):
        self.delete_comment_endpoint.delete_comment(comment_id, headers={'Content-type': 'application/json'})
        self.delete_comment_endpoint.check_that_status_is_401()

    # ================= UPDATE =================
    @allure.step("Update comment successfully")
    def update_comment_successful(self, payload: UpdateCommentPayload, comment_id: int):
        self.update_comment_endpoint.update_comment(payload, comment_id)
        self.update_comment_endpoint.check_that_status_is_200()

    @allure.step("Update comment without auth")
    def update_comment_without_auth(self, payload: UpdateCommentPayload, comment_id: int):
        self.update_comment_endpoint.update_comment(payload, comment_id, headers={'Content-type': 'application/json'})
        self.update_comment_endpoint.check_that_status_is_401()

    # ================= GET =================
    @allure.step("Get comment successfully")
    def get_comment_successful(self, comment_id: int):
        self.get_comment_endpoint.get_comment(comment_id)
        self.get_comment_endpoint.check_that_status_is_200()
        self.get_comment_endpoint.check_that_id_is_correct(comment_id)
        return self.get_comment_endpoint.data

    @allure.step("Get comment without auth")
    def get_comment_without_auth(self, comment_id: int):
        self.get_comment_endpoint.get_comment(comment_id, headers={'Content-type': 'application/json'})
        self.get_comment_endpoint.check_that_status_is_401()

    @allure.step("Get not existing comment")
    def get_not_existing_comment(self, comment_id: int = 999999999999999999999):
        self.get_comment_endpoint.get_comment(comment_id)
        self.get_comment_endpoint.check_that_status_is_404()

    # ================= FIND =================
    @allure.step("Find comments by content")
    def find_comments_by_content_successful(self, content_id: int):
        self.find_by_content_endpoint.find_comments_by_content(content_id)
        self.find_by_content_endpoint.check_that_status_is_200()
        return self.find_by_content_endpoint.data

    @allure.step("Find comments by content without auth")
    def find_comments_by_content_without_auth(self, content_id: int):
        self.find_by_content_endpoint.find_comments_by_content(content_id, headers={'Content-type': 'application/json'})
        self.find_by_content_endpoint.check_that_status_is_401()

    @allure.step("Find comments by object")
    def find_comments_by_object_successful(self, params: dict):
        self.find_by_object_endpoint.find_comments_by_object(params=params)
        self.find_by_object_endpoint.check_that_status_is_200()
        return self.find_by_object_endpoint.data

    @allure.step("Find comments by object without auth")
    def find_comments_by_object_without_auth(self, params: dict):
        self.find_by_object_endpoint.find_comments_by_object(params=params,
                                                             headers={'Content-type': 'application/json'})
        self.find_by_object_endpoint.check_that_status_is_401()
