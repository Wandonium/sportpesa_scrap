from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pprint

driver_path = '/opt/WebDriver/bin/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.ke.sportpesa.com/sports?sportId=2&section=country&countryId=16838&leagueId=78604&name=NBA")
sleep(3)

event_list = driver.find_element_by_css_selector('#mainview > div > div > div.col-xs-12.col-sm-9.list-v2 > div.list-v2-content > div:nth-child(4) > events-content > div:nth-child(4) > events-list > section')
rows = event_list.find_elements_by_css_selector('div.event-row-container.ng-scope')
highlights = []
for row in rows:
    event_dict = {}
    event_desc = row.find_element_by_css_selector('event-row > ng-include > div > div > div.event-description')
    event_info = event_desc.find_element_by_css_selector('div.event-info.event-column')
    event_dict['time'] = event_info.find_element_by_css_selector('div:nth-child(1) > time-component > span').get_attribute('innerHTML')
    event_dict['date'] = event_info.find_element_by_css_selector('div:nth-child(2) > time-component > span').get_attribute('innerHTML')
    event_dict['id'] = event_info.find_element_by_css_selector('div:nth-child(3)').get_attribute('innerHTML')
    # print(event_dict)
    event_names = event_desc.find_element_by_css_selector('div.event-names.event-column')
    event_team1 = event_names.find_element_by_css_selector('div:nth-child(1)').get_attribute('title')
    event_team2 = event_names.find_element_by_css_selector('div:nth-child(2)').get_attribute('title')
    # print(event_team1 + ", " + event_team2)
    event_dict['name'] = event_team1 + " vs " + event_team2
    event_odds = row.find_element_by_css_selector('event-row > ng-include > div > div > div.upper-to-left.event-bets.ng-scope > div:nth-child(1) > div.event-selections')
    myOdds = []
    for x in range(1,3):
        name = event_odds.find_element_by_css_selector("div:nth-child(" + str(x) + ") > div.event-text.ng-scope").get_attribute("innerHTML")
        odd = event_odds.find_element_by_css_selector("div:nth-child(" + str(x) + ") > div.ng-binding").get_attribute("innerHTML")
        myOdds.append([name, odd])
    # print(myOdds)
    event_dict['odds'] = myOdds
    highlights.append(event_dict)
print(*highlights, sep='\n')
driver.close()
driver.quit()