from models.Page import Page


class EditAddressPage(Page):
    def __init__(self, page):
        self.page = page

        self.address1_input = self.getPageInput(page, "address_line1")
        self.address2_input = self.getPageInput(page, "address_line2")
        self.city_input = self.getPageInput(page, "city")
        self.zip_code_input = self.getPageInput(page, "zip_code")
        self.update_button = page.get_by_role("button", name="Update")

    def navigate(self, employee_id):
        self.page.goto("/employee/" + employee_id + "/address")

    def fill(self, address_line1, address_line2, city, zip_code):
        self.name_input.fill(address_line1)
        self.name_input.fill(address_line2)
        self.name_input.fill(city)
        self.name_input.fill(zip_code)

    def update(self):
        self.update_button.click()
