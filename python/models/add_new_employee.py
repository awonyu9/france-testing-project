from utils import getPageInput


class AddNewEmployeePage:
    def __init__(self, page):
        self.page = page

        self.name_input = getPageInput(page, "name")
        self.email_input = getPageInput(page, "email")
        self.address1_input = getPageInput(page, "address_line1")
        self.address2_input = getPageInput(page, "address_line2")
        self.city_input = getPageInput(page, "city")
        self.zip_input = getPageInput(page, "zip_code")
        self.hiring_date_input = getPageInput(page, "hiring_date")
        self.job_title_input = getPageInput(page, "job_title")

        self.add_button = page.get_by_role("button", name="Add")

    def navigate(self):
        self.page.goto("/add_employee")

    def fill(self, name, email, address1, address2, city, zip, hiring_date, job_title):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.address1_input.fill(address1)
        self.address2_input.fill(address2)
        self.city_input.fill(city)
        self.zip_input.fill(zip)
        self.hiring_date_input.fill(hiring_date)
        self.job_title_input.fill(job_title)

    def add(self):
        self.add_button.click()
