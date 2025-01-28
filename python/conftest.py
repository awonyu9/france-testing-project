import pytest

@pytest.fixture(scope="function", autouse=True)
def reset_database(page):
    page.goto("/reset_db")
    page.locator("button:has-text('proceed')").click()
