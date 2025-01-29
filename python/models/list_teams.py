from models.Page import Page


class ListTeamsPage(Page):
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("/teams")

    def is_team_visible(self, team_name):
        return self.page.is_visible(f"td:has-text('{team_name}')")
