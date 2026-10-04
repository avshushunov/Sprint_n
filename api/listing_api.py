import requests
from constants import URL, Endpoints


IMAGE_PATH = "assets/listing.png"

class ListingAPI:

    @staticmethod
    def create_listing(token, body):
        files = {"images": open(IMAGE_PATH, "rb")}
        return requests.post(
            URL.BASE_URL + Endpoints.CREATE_LISTING,
            data=body,
            files=files,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
        )

    @staticmethod
    def update_listing(token, listing_id, body):
        files = {"images": open(IMAGE_PATH, "rb")}
        return requests.patch(
            URL.BASE_URL + Endpoints.UPDATE_LISTING + str(listing_id),
            data=body,
            files=files,
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
        )

    @staticmethod
    def delete_listing(token, listing_id):
        return requests.delete(
            URL.BASE_URL + Endpoints.DELETE_LISTING + str(listing_id),
            headers={"Authorization": f"Bearer {token}"},
            verify=False,
        )