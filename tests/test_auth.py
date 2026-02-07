import pytest

def test_auth_endpoints_available(client):
    
    response = client.post("/reg", json={
        "username": "test123",
        "email": "test@test.com",
        "password": "Test123!"})
    
    assert response.status_code != 500

    response = client.post("/login", data={
        "username": "test123",
        "password": "Test123!"
    })
    
    assert response.status_code != 500

    response = client.get("/user/about_user")
    
    assert response.status_code != 500

