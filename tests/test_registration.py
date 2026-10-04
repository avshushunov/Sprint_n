from api.user_api import UserAPI
from constants import ResponseCode, ErrorMessages


class TestRegistration:

    def test_registration_success(self, user_body):
        response = UserAPI.register(user_body["email"], user_body["password"], user_body["name"])

        assert response.status_code == ResponseCode.CREATED
        assert response.json()["user"]["email"] == user_body["email"]
        assert response.json()["access_token"]["access_token"]

    def test_registration_with_existing_email(self, registered_user):
        response = UserAPI.register(
            registered_user["email"],
            registered_user["password"],
            registered_user["name"],
        )

        assert response.status_code == ResponseCode.BAD_REQUEST
        assert response.json()["message"] == ErrorMessages.DUPLICATE_EMAIL