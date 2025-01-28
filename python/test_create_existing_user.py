from utils import getPageInput


def test_create_existing_user(page):
    user_name = "John Doe"
    user_email = "email@gmail.com"
    user_address = "Address 1"
    user_address2 = "Address 2"
    user_city = "Paris"
    user_zip = "75001"
    user_hiring_date = "2025-01-17"
    user_job_title = "Manager"

    page.goto("https://f.se1.hr.dmerej.info/add_employee")

    name_input = getPageInput(page, "name")
    email_input = getPageInput(page, "email")
    address1_input = getPageInput(page, "address_line1")
    address2_input = getPageInput(page, "address_line2")
    city_input = getPageInput(page, "city")
    zip_input = getPageInput(page, "zip_code")
    hiring_date_input = getPageInput(page, "hiring_date")
    job_title_input = getPageInput(page, "job_title")

    name_input.fill(user_name)
    email_input.fill(user_email)
    address1_input.fill(user_address)
    address2_input.fill(user_address2)
    city_input.fill(user_city)
    zip_input.fill(user_zip)
    hiring_date_input.fill(user_hiring_date)
    job_title_input.fill(user_job_title)
    page.click("text='Add'")

    assert page.is_visible(f"td:has-text('{user_name}')")
    assert page.is_visible(f"td:has-text('{user_email}')")

    page.goto("https://f.se1.hr.dmerej.info/add_employee")
    name_input.fill(user_name)
    email_input.fill(user_email)
    address1_input.fill(user_address)
    address2_input.fill(user_address2)
    city_input.fill(user_city)
    zip_input.fill(user_zip)
    hiring_date_input.fill(user_hiring_date)
    job_title_input.fill(user_job_title)
    page.click("text='Add'")

    email_occurrences = page.locator(f"text={user_email}").count()
    assert email_occurrences == 1, f"Expected 1 occurrence of email '{user_email}', but found {email_occurrences}. ""The user may have been created twice."
