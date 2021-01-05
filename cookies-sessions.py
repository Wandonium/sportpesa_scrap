from pyquery import PyQuery as pq
import requests
mainUrl = "http://toscrape.com/"
loginUrl = "http://quotes.toscrape.com/login"
quoteUrl = "http://quotes.toscrape.com/"

def getCustomHeaders(cookieHeader):
    return {
        'Host': 'quotes.toscrape.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Referer': 'http://quotes.toscrape.com/login',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': cookieHeader
    }

def responseCookies(response):
    headers = response.headers
    cookies = response.cookies
    # print("Headers: ", headers)
    # print("Cookies: ", cookies)
    return headers['Set-Cookie']

if __name__ == '__main__':
    response = requests.get(loginUrl)
    setCookie = responseCookies(response)
    # print("Set-Cookie: ", setCookie)
    responseA = pq(response.text)
    print(responseA)
    csrf_token = responseA.find('input[name="csrf_token"]').attr('value')
    username = responseA.find('input[id="username"]').attr('name')
    password = responseA.find('input[id="password"]').attr('name')

    params = {username: 'test', password: 'test', 'csrf_token': csrf_token}
    print(params)

    customHeaders = getCustomHeaders(setCookie)
    # print("customHeaders: ", customHeaders)
    response = requests.post(loginUrl, data=params)
    setCookie = responseCookies(response)
    # print("Set-Cookie: ", setCookie)

    responseB = pq(response.text)
    print("responseB: ", responseB)
    logoutText = responseB.find('a[href*="logout"]').text()
    logoutLink = responseB.find('a[href*="logout"]').attr('href')

    print("Current Page: ", response.url)
    print("Confirm Login: ", responseB.find('.row h2').text())
    print("Logout Info: ", logoutText, " & ", logoutLink)