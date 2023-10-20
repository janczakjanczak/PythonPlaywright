import re
from playwright.sync_api import Page, expect
from src.page_object.search_page import SearchPage
from src.page_object.google_page import GooglePage


def test_homepage(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

    # create a locator
    get_started = page.get_by_role("link", name="Get started")

    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/docs/intro")

    # Click the get started link.
    get_started.click()

    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*intro"))


def test_search(page: Page):
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("search query")


def test_new(page: Page):
    google_page = GooglePage(page)
    google_page.start_button.click()
    google_page.search_for_phrase()
