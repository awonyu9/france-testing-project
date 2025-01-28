from utils import create_user, create_team

def test_delete_team(page):
    # create new team
    create_team(page, "Team test")

    page.goto("/")
    # create new employees
    # bob
    create_user(page, "bob", "bob@gmail.com", "2 rue de voila", "14 avenue ok", "Paris", "75000", "2510-12-20", "CEO")
    page.get_by_role("link", name="Home").click()
    # alice
    create_user(page, "alice", "alice@gmail.com", "3 boulevard du mont", "9 rue des mwai", "Paris", "75000", "2002-02-20", "CTO")

    # add employees to team
    page.goto("/employees")
    page.get_by_role("link", name="Edit").first.click()
    page.get_by_role("link", name="Add to team").click()
    page.get_by_label("Team").click()
    page.get_by_label("Team").select_option(label="Team test team")
    page.click("text='Add'")
    page.goto("/employees")
    page.get_by_role("link", name="Edit").nth(1).click()
    page.get_by_role("link", name="Add to team").click()
    page.get_by_label("Team").click()
    page.get_by_label("Team").select_option(label="Team test team")
    page.click("text='Add'")

    # delete the team
    page.goto("/teams")
    page.click("text='Delete'")
    page.click("text='Proceed'")

    # go to employees list
    page.goto("/employees")

    assert page.get_by_role("cell", name="bob", exact=True).is_visible(), "Bob is not visible"
    assert page.get_by_role("cell", name="bob@gmail.com", exact=True).is_visible(), "Bob email is not visible"
    assert page.get_by_role("cell", name="alice", exact=True).is_visible(), "Alice is not visible"
    assert page.get_by_role("cell", name="alice@gmail.com", exact=True).is_visible(), "Alice email is not visible"