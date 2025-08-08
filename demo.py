import time
from selenium import webdriver


driver = webdriver.Chrome() 
driver.get('https://rahulshettyacademy.com')
time.sleep(6)
print('Page Title: ', driver.title)

time.sleep(2)
driver.get('https://www.wikipedia.org')
driver.maximize_window()
time.sleep(2)

print('Current URL: ', driver.current_url)
driver.back;
driver.save_screenshot("D:\\Python\\Python_selenium\screenshot\\rahul_homepage.png")
time.sleep(2)
driver.quit()