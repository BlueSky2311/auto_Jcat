from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

# Start a new Chrome WebDriver session
driver = webdriver.Chrome()

# Open the CSV file
with open('C:/Users/darkh/Downloads/JCat_test.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # For each DNA sequence in the CSV file
    for row in reader:
        gene_name = row[1]  # The gene name is in the second column
        dna_sequence = row[5]  # The DNA sequence is in the sixth column

        # Navigate to the VectorBuilder website
        driver.get('https://en.vectorbuilder.com/tool/codon-optimization.html')

        # Wait until the div with the class 'seq-editor' is present on the page
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.seq-editor')))

        # Find the CodeMirror div
        code_mirror = driver.find_element(By.CSS_SELECTOR, '.CodeMirror')

        # Use JavaScript to input text into the CodeMirror editor
        driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);", code_mirror, dna_sequence)

        # Get all option elements within the select element
        options = driver.find_elements(By.TAG_NAME, 'option')

        # Loop through all options
        for option in options:
            # If the option's text content is 'Escherichia coli str. K-12 substr. MG1655'
            if option.text.strip() == 'Escherichia coli str. K-12 substr. MG1655':
                # Select this option
                option.click()
                break

        # Find all checkboxes within elements with the class ‘checkbox long-list’ and check each one
        checkboxes = driver.find_elements(By.CSS_SELECTOR, '.checkbox.long-list input[type=checkbox]')
        for checkbox in checkboxes:
            # Scroll the checkbox into view
            driver.execute_script("arguments[0].scrollIntoView();", checkbox)

            # Use JavaScript to click the checkbox
            driver.execute_script("arguments[0].click();", checkbox)

# Close the WebDriver session
#driver.quit()
