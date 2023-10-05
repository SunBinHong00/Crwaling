from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

browser = webdriver.Chrome()
word = '명언'
url = f"https://en.dict.naver.com/#/search?range=example&shouldSearchVlive=false&query={word}&autoConvert="
browser.get(url)

browser.implicitly_wait(2)
#expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="searchPage_example"]/div[2]'))	
data = browser.find_element(By.XPATH, '//*[@id="searchPage_example"]/div[2]')

print(data)

input()
browser.quit()