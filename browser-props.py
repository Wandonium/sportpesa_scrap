from selenium import webdriver
import re

#setting up path to 'chromedriver'
chromedriver_path = '/opt/WebDriver/bin/chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver_path)
driver.get('https://www.weboas.is')
print("Title: ", driver.title)
print("Current Page url: ", driver.current_url)

if re.search(r'weboas.is', driver.current_url):
    driver.save_screenshot("weboasis.png")
    print("WebOasis screenshot saved.")

#get cookie info
cookies = driver.get_cookies()
print("Cookies obtained from weboas.is")
print(cookies)
# print(driver.page_source)
driver.refresh()

driver.get('https://ke.sportpesa.com/sports')
print("Title: ", driver.title)
print("Current page url: ", driver.current_url)

if re.search(r'sportpesa', driver.current_url):
    driver.save_screenshot("sportpesa.png")
    print("Sportpesa screenshot saved.")

cookies = driver.get_cookies()
print("Current Page url: ", driver.current_url)
driver.back()   #History back action
print("Page URL (Back): ", driver.current_url)
driver.forward()    #History forward action
print("Page URL (Forward): ", driver.current_url)
driver.close()  #close browser
driver.quit()   #quit webdriver