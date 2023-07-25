from playwright.sync_api import Page, expect

class GooglePage:
    def __init__(self, page_from_playwright):
        self.page = page_from_playwright
        self.start_button = page_from_playwright.locator('//button_xPath')
        self.stop_button = page_from_playwright.locator('')
        self.search_field = page_from_playwright.locator('')

    def search_for_phrase(self, phrase):
        self.search_field.fill(phrase)