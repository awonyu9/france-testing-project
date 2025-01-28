import pytest

def getPageInput(page, name):
    return page.locator('input[name="' + name + '"]')

def add_employee(page, name, email, address1, address2, city, zip_code, hiring_date, job_title):
    page.goto("/add_employee")

    name_input = getPageInput(page, "name")
    email_input = getPageInput(page, "email")
    address1_input = getPageInput(page, "address_line1")
    address2_input = getPageInput(page, "address_line2")
    city_input = getPageInput(page, "city")
    zip_input = getPageInput(page, "zip_code")
    hiring_date_input = getPageInput(page, "hiring_date")
    job_title_input = getPageInput(page, "job_title")


    name_input.fill(name)
    email_input.fill(email)
    address1_input.fill(address1)
    address2_input.fill(address2)
    city_input.fill(city)
    zip_input.fill(zip_code)
    hiring_date_input.fill(hiring_date)
    job_title_input.fill(job_title)
    page.click("text='Add'")
    page.goto("/")

def test_edit_employee_hiring_date(page):

    user_name = "John Doe"
    user_email = "email@gmail.com"
    user_address = "Address 1"
    user_address2 = "Address 2"
    user_city = "Paris"
    user_zip = "75001"
    user_hiring_date = "2025-01-17"
    user_job_title = "Manager"

    add_employee(page, user_name, user_email, user_address, user_address2, user_city, user_zip, user_hiring_date, user_job_title)

    page.goto("/employees")
    page.click("text='Edit'")
    page.click("text='Update contract'")
    getPageInput(page, "hiring_date").fill("2025-01-18")
    page.click("text='Update'")

    
    hiring_date_cell = getPageInput(page, "hiring_date")
    assert hiring_date_cell.is_visible(f"td:has-text('2025-01-18')")


        
