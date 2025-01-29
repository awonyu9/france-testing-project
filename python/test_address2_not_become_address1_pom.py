from models.list_employees import ListEmployeesPage
from models.add_new_employee import AddNewEmployeePage
from models.edit_address import EditAddressPage
from models.edit_employee import EditEmployeePage

def test_address2_not_become_address1_pom(page):
    add_new_employee_page = AddNewEmployeePage(
        page)
    add_new_employee_page.navigate()
    add_new_employee_page.fill("Mark Doe", "email@email.com", "address 1", "address 2", "Paris", "75017", "2025-01-28", "CEO")
    add_new_employee_page.add()

    list_employees_page = ListEmployeesPage(page)
    list_employees_page.navigate()
    list_employees_page.edit_employee(0)

    edit_employee_page = EditEmployeePage(page)
    edit_employee_page.navigate_update_address()
    edit_address_page = EditAddressPage(page)
    edit_address_page.update()
    edit_employee_page.navigate_update_address()

    address1 = edit_address_page.get_address1()
    updated_address2 = edit_address_page.get_address2()
    assert updated_address2 != address1, f"Address 2 value('{updated_address2}') unexpectedly matches Address 1 value ('{address1}')."