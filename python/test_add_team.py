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
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("Name")
    page.get_by_role("textbox", name="Email").click()
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

def test_create_existing_user(page):
    user_name = "Name"
    user_email = "email@gmail.com"
    user_address = "Test address 1"
    user_address2 = "Test address 2"
    user_city = "City test"
    user_zip = "75000"
    user_hiring_date = "2025-01-17"
    user_job_title = "Test"

    page.goto("https://f.se1.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill(user_name)
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(user_email)
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill(user_address)
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill(user_address2)
    page.get_by_role("textbox", name="City").click()
    page.get_by_role("textbox", name="City").fill(user_city)
    page.get_by_role("spinbutton", name="Zip code").click()
    page.get_by_role("spinbutton", name="Zip code").fill(user_zip)
    page.get_by_role("textbox", name="Hiring date").fill(user_hiring_date)
    page.get_by_role("textbox", name="Job title").click()
    page.get_by_role("textbox", name="Job title").fill(user_job_title)
    page.get_by_role("button", name="Add").click()

    assert page.get_by_role("cell", name="Name", exact=True).is_visible()
    assert page.get_by_role("cell", name="email@gmail.com", exact=True).is_visible()

    page.goto("https://f.se1.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill(user_name)
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(user_email)
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill(user_address)
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill(user_address2)
    page.get_by_role("textbox", name="City").click()
    page.get_by_role("textbox", name="City").fill(user_city)
    page.get_by_role("spinbutton", name="Zip code").click()
    page.get_by_role("spinbutton", name="Zip code").fill(user_zip)
    page.get_by_role("textbox", name="Hiring date").fill(user_hiring_date)
    page.get_by_role("textbox", name="Job title").click()
    page.get_by_role("textbox", name="Job title").fill(user_job_title)
    page.get_by_role("button", name="Add").click()

    email_occurrences = page.locator(f"text={user_email}").count()
    assert email_occurrences == 1, f"Expected 1 occurrence of email '{user_email}', but found {email_occurrences}. ""The user may have been created twice."


def test_address2_not_become_address1(page):
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("test")
    page.locator("div").filter(has_text="Email").click()
    page.get_by_role("textbox", name="Email").fill("test@gmail.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("address1")
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line1").fill("address2")
    page.get_by_role("textbox", name="City").click()
    page.get_by_role("textbox", name="City").fill("city")
    page.get_by_role("spinbutton", name="Zip code").click()
    page.get_by_role("spinbutton", name="Zip code").fill("75000")
    page.get_by_role("textbox", name="Hiring date").fill("2025-01-15")
    page.get_by_role("textbox", name="Job title").click()
    page.get_by_role("textbox", name="Job title").fill("Tester")
    page.get_by_role("button", name="Add").click()
    page.get_by_role("link", name="Home").click()
    page.get_by_role("link", name="List employees").click()
    page.get_by_role("link", name="Edit").nth(0).click()
    page.get_by_role("link", name="Update address").click()
    address2 = page.locator("#id_address_line2").input_value()
    page.get_by_role("button", name="Update").click()
    page.get_by_role("link", name="Update address").click()

    address1 = page.locator("#id_address_line1").input_value()
    updated_address2 = page.locator("#id_address_line2").input_value()
    assert updated_address2 != address1, f"Address 2 ('{updated_address2}') unexpectedly matches Address 1 ('{address1}')."
    

def test_zipcode_cannot_be_negative(page):
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("Test User")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("testuser@gmail.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("123 Main Street")
    page.get_by_role("textbox", name="City").click()
    page.get_by_role("textbox", name="City").fill("Test City")
    page.get_by_role("spinbutton", name="Zip code").click()
    page.get_by_role("spinbutton", name="Zip code").fill("-12345")
    
    page.get_by_role("button", name="Add").click()
    
    error_message = page.locator("span.error:has-text('Invalid ZIP code')")  
    assert error_message.is_visible(), "Error message for invalid ZIP code was not displayed."
    assert page.url.endswith("/add_employee"), "Form was submitted with an invalid ZIP code."

