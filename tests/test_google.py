from playwright.sync_api import Page, expect
from src.page_object.search_page import SearchPage
from src.page_object.terms__conditions import TermsConditions
from src.page_object.change_language import ChangeLanguage


def test_if_we_can_accept_all_conditions(page: Page):
    trms = TermsConditions(page)
    trms.navigate()
    # dodać sprawdzenie np po nagłówku
    trms.accept_all()


def test_if_we_can_change_language(page: Page):
    trms = TermsConditions(page)
    trms.navigate()
    trms.changeLanguage()


def test_search_phrase(page: Page):
    trms = TermsConditions(page)
    trms.navigate()
    trms.accept_all()

    search_page = SearchPage(page)
    search_page.search("Ania")
    search_page.search()
