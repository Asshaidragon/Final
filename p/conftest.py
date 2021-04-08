import pytest
from main import ExampleApp

@pytest.fixture
def supply_calc():
    return ExampleApp()