import pytest

@pytest.fixture(scope="function", autouse=True)
def reset_database(page):
    page.goto("/reset_db")
    page.locator("button:has-text('proceed')").click()

def test_create_team(page):
    # Create a team 
    page.goto("/")
    page.goto("/add_team")
    name_input = page.locator('input[name="name"]')
    team_name = "my team"
    name_input.fill(team_name)
    page.click("text='Add'")

    # Goto the team list
    page.goto("/teams")

    # Check the new team is there
    assert page.is_visible(f"td:has-text('{team_name}')")

def test_create_user_with_info(page):
    page.goto("https://f.se1.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("Name")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("email@gmail.Com")
    page.get_by_role("textbox", name="Email").press("ArrowLeft")
    page.get_by_role("textbox", name="Email").press("ArrowLeft")
    page.get_by_role("textbox", name="Email").fill("email@gmail.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("Test address 1")
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill("Test address 2")
    page.get_by_role("textbox", name="City").click()
    page.get_by_role("textbox", name="City").fill("City test")
    page.get_by_role("spinbutton", name="Zip code").click()
    page.get_by_role("spinbutton", name="Zip code").fill("75000")
    page.get_by_role("textbox", name="Hiring date").fill("2025-01-17")
    page.get_by_role("textbox", name="Job title").click()
    page.get_by_role("textbox", name="Job title").fill("TEstt")
    page.get_by_role("button", name="Add").click()

    assert page.get_by_role("cell", name="Name", exact=True).is_visible()
    assert page.get_by_role("cell", name="email@gmail.com", exact=True).is_visible()

