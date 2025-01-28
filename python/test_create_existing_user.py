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