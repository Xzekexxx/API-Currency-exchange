import pytest
from unittest.mock import AsyncMock
from fastapi.testclient import TestClient

from app.main import app
from app.database.database import get_session


@pytest.fixture
def client():
    
    mock_db = AsyncMock()
    
    def override_get_db():
        yield mock_db
    
    app.dependency_overrides[get_session] = override_get_db
    
    with TestClient(app) as c:
        yield c
    
    app.dependency_overrides.clear()