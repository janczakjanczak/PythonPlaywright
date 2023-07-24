from playwright.sync_api import Page, expect

class GooglePage:
    def __init__(self, page_from_playwright):
        self.page = page_from_playwright
        self.start_button = page.locator('//button')
        self.stop_button = page.locator('')