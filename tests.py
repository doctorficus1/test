import pytest
import requests

BASE_URL = "https://petstore.swagger.io/v2"

class TestPet:
    def test_add_pet(self):
        payload = {"id": 228, "name": "XD", "status": "available"}
        response = requests.post(f"{BASE_URL}/pet", json=payload)
        assert response.status_code == 200
        assert response.json()["name"] == "XD"

    def test_get_pet_by_id(self):
        response = requests.get(f"{BASE_URL}/pet/228")
        assert response.status_code == 200
        assert response.json()["id"] == 228

    def test_update_pet(self):
        payload = {"id": 228, "name": "XD_New", "status": "sold"}
        response = requests.put(f"{BASE_URL}/pet", json=payload)
        assert response.status_code == 200
        assert response.json()["name"] == "XD_New"

    def test_find_by_status(self):
        params = {"status": "available"}
        response = requests.get(f"{BASE_URL}/pet/findByStatus", params=params)
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_delete_pet(self):
        response = requests.delete(f"{BASE_URL}/pet/228")
        assert response.status_code == 200


class TestUser:
    def test_create_user(self):
        payload = {"id": 1, "username": "testuser", "firstName": "Tyx", "password": "123"}
        response = requests.post(f"{BASE_URL}/user", json=payload)
        assert response.status_code == 200

    def test_get_user(self):
        response = requests.get(f"{BASE_URL}/user/testuser")
        assert response.status_code == 200
        assert response.json()["username"] == "testuser"

    def test_user_login(self):
        params = {"username": "testuser", "password": "123"}
        response = requests.get(f"{BASE_URL}/user/login", params=params)
        
        assert response.status_code == 200
        assert "logged in user session" in response.json()["message"]

    def test_update_user(self):
        payload = {"username": "testuser", "firstName": "Tyx_New"}
        response = requests.put(f"{BASE_URL}/user/testuser", json=payload)
        assert response.status_code == 200

    def test_delete_user(self):
        response = requests.delete(f"{BASE_URL}/user/testuser")
        assert response.status_code == 200


class TestStore:
    def test_place_order(self):
        payload = {"id": 1, "petId": 12345, "quantity": 1, "status": "placed"}
        response = requests.post(f"{BASE_URL}/store/order", json=payload)
        assert response.status_code == 200
        assert response.json()["status"] == "placed"

    def test_get_order(self):
        response = requests.get(f"{BASE_URL}/store/order/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    def test_get_inventory(self):
        response = requests.get(f"{BASE_URL}/store/inventory")
        assert response.status_code == 200
        assert isinstance(response.json(), dict)

    def test_delete_order(self):
        requests.post(f"{BASE_URL}/store/order", json={"id": 99, "petId": 1})
        response = requests.delete(f"{BASE_URL}/store/order/99")
        assert response.status_code == 200

    def test_order_not_found(self):
        response = requests.get(f"{BASE_URL}/store/order/0")
        assert response.status_code == 404