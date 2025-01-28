from models.list_employees import ListEmployeesPage
from models.add_new_employee import AddNewEmployeePage

def test_address2_not_become_address1_pom(page):
    add_new_employee_page = AddNewEmployeePage(
        page)
    add_new_employee_page.navigate()
    add_new_employee_page.fill("Mark Doe", "email@email.com", "address 1", "address 2", "Paris", "75017", "2025-01-28", "CEO")
    add_new_employee_page.add()

    list_employees_page = ListEmployeesPage(page)
    list_employees_page.navigate()
    list_employees_page.edit_employee(0)

    page.locator('a[href$="address"]').click()
    address2 = page.locator('input[name="address_line2"]').input_value()
    page.click("text='Update'")
    page.get_by_role("link", name="Update address").click()

    address1 = page.locator('input[name="address_line1"]').input_value()
    updated_address2 = page.locator('input[name="address_line2"]').input_value()
    assert updated_address2 != address1, f"Address 2 ('{updated_address2}') unexpectedly matches Address 1 ('{address1}')."