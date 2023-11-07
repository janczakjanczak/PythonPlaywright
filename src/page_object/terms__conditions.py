from playwright.sync_api import Page, expect


class TermsConditions:
    def __init__(self, page: Page):
        self.page = page
        self.acceptAllButton = page.locator("//div[text()='Zaakceptuj wszystko']")
        self.rejectAllButton = page.locator("//div[text()='Odrzuć wszystko']")
        self.termsMainHeader = page.locator("//h1[text()='Zanim przejdziesz do Google']")

    def navigate(self):
        self.page.goto("https://www.google.com/")

    def accept_all(self):
        self.acceptAllButton.click()

    def reject_all(self):
        self.rejectAllButton.click()
