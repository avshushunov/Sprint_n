import requests

from constants import URL, Endpoints


class UserAPI:

    @staticmethod
    def register(email, password, name):
        payload = {"email": email, "password": password, "name": name}
        return requests.post(URL.BASE_URL + Endpoints.SIGNUP, json=payload, verify=False)

    @staticmethod
    def login(email, password):
        payload = {"email": email, "password": password}
        return requests.post(URL.BASE_URL + Endpoints.SIGNIN, json=payload, verify=False)