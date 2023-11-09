from playwright.sync_api import Page, expect


class ChangeLanguage:
    def __init__(self, page: Page):
        self.page = page
        self.changeLanguageButton = page.locator("//*[@id='vc3jof']")
       # self.englishLanguageButton = page.locator("//*[@id='tbTubd']/div/div/li[2]") - sprawdzic czemu nie dzialal 
        self.englishLanguageButton = page.get_by_role("menuitem", name="English (United Kingdom)")
        # czy aby na pewno definiowanie lokatora tutaj jest poprawne? Jesli tak to jak sie do niego odwolac w tescie 
        self.englishHeading = page.get_by_role("heading", name="Before you continue to Google")
    def changeLanguage(self):
        self.changeLanguageButton.click()

    def pickEnglish(self):
        self.englishLanguageButton.click()
