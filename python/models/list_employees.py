class ListEmployeesPage:
    def __init__(self, page):
        self.page = page
        self.employees_rows = page.locator("table.table tbody tr")
        self.edit_button = "td:nth-child(4) a"
        self.delete_button = "td:nth-child(5) a"

    def navigate(self):
        self.page.goto("/employees")

    def edit_employee(self, index):
        employee_row = self.employees_rows.nth(index)
        employee_row.locator(self.edit_button).click()

    def delete_employee(self, index):
        employee_row = self.employees_rows.nth(index)
        employee_row.locator(self.delete_button).click()

    def count_email_occurrences(self, email):
        return self.page.locator(f"text={email}").count()
