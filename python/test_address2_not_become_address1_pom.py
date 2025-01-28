from models.add_new_employee import AddNewEmployeePage 
from models.edit_address import EditAddressPage

from utils import get_employeeId_by_email


def test_address2_not_become_address1_pom(page):
    user_name = "John Doe"
    user_email = "email@gmail.com"
    user_address1 = "Address 1"
    user_address2 = "Address 2"
    user_city = "Paris"
    user_zip = "75001"
    user_hiring_date = "2025-01-17"
    user_job_title = "Manager"

    add_new_employee_page = AddNewEmployeePage(page)
    add_new_employee_page.navigate()
    add_new_employee_page.fill(user_name, user_email, user_address1, user_address2, user_city, user_zip, user_hiring_date, user_job_title)
    add_new_employee_page.add()


    edit_address_page = EditAddressPage(page)
    edit_address_page.navigate(get_employeeId_by_email(page, user_email))
    address2 = edit_address_page.address2_input.input_value()
    edit_address_page.update()    
    
    edit_address_page.navigate(get_employeeId_by_email(page, user_email))

    address1 = edit_address_page.address1_input.input_value()
    updated_address2 = edit_address_page.address1_input.input_value()

    assert updated_address2 != address1, f"Address 2 ('{updated_address2}') unexpectedly matches Address 1 ('{address1}')."
