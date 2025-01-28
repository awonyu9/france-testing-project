from models.add_new_employee import AddNewEmployeePage
from models.list_employees import ListEmployeesPage

def test_create_existing_user_pom(page):
    user_name = "John Doe"
    user_email = "email@gmail.com"
    user_address1 = "Address 1"
    user_address2 = "Address 2"
    user_city = "Paris"
    user_zip = "75001"
    user_hiring_date = "2025-01-17"
    user_job_title = "Manager"

    add_new_employee_page = AddNewEmployeePage(
        page)
    add_new_employee_page.navigate()
    add_new_employee_page.fill(user_name, user_email, user_address1, user_address2, user_city, user_zip, user_hiring_date, user_job_title
                               )
    add_new_employee_page.add()

    list_employees_page = ListEmployeesPage(page)
    list_employees_page.navigate()

    assert list_employees_page.is_name_visible(user_name)
    assert list_employees_page.is_email_visible(user_email)

    add_new_employee_page.navigate()
    add_new_employee_page.fill(user_name, user_email, user_address1, user_address2, user_city, user_zip, user_hiring_date, user_job_title)
    add_new_employee_page.add()

    list_employees_page.navigate()
    email_occurrences = list_employees_page.count_email_occurrences(user_email)
    assert email_occurrences == 1, f"Expected 1 occurrence of email '{user_email}', but found {email_occurrences}. ""The user may have been created twice."
