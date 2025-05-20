import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()
driver.get('https://www.bestwatch.ru/watch/filter/pol:unisex/')
driver.find_element(By.CSS_SELECTOR, 'a.red-btn').click()
driver.find_element(By.CSS_SELECTOR, 'button.hide-cookie-policy').click()
FILENAME = "data.csv"
with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    while True:
        wait = WebDriverWait(driver, 5)
        catalog_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[itemtype="http://schema.org/Product"]')))
        for item in catalog_items:
            try:
                item_code_element = item.find_element(By.CSS_SELECTOR, 'p.catalog-item__code')
                item_code = item_code_element.text if item_code_element else "Code not found"
            except:
                item_code = "Code. Error"
            try:
                item_name_element = item.find_element(By.CSS_SELECTOR, 'span.catalog-item__name')
                item_name = item_name_element.text if item_name_element else "Name not found"
            except:
                item_name = "Name. Error"
            try:
                old_price_element = item.find_element(By.CSS_SELECTOR, 'p.catalog-item__oldprice')
                old_price = old_price_element.text if old_price_element.text else "Old price not found"
            except:
                old_price = "Old price. Error"
            try:
                new_price_element = item.find_element(By.CSS_SELECTOR, 'p.catalog-item__price.with-sale')
                new_price = new_price_element.text if new_price_element else "New price not found"
            except:
                new_price = "New price. Error"
            data = [item_code, item_name, old_price, new_price]
            writer.writerow(data)
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'a.next')
            driver.execute_script("arguments[0].scrollIntoView(true);", next_button)
            next_button.click()
        except Exception as e:
            print(f"Достигнут конец страниц")
            break
driver.quit()
