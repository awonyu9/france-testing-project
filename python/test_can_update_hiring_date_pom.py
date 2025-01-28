from models.add_new_employee import AddNewEmployeePage
from models.list_employees import ListEmployeesPage
from models.update_contract import UpdateContractPage


def test_can_update_hiring_date_pom(page):
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
    list_employees_page.edit_employee(0)

    update_contract_page = UpdateContractPage(page)
    update_contract_page.navigate()

    assert update_contract_page.hiring_date_input.is_enabled(
    ), "Hiring date field is not enabled"
