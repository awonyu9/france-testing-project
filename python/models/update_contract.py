from models.Page import Page


class UpdateContractPage(Page):
    def __init__(self, page):
        self.page = page
        self.user_id = page.url.split("/")[-1]
        self.hiring_date_input = self.getPageInput(page, "hiring_date")
        self.job_title_input = self.getPageInput(page, "job_title")
        self.update_button = page.get_by_role("button", name="Update")

    def navigate(self):
        self.page.goto(f"/employee/{self.user_id}/contract")

    def fill(self, hiring_date, job_title):
        self.hiring_date_input.fill(hiring_date)
        self.job_title_input.fill(job_title)

    def update(self):
        self.update_button.click()
