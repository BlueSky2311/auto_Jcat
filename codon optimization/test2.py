from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as uc

driver = webdriver.Chrome()
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

with open('C:/Users/darkh/Downloads/JCat_test.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    row = next(reader)
    gene_name = row[1]  # The gene name is in the second column
    dna_sequence = row[5]  # The DNA sequence is in the sixth column

    driver.get('https://en.vectorbuilder.com/tool/codon-optimization.html')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.seq-editor')))

    code_mirror = driver.find_element(By.CSS_SELECTOR, '.CodeMirror')

    driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);", code_mirror, dna_sequence)

    time.sleep(2)  # Wait for 2 seconds

    driver.execute_script("document.getElementById('radio2').checked = true;")

    time.sleep(2)  # Wait for 2 seconds

    options = driver.find_elements(By.TAG_NAME, 'option')

    for option in options:
        if option.text.strip() == 'Escherichia coli str. K-12 substr. MG1655':
            option.click()
            break

    time.sleep(2)  # Wait for 2 seconds

    checkboxes = driver.find_elements(By.CSS_SELECTOR, '.checkbox.long-list input[type=checkbox]')
    for checkbox in checkboxes:
        # Scroll the checkbox into view
        driver.execute_script("arguments[0].scrollIntoView();", checkbox)

        # Use JavaScript to click the checkbox
        driver.execute_script("arguments[0].click();", checkbox)

    time.sleep(10)  # Wait for 2 seconds

    submit_button = driver.find_element(By.CSS_SELECTOR, 'button[ng-click="submit()"]')
    submit_button.click()  # Use Selenium's click method