from pyquery import PyQuery as pq
import requests

dataSet = list()
sourceUrl = 'https://developer.ibm.com/announcements/'

def read_url(url):
    """ Read given url. Returns pyquery object for page content """
    pagesource = requests.get(url).content
    return pq(pagesource)

def get_details(page):
    """ read 'page' url and append list of queried items to dataSet """
    response = read_url(page)

    articles = response.find('.developer--card > a.developer--card__block_link')
    print("\nTotal articles found:", articles.__len__(), ' in Page: ', page)

    for article in articles.items():
        link = article.attr('href')
        adate = article.find('div.developer--card__bottom > p > span').text()
        atype = article.find('h5.developer--card__type > span').text().strip()
        title = article.find('div.developer--card__body > h3 > span').text().encode('utf-8')

        if link:
            link = str(link).replace('/announcements/', mainUrl)
            dataSet.append([link, atype, adate, title])

if __name__ == '__main__':
    mainUrl = sourceUrl + "category/data-science/?fa=date:DESC&fb="
    pageUrls = [sourceUrl + "category/data-science/page/%(page)s?fa=date:DESC&fb=" % {'page': page} for page in range(1, 3)]

    for pages in pageUrls:
        get_details(pages)

    print("\nTotal articles collected: ", len(dataSet))
    print(dataSet)