import pytest
import requests

@pytest.mark.parametrize("id, expected_name", [
    (1, "Leanne Graham"),
    (2, "Ervin Howell")
])
def test_get_user_name(id, expected_name):
    # 这里的 URL 是 JSONPlaceholder 提供的真实接口
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["name"] == expected_name