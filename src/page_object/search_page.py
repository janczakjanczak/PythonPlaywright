class SearchPage:
    def __init__(self, page):
        self.page = page
        self.search_term_input = page.locator("//textarea[@title='Szukaj']")

    def search(self, text:str):
        self.search_term_input.fill(text)
        self.search_term_input.press("Enter")
