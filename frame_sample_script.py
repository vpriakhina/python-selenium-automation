from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)

driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe')

driver.switch_to.frame('iframeResult')

frame=driver.find_element(By.CSS_SELECTOR, "iframe[src='https://www.w3schools.com']")
driver.switch_to.frame(frame)

logo = driver.find_element(By.CSS_SELECTOR, 'a.w3schools-logo')

print(logo.get_attribute('href'))

driver.quit()