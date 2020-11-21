from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')

searchbox = driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('hello world')

button = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
button.click()


button = driver.find_element_by_class_name("infoDismiss")

driver.implicitly_wait(10)
ActionChains(driver).move_to_element(button).click(button).perform()
