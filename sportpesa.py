from selenium import webdriver
from time import sleep

driver_path = '/opt/WebDriver/bin/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://ke.sportpesa.com/sports")
sleep(3)
# //*[@id="mainview"]/div/div/div[1]/div[2]/div[3]
# //*[@id="mainview"]/div/div/div[1]/div[2]/div[3]/events-content/div[4]/events-list[1]/section/div[2]/div[2]/div/event-row/ng-include/div/div/div[3]
events = driver.find_element_by_xpath('//*[@id="mainview"]//div[@class="row"]//div[@class="list-v2-content"]//div[3]/events-content//div[@class="list-events"]')
rows = events.find_elements_by_xpath("//div[@class='event-row-container']")
eInfo = []
event_desc = rows[0].find_element_by_xpath("//div[@class='event-row']//div[1]//div[@class='event-description']")
event_info = event_desc.find_element_by_xpath('//div[@class="event-info event-column"]')
event_id = event_info.find_element_by_xpath('//div[@class="event-text ng-binding"]').get_attribute("innerHTML")
event_time = event_info.find_element_by_xpath('//div[@class="event-text"][1]//time-component//span').get_attribute("innerHTML")
event_date = event_info.find_element_by_xpath('//div[@class="event-text"][2]//time-component//span').get_attribute("innerHTML")
event_names = event_desc.find_element_by_xpath('//div[@class="event-names event-column"]')
event_teams = event_names.find_elements_by_xpath('//div[@class="event-text ng-binding"]')
event_team1 = event_teams[2].get_attribute("title")
event_team2 = event_teams[3].get_attribute("title")
event_title = event_team1 + " vs " + event_team2

# event_odds = rows[0].find_element_by_xpath("//div[@class='event-row']//div[1]//div[@class='event-bets']")
# team1_name = event_odds.find_element_by_xpath("//div[@class='event-selections']//div[@class='event-text ng-scope'][1]").get_attribute("innerHTML")
# team1_odds = event_odds.find_element_by_xpath("//div[@class='event-selections']//div[@class='ng-binding'][1]").get_attribute("innerHTML")
# print(team1_name + ": " + team1_odds)
# team2_name = event_odds.find_element_by_xpath("//div[@class='event-selections']//div[@class='event-text ng-scope'][2]").get_attribute("innerHTML")
# team2_odds = event_odds.find_element_by_xpath("//div[@class='event-selections']//div[@class='ng-binding'][2]").get_attribute("innerHTML")
# print(team2_name + ": " + team2_odds)

event_odds = rows[0].find_element_by_xpath("//div[@class='event-row']//div[1]//div[@class='event-bets']//div[@class='event-selections']")
print(event_odds.get_attribute("innerHTML"))


eInfo.append([event_id, event_time, event_date, event_title])
print(eInfo)
sleep(2)
driver.close()
driver.quit()
