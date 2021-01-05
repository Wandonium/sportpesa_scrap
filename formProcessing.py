from pyquery import PyQuery as pq
import requests
mainUrl = "http://toscrape.com/"
searchUrl = "http://quotes.toscrape.com/search.aspx"
filterUrl = "http://quotes.toscrape.com/filter.aspx"
quoteUrl = "http://quotes.toscrape.com/"
authorTags = [('Albert Einstein', 'success'), ('Thomas A. Edison', 'inspirational')]

def processRequests(url, params={}, customheaders={}):
    if len(params) > 0:
        response = requests.post(url, data=params, headers=customheaders)
    else:
        response = requests.get(url)
    return pq(response.text)

if __name__ == '__main__':
    for authorTag in authorTags:
        authorName, tagName = authorTag

        #Step 1: load searchUrl
        searchResponse = processRequests(searchUrl)
        author = searchResponse.find('select#author option:contains("' + authorName + '")').attr('value')
        viewState = searchResponse.find('input#__VIEWSTATE').attr('value')
        tag = searchResponse.find('select#tag option').text()

        # print("Author: ", author)
        # print("ViewState: ", viewState)
        # print("Tag: ", tag)

        #Step2: load filterUrl with author and default tag
        params = {
            'author': author,
            'tag': tag,
            '__VIEWSTATE': viewState
        }
        customheaders = {
            'Accept': 'text/html, application/xhtml+xml, application/xml;q=0.9, image/webp, image/apng, */*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': searchUrl
        }

        filterResponse = processRequests(filterUrl, params, customheaders)
        viewstate = filterResponse.find('input#__VIEWSTATE').attr('value')
        tagSuccess = filterResponse.find('select#tag option:contains("' + tagName + '")').attr('value')
        submitButton = filterResponse.find('input[name="submit_button"]').attr('value')

        # print("Author: ", author)
        # print("ViewState: ", viewstate)
        # print("Tag: ", tagSuccess)
        # print("Submit: ", submitButton)

        #Step 3: load filterUrl with author and defined tag
        params = {'author': author, 'tag': tagSuccess, 'submit_button': submitButton, '__VIEWSTATE': viewstate}
        customheaders = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': filterUrl
        }

        finalResponse = processRequests(filterUrl, params, customheaders)

        #Step 4: Extract results
        quote = finalResponse.find('div.quote span.content').text()
        quotesAuthor = finalResponse.find('div.quote span.author').text()
        message = finalResponse.find('div.quote span.tag').text()
        print("Quote: ", quote, "\nAuthor: ", quotesAuthor, "\nMessage: ", message)