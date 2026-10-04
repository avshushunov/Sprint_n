from api.listing_api import ListingAPI
from constants import ResponseCode, ErrorMessages
from data.test_data import UPDATED_LISTING


class TestEditListing:

    def test_edit_listing_success(self, created_listing, registered_user):
        response = ListingAPI.update_listing(
            registered_user["token"],
            created_listing["id"],
            UPDATED_LISTING,
        )

        assert response.status_code == ResponseCode.OK
        assert response.json()["name"] == UPDATED_LISTING["name"]

    def test_edit_listing_by_another_user(self, created_listing, another_user):
        response = ListingAPI.update_listing(
            another_user["token"],
            created_listing["id"],
            UPDATED_LISTING,
        )

        assert response.status_code == ResponseCode.UNAUTHORIZED
        assert response.json()["message"] == ErrorMessages.FORBIDDEN_EDIT