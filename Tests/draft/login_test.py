import requests

def test_login_():
    result = requests.post('https://kasta.ua/api/v2/login/', json={"email": "yfk73402@bcaoo.com", "password": "23423wqq"})
    assert 200 == result.status_code
    cookie = {'modnakasta_sessionid': result.cookies.get("modnakasta_sessionid")}

def test_wishlist():
    result = requests.post('https://kasta.ua/me/wishlist/', cookies={"name": "modnakasta_sessionid"})
    assert 200 == result.status_code
    response_json = result.json={"id": "176869889", "index": "1"}


def test_logout():
    result = requests.post("https://kasta.ua/api/v2/logout/")
    assert 200 == result.status_code
