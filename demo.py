import requests


BASE_URL = "https://api.scripture.api.bible/v1"
ENDPOINT = "/swagger.json"


def get_info_from_api():
    info = requests.get(BASE_URL + ENDPOINT)
    return info


INFO = get_info_from_api()

STATUS_CODE = INFO.status_code
BODY = INFO.json()

print(STATUS_CODE, INFO.ok)
print(get_info_from_api())
print(dir(INFO))
print(BODY)
print(type(BODY))
