from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

# Start a new Chrome WebDriver session
driver = webdriver.Chrome()
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

# Open the CSV file
with open('C:/Users/darkh/Downloads/JCat_test.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

    # Define the output CSV file path
    output_csv_path = 'C:/Users/darkh/Downloads/JCat_test_result.csv'

    # Open the output CSV file
    with open(output_csv_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)

        # Write the header row
        writer.writerow(['Locus_tag', 'Length', 'gc_value', 'cai_value', 'Optimized_Sequence', 'Name of restricted enzyme'])

        # For each DNA sequence in the CSV file
        for row in reader:
            locus_tag = row[2]  # The locus tag is in the third column
            dna_sequence = row[5]  # The DNA sequence is in the sixth column

            # Navigate to the VectorBuilder website
            driver.get('https://en.vectorbuilder.com/tool/codon-optimization.html')

            # Wait until the div with the class 'seq-editor' is present on the page
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.seq-editor')))

            # Find the CodeMirror div
            code_mirror = driver.find_element(By.CSS_SELECTOR, '.CodeMirror')

            # Use JavaScript to input text into the CodeMirror editor
            driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);", code_mirror, dna_sequence)

            # Use JavaScript to select the 'Protein sequence' radio button
            driver.execute_script("document.getElementById('radio1').checked = true;")

            # Get all option elements within the select element
            options = driver.find_elements(By.TAG_NAME, 'option')

            # Loop through all options
            for option in options:
                # If the option's text content is 'Escherichia coli str. K-12 substr. MG1655'
                if option.text.strip() == 'Escherichia coli str. K-12 substr. MG1655':
                    # Select this option
                    option.click()
                    break

            # Define the list of enzymes to select
            enzymes_to_select = ['BamHI', 'EcoRI', 'HindIII', 'NdeI', 'NotI', 'PstI', 'XhoI']

            # Find all checkboxes within elements with the class ‘checkbox long-list’
            checkboxes = driver.find_elements(By.CSS_SELECTOR, '.checkbox.long-list input[type=checkbox]')

            # Loop through all checkboxes
            for checkbox in checkboxes:
                # Get the parent label element
                label = checkbox.find_element(By.XPATH, '..')

                # Get the text content of the label
                enzyme_name = label.text.strip()

                # If the enzyme name is in the list of enzymes to select
                if enzyme_name in enzymes_to_select:
                    # Scroll the checkbox into view
                    driver.execute_script("arguments[0].scrollIntoView();", checkbox)

                    # Use JavaScript to click the checkbox
                    driver.execute_script("arguments[0].click();", checkbox)

            # Find the 'Submit' button using XPath and click it
            driver.execute_script('document.querySelector(\'button[ng-click="submit()"]\').click();')

            time.sleep(10)
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.ng-scope')))
            improved_dna_label = driver.find_element(By.CSS_SELECTOR, '.ng-scope label.ng-binding').text
            improved_dna_sequence = driver.find_element(By.CSS_SELECTOR, '.ng-scope pre.ng-binding').text

            # Parse the GC value and CAI value from the label text
            gc_value = improved_dna_label.split('GC=')[1].split('%')[0]
            cai_value = improved_dna_label.split('CAI=')[1]

            # Write the data row
            writer.writerow([locus_tag, len(improved_dna_sequence), gc_value, cai_value, improved_dna_sequence, 'BamHI, EcoRI, HindIII, NdeI, NotI, PstI, XhoI'])

driver.quit()
