from playwright.sync_api import Page, expect


class GooglePage:
    def __init__(self, page):
        self.page = page
        self.start_button = page.locator("//button_xPath")
        self.stop_button = page.locator("")
        self.search_field = page.locator("")

    def search_for_phrase(self, phrase):
        self.search_field.fill(phrase)
