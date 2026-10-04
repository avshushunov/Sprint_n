from api.listing_api import ListingAPI
from constants import ResponseCode, ErrorMessages


class TestDeleteListing:

    def test_delete_listing_success(self, created_listing, registered_user):
        response = ListingAPI.delete_listing(
            registered_user["token"],
            created_listing["id"],
        )

        assert response.status_code == ResponseCode.OK
        assert response.json()["message"] == ErrorMessages.DELETE_SUCCESS