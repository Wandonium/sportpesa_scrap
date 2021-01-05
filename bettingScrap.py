from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import pprint

driver_path = '/opt/WebDriver/bin/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://ke.sportpesa.com/sports")
sleep(3)

def get_odds(sport):
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
        # print(event_time + ", " + event_date + ", " + event_id)
        event_names = event_desc.find_element_by_css_selector('div.event-names.event-column')
        event_team1 = event_names.find_element_by_css_selector('div:nth-child(1)').get_attribute('title')
        event_team2 = event_names.find_element_by_css_selector('div:nth-child(2)').get_attribute('title')
        # print(event_team1 + ", " + event_team2)
        event_dict['name'] = event_team1 + " vs " + event_team2
        event_odds = row.find_element_by_css_selector('event-row > ng-include > div > div > div.upper-to-left.event-bets.ng-scope > div:nth-child(1) > div.event-selections')
        myOdds = []
        myRange = range(1,4) if(sport == 'Football' or sport == 'Rugby Union' or sport == 'Handball' or sport == 'Ice Hockey') else range(1,3)
        for x in myRange:
            name = event_odds.find_element_by_css_selector("div:nth-child(" + str(x) + ") > div.event-text.ng-scope").get_attribute("innerHTML")
            odd = event_odds.find_element_by_css_selector("div:nth-child(" + str(x) + ") > div.ng-binding").get_attribute("innerHTML")
            myOdds.append([name, odd])
        # print(myOdds)
        event_dict['odds'] = myOdds
        highlights.append(event_dict)
    return highlights

menu = driver.find_elements_by_css_selector('#mainview > div > div > div.col-xs-12.col-sm-9.list-v2 > sports-menu > nav > ul > li')
for x in range(1, len(menu)):
    sport = menu[x].find_element_by_css_selector('div:nth-child(1) > span').get_attribute('translate-default')
    print("getting odds for sport: " + sport)
    sport_click = menu[x].find_element_by_css_selector('div:nth-child(1)').click()
    country_click = menu[x].find_element_by_css_selector('div:nth-child(2) > ul > li:nth-child(4) > div').click() if(sport == 'Football') else menu[x].find_element_by_css_selector('div:nth-child(2) > ul > li:nth-child(3) > div').click()
    country_list = menu[x].find_element_by_css_selector('div:nth-child(2) > ul > li:nth-child(4) > ul') if(sport == 'Football') else menu[x].find_element_by_css_selector('div:nth-child(2) > ul > li:nth-child(3) > ul')
    countries = country_list.find_elements_by_css_selector('li')
    print("no. of countries for " + sport + ": " + str(len(countries)))
    the_country_leagues = {}
    for country in countries:
        country_name = country.find_element_by_css_selector('div > span').get_attribute('innerHTML')
        country_click = country.find_element_by_css_selector('div').click()
        sleep(2)
        country_leagues = country.find_elements_by_css_selector('ul > li')
        leagues = {}
        for league in country_leagues:
        # for x in range(1):
            # league = country_leagues[x]
            league_name = league.find_element_by_css_selector('div > span').get_attribute('innerHTML')
            league.click()
            league_odds = []
            sleep(2)
            try:
                pagination = driver.find_element_by_css_selector('#mainview > div > div > div.col-xs-12.col-sm-9.list-v2 > div.list-v2-content > div:nth-child(4) > events-content > div:nth-child(4) > events-list > basic-pagination')
                pagination_links = pagination.find_elements_by_css_selector('ul > li')
                if(len(pagination_links) == 0):
                    print("only one page found for odds in " + league_name)
                    league_odds.append(get_odds(sport))
                    leagues[league_name] = league_odds
                else:
                    print(str(len(pagination_links)) + " pages found for odds in " + league_name)
                    for link in pagination_links:
                        text = link.get_attribute('innerHTML')
                        print(text)
                        if(text != "Previous" and text != "Next"):
                            print("getting odds")
                            link.click()
                            sleep(2)
                            the_odds = get_odds(sport)
                            league_odds = league_odds + the_odds
                            leagues[league_name] = league_odds
                continue
            except NoSuchElementException:
                print("No events for " + league_name + " in " + country_name)
        the_country_leagues[country_name] = leagues
    # pprint.pprint(the_country_leagues)
    with open(sport + ".txt", "w") as fout:
        fout.write(pprint.pformat(the_country_leagues))
# event_list = driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[1]/div[2]/div[3]/events-content/div[4]/events-list[1]/section/div[2]')
driver.close()
driver.quit()