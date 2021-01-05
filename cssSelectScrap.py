from lxml import html
import requests
from lxml.cssselect import CSSSelector
url = 'https://developer.ibm.com/announcements/category/data-science/?fa=date%3ADESC&fb='
url_get = requests.get(url)
tree = html.document_fromstring(url_get.content)

announcements = []
#content > div > div > div.cpt-archive-new > div.search-results > div > div:nth-child(2) > div.bx--row.bx--no-gutter--right.code-card-grid > div:nth-child(1)
#content > div > div > div.cpt-archive-new > div.search-results > div > div:nth-child(2) > div.bx--row.bx--no-gutter--right.code-card-grid > div:nth-child(12)
articles = tree.cssselect('#content > div > div > div.cpt-archive-new > div.search-results > div > div:nth-child(2) > div.bx--row.bx--no-gutter--right.code-card-grid')

parent = "#content > div > div > div.cpt-archive-new > div.search-results > div > div:nth-child(2) > div.bx--row.bx--no-gutter--right.code-card-grid >"
for i in range(12):
    index = i + 1
    child = parent + "div:nth-child(" + str(index) + ")"
    article = tree.cssselect(child)
    link = article[0].cssselect('a.developer--card__block_link')[0].get('href')
    atype = article[0].cssselect('a > h5.developer--card__type > span')[0].text.strip()
    title = article[0].cssselect('a > div.developer--card__body > h3 > span')[0].text_content()
    adate = article[0].cssselect('a > div.developer--card__bottom > p > span')[0].text
    announcements.append([link, atype, title, adate])

print(announcements)