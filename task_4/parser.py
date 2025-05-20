from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def init_driver():
    driver = webdriver.Firefox()
    return(driver)

def prelaunch(driver):
    driver.find_element(By.CSS_SELECTOR, 'a.red-btn').click()
    driver.find_element(By.CSS_SELECTOR, 'button.hide-cookie-policy').click()
    
def next_page(driver):
    next_button = driver.find_element(By.CSS_SELECTOR, 'a.next')
    driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
    next_button.click()

def parser_func(driver):
    wait = WebDriverWait(driver, 5)
    data = []
    catalog_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[itemtype="http://schema.org/Product"]')))
    for item in catalog_items:
        try:
            item_code_element = item.find_element(By.CSS_SELECTOR, 'p.catalog-item__code')
            item_code = item_code_element.text if item_code_element else "Code_not_found"
        except: 
            item_code = "Code.Error"
        try:
            item_name_element = item.find_element(By.CSS_SELECTOR, 'span.catalog-item__name')
            item_name = item_name_element.text if item_name_element else "Name_not_found"
        except: 
            item_name = "Name.Error"
        try:
            old_price_element = item.find_element(By.CSS_SELECTOR, 'p.catalog-item__oldprice')
            old_price = old_price_element.text if old_price_element.text else "Old_price_not_found"
        except: 
            old_price = "Old_price.Error"
        try:
            new_price_element = item.find_element(By.CSS_SELECTOR, 'p.catalog-item__price.with-sale')
            new_price = new_price_element.text if new_price_element else "New_price_not_found"
        except: 
            new_price = "New_price.Error"
        data.append([item_code, item_name, old_price, new_price])
    return(data)
