from playwright.sync_api import Page, expect


class ChangeLanguage:
    def __init__(self, page: Page):
        self.page = page
        self.changeLanguageButton = page.locator("//*[@id='vc3jof']")

    def changeLanguage(self):
        self.changeLanguageButton.click()
