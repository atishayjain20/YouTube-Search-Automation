from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
path="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(path)
driver.get("https://youtube.com")
search=driver.find_element_by_id("search")
search.send_keys("test")
search.send_keys(Keys.RETURN)
# print(driver.page_source)
te=driver.find_element_by_id("filter-group-name")
print(te.text);
# //*[@id="filter-group-name"]/yt-formatted-string
time.sleep(10)
driver.close()