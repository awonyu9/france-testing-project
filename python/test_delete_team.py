import pytest

@pytest.fixture(scope="function", autouse=True)
def reset_database(page):
    page.goto("/reset_db")
    page.locator("button:has-text('proceed')").click()

def test_delete_team(page):
    # create new team
    page.get_by_role("link", name="List teams").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Create new team").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Team test")
    page.get_by_role("button", name="Add").click()
    page.get_by_role("link", name="Home").click()

    # create new employees
    # bob
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("bob")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("bob@gmail.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("2 rue de voila")
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill("14 avenue ok")
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("Paris")
    page.get_by_placeholder("Zip code").click()
    page.get_by_placeholder("Zip code").fill("75000")
    page.get_by_placeholder("Hiring date").fill("2510-12-20")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("CEO")
    page.get_by_role("button", name="Add").click()
    page.get_by_role("link", name="Home").click()
    # alice
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("alice")
    page.locator("div").filter(has_text="Email").click()
    page.get_by_placeholder("Email").fill("alice@gmail.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("3 boulevard du mont")
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill("9 rue des mwai")
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("Paris")
    page.get_by_placeholder("Zip code").click()
    page.get_by_placeholder("Zip code").fill("75000")
    page.get_by_placeholder("Hiring date").fill("2002-02-20")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("CTO")
    page.get_by_role("button", name="Add").click()

    # add employees to team
    page.get_by_role("link", name="Edit").first.click()
    page.get_by_role("link", name="Add to team").click()
    page.get_by_label("Team").click()
    page.get_by_label("Team").select_option(label="Team test team")
    page.get_by_role("button", name="Add").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="List employees").click()
    page.get_by_role("link", name="Edit").nth(1).click()
    page.get_by_role("link", name="Add to team").click()
    page.get_by_label("Team").click()
    page.get_by_label("Team").select_option(label="Team test team")
    page.get_by_role("button", name="Add").click()
    page.get_by_role("link", name="Home").click()

    # delete the team
    page.get_by_role("link", name="List teams").click()
    page.get_by_role("link", name="Delete").click()
    page.get_by_role("button", name="Proceed").click()

    # go to employees list
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="List employees").click()

    assert page.get_by_role("cell", name="bob", exact=True).is_visible()
    assert page.get_by_role("cell", name="bob@gmail.com", exact=True).is_visible()
    assert page.get_by_role("cell", name="alice", exact=True).is_visible()
    assert page.get_by_role("cell", name="alice@gmail.com", exact=True).is_visible()