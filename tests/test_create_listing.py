from api.listing_api import ListingAPI
from constants import ResponseCode
from data.test_data import NEW_LISTING


class TestCreateListing:

    def test_create_listing_success(self, registered_user, listing_cleanup):
        response = ListingAPI.create_listing(registered_user["token"], NEW_LISTING)
        listing_cleanup.append(response.json()["id"])

        assert response.status_code == ResponseCode.CREATED
        assert response.json()["name"] == NEW_LISTING["name"]
        assert response.json()["category"] == NEW_LISTING["category"]
        assert response.json()["id"]