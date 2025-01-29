from models.Page import Page


class EditEmployeePage(Page):
    def __init__(self, page):
        self.page = page
        self.update_basic_info_button = page.locator('a[href$="address"]')
        self.update_address_button = page.locator('a[href$="address"]')
        self.update_contract_button = page.locator('a[href$="contract"]')
        self.promote_button = page.locator('a[href$="promote"]')
        self.add_team_button = page.locator('a[href$="team"]')

    def navigate_basic_info(self):
        self.update_basic_info_button.click()

    def navigate_update_address(self):
        self.update_address_button.click()

    def navigate_contract(self):
        self.update_contract_button.click()

    def navigate_promote(self):
        self.promote_button.click()

    def navigate_team(self):
        self.add_team_button.click()
