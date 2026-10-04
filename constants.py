class URL:
    BASE_URL = "https://qa-desk.education-services.ru/api"


class Endpoints:
    SIGNUP = "/signup"
    SIGNIN = "/signin"
    CREATE_LISTING = "/create-listing"
    UPDATE_LISTING = "/update-offer/"
    DELETE_LISTING = "/listings/"


class ResponseCode:
    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    UNAUTHORIZED = 401


class ErrorMessages:
    DUPLICATE_EMAIL = "Почта уже используется"
    FORBIDDEN_EDIT = "Оффер не найден или у вас нет прав на его редактирование"
    DELETE_SUCCESS = "Объявление удалено успешно"