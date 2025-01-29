from models.Page import Page


class AddTeamPage(Page):
    def __init__(self, page):
        self.page = page
        self.name_input = self.getPageInput(page, "name")
        self.add_button = page.get_by_role("button", name="Add")

    def navigate(self):
        self.page.goto("/add_team")

    def fill(self, name):
        self.name_input.fill(name)

    def add(self):
        self.add_button.click()
