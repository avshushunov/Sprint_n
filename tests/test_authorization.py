from api.user_api import UserAPI
from constants import ResponseCode


class TestAuthorization:

    def test_authorization_success(self, registered_user):
        response = UserAPI.login(registered_user["email"], registered_user["password"])

        assert response.status_code == ResponseCode.CREATED
        assert response.json()["user"]["email"] == registered_user["email"]
        assert response.json()["token"]["access_token"]