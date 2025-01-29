class Page:
    def getPageInput(self, page, name):
        return page.locator('input[name="' + name + '"]')
