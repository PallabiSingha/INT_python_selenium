import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(2)

# 1️⃣ Opens https://rahulshettyacademy.com in Chrome browser.
driver.get("https://rahulshettyacademy.com")

# 2️⃣ Prints the title of the page in the console.
print(driver.title)

# 3️⃣ Navigates to https://www.wikipedia.org after 2 seconds.
driver.get("https://www.wikipedia.org")

# 4️⃣ Maximizes the browser window.
driver.maximize_window()

# 5️⃣ Prints the current URL of the page.
print(driver.current_url)

# 6️⃣ Goes back to https://rahulshettyacademy.com using browser navigation.
driver.back()

# 7️⃣ Takes a screenshot of loaded page and save it as rahul_homepage.png.
time.sleep(2)
driver.save_screenshot('D:\\Python_Exercism\\rahul_homepage.png')

# 8️⃣ Closes the browser at the end of the script.
driver.close()