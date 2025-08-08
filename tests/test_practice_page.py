import time
import pytest
from selenium.webdriver.common.by import By

URL = "https://www.letskodeit.com/practice"

@pytest.fixture(autouse=True)
def open_practice_page(driver):
    driver.get(URL)
    yield

# Open and verify Practice Page title
def test_title(driver):
    print('Page Title: ', driver.title)
    assert "Practice" in driver.title
    
    

#Radio Button selection 
def test_rediobutton_selecction(driver):
    Benz_radio = driver.find_element(By.ID, "benzradio")
    Benz_radio.click()
    assert Benz_radio.is_selected()
    #time.sleep(4)



#Checkbox selection
def test_checkbox_selecction(driver):
    #checkboxes = driver.find_elements(By.XPATH,"//input[contains(@type,'checkbox')] | //input[contains(@name,'cars')]")
    
    checkboxes = driver.find_elements(By.XPATH,"//input[contains(@type,'checkbox')] | input[contains(@id,'benzcheck')]")
    #bmw_check.click()
    #assert bmw_check.is_selected()
    for check_theBox in checkboxes:
        if not check_theBox.is_selected():
            check_theBox.click()
    #time.sleep(4)
