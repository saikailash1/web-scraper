from selenium import webdriver
from pages.quotes_page import QuotesPage

chrome = webdriver.Chrome(executable_path="/home/dogg/Downloads/chromedriver")
chrome.get("http://quotes.toscrape.com/search.aspx")
page = QuotesPage(chrome)

author = 'Bob Marley'
page.select_author(author)

tages = page.get_all_tags()
print('[{}]'.format('|'.join(tages)))
tag = input('enter a choice')
page.select_tags(tag)
