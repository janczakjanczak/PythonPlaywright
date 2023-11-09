from playwright.sync_api import Page, expect
from src.page_object.search_page import SearchPage
from src.page_object.terms__conditions import TermsConditions
from src.page_object.change_language import ChangeLanguage


def test_if_we_can_accept_all_conditions(page: Page):
    trms = TermsConditions(page)
    trms.navigate()
    trms.accept_all()
    searchPage = SearchPage(page)
    expect(searchPage.search_input).to_be_visible()


def test_if_we_can_change_language(page: Page):
    trms = TermsConditions(page)
    trms.navigate()
    language = ChangeLanguage(page)
    language.changeLanguage()
    #page.pause()
    language.pickEnglish()
    expect(language.englishHeading).to_contain_text("Before you continue to Google")



def test_search_phrase(page: Page):
    trms = TermsConditions(page)
    trms.navigate()
    trms.accept_all()
    page.pause()
    search_page = SearchPage(page)
    search_page.search("Ania")
    
