from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# open the url
driver.get('https://www.amazon.com/')

driver.find_element(By.XPATH, "//li[@class='nav_last']/a[text()='Help']").click()
sleep(2)

search = driver.find_element(By.XPATH, "//input[@id='helpsearch']")
search.clear()
search.send_keys('Cancel order')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.XPATH, "//input[@class='a-button-input']").click()

# verify
assert 'Cancel Items or Orders' in driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text

driver.quit()