from my_service import MyService, Request, Response
from single_sign_on import SSOToken, SingleSignonRegistry
from unittest.mock import Mock
import pytest

@pytest.fixture
def stub_registry():
    return Mock(SingleSignonRegistry)

def test_hello_name(stub_registry):
    service = MyService(stub_registry)
    response = service.handle(Request("Emily"), SSOToken())
    assert response.text == "Hello Emily!"

def test_single_sign_on(stub_registry):
    service = MyService(stub_registry)
    token = SSOToken
    service.handle(Request("Emily"), token)
    stub_registry.is_valid.assert_called_with(token)

def test_single_sign_on_with_invalid_token(stub_registry):
    stub_registry.is_valid.return_value = False
    service = MyService(stub_registry)
    token = SSOToken
    response = service.handle(Request("Emily"), token)
    stub_registry.is_valid.assert_called_with(token)
    assert response.text == "Please sign in"

def confirm_token(correct_token):
    def is_valid(actual_token):
        if actual_token != correct_token:
            raise ValueError("Wrong Token Received!")
    return is_valid

def test_single_sign_on_receives_correct_token(stub_registry):
    correct_token = SSOToken()
    stub_registry.is_valid = Mock(side_effect=confirm_token(correct_token))
    service = MyService(stub_registry)
    service.handle(Request("Emily"), correct_token)
    stub_registry.is_valid.assert_called()
    