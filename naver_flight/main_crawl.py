from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://flight.naver.com/"
browser.get(url)
'''
// 전체 문서
@ 클래스
'''
departure_point = browser.find_element(By.XPATH, '//button[@class="tabContent_route__1GI8F select_City__2NOOZ start"]')
departure_point.click()

browser.implicitly_wait(1)

departure_point2 = browser.find_element(By.XPATH, '//button[text()="국내"]')
departure_point2.click()

departure_point3 = browser.find_element(By.XPATH, '//i[text()="서울"]')
departure_point3.click()



arrival_point = browser.find_element(By.XPATH, '//button[@class="tabContent_route__1GI8F select_City__2NOOZ end"]')
arrival_point.click()

browser.implicitly_wait(1)

arrival_point2 = browser.find_element(By.XPATH, '//button[@class="autocomplete_Collapse__tP3pM" and text()="일본"]')
arrival_point2.click


arrival_point3 = browser.find_element(By.XPATH, '//i[@class="autocomplete_location__TDL6g" and text()="오사카, 일본"]')
arrival_point3.click

input()
browser.quit()
