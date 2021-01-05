from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.binary_location = '/usr/bin/brave-browser'
driver_path = '/opt/WebDriver/bin/chromedriver'
drvr = webdriver.Chrome(options = options, executable_path = driver_path)
drvr.get('https://stackoverflow.com')