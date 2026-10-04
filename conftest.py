import pytest

from api.listing_api import ListingAPI
from api.user_api import UserAPI
from data.test_data import DEFAULT_PASSWORD, DEFAULT_USER_NAME, NEW_LISTING
from helpers.helpers import generate_unique_email


@pytest.fixture
def user_body():
    return {
        "email": generate_unique_email(),
        "password": DEFAULT_PASSWORD,
        "name": DEFAULT_USER_NAME,
    }


@pytest.fixture
def registered_user(user_body):
    response = UserAPI.register(user_body["email"], user_body["password"], user_body["name"])
    token = response.json()["access_token"]["access_token"]
    return {
        "email": user_body["email"],
        "password": user_body["password"],
        "name": user_body["name"],
        "token": token,
    }


@pytest.fixture
def another_user():
    email = generate_unique_email()
    response = UserAPI.register(email, DEFAULT_PASSWORD, DEFAULT_USER_NAME)
    token = response.json()["access_token"]["access_token"]
    return {
        "email": email,
        "password": DEFAULT_PASSWORD,
        "name": DEFAULT_USER_NAME,
        "token": token,
    }


@pytest.fixture
def created_listing(registered_user):
    response = ListingAPI.create_listing(registered_user["token"], NEW_LISTING)
    listing = response.json()
    yield listing
    ListingAPI.delete_listing(registered_user["token"], listing["id"])


@pytest.fixture
def listing_cleanup(registered_user):
    listing_ids = []
    yield listing_ids
    for listing_id in listing_ids:
        ListingAPI.delete_listing(registered_user["token"], listing_id)