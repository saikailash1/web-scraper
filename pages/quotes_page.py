from selenium.webdriver.support.ui import Select

from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self):
        return [
            QuoteParser(e)
            for e in self.browser.find_elements_by_css_selector(QuotesPageLocators.QUOTE)
        ]

    @property
    def author_dropdown(self):
        element = self.browser.find_element_by_css_selector(QuotesPageLocators.AUTHOR_DROPDOWN)
        return Select(element)

    @property
    def tags_dropdown(self):
        alltags = self.browser.find_element_by_css_selector(QuotesPageLocators.TAG_DROPDOWN)
        return Select(alltags)

    def get_all_tags(self):
        return [option.text.strip() for option in self.tags_dropdown.options]

    def select_author(self, author_name):
        self.author_dropdown.select_by_visible_text(author_name)

    def select_tags(self, tag_name):
        self.tags_dropdown.select_by_visible_text(tag_name)
