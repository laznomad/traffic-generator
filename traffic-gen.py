import selenium as se
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import random
import csv

url = input("Enter destination URL: ")
visits = int(input("Enter number of visits: "))

options = Options()
ua = UserAgent()
chrome_path = './chromedriver'
for i in range(visits):
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')
    driver = webdriver.Chrome(chrome_options=options, executable_path=chrome_path)
    driver.get(url)
    driver.set_window_size(1120, 550)
    time.sleep(random.randint(2,10)) 
    print(driver.current_url)
    print(i)
    with open('traffic3.log', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(["User Agent"])
        writer.writerow(userAgent)
        #writer.writerows(int(time.time()))
        #writer.writerow(int(i))
driver.quit()
