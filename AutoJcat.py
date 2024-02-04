import csv
import re
import glob
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# read the CSV file
with open('C:/Users/darkh/Downloads/JCat_test.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # create a new Chrome session
        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        driver.maximize_window()

        # navigate to the application home page
        driver.get("https://jcat.de/Start.jsp")

        # find the textarea and input the DNA sequence from the CSV file
        textarea = driver.find_element(By.TAG_NAME, "textarea")
        textarea.send_keys(row['Sequence'])

        # find the dropdown and select an option
        dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
        dropdown.select_by_visible_text('Escherichia coli (strain K12)')

        # the names of the checkboxes you want to check
        names = ['hairpin', 'rbs', 'restriction']

        # loop through each name
        for name in names:
            # find the checkbox with the current name and check it
            checkbox = driver.find_element(By.NAME, name)
            checkbox.click()

        # find the button and click it
        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        # wait for the page to load and check the current URL
        current_url = driver.current_url
        if current_url == "https://jcat.de/Result.jsp":
            print("The current URL is https://jcat.de/Result.jsp")
            # get all the text data from the webpage
            text_data = driver.find_element(By.TAG_NAME, "body").text

            # remove line numbers
            text_data = re.sub(r'\d+\n', '\n', text_data)

            # extract the Improved DNA sequence
            improved_dna_match = re.search(r'Improved DNA:\n([A-Z\s]+)', text_data)
            improved_dna = improved_dna_match.group(1).strip() if improved_dna_match else 'Not found'

            # find the line with the CAI-Value and GC-Content of the improved sequence
            cai_gc_line = text_data.split('CAI-Value of the improved sequence: GC-Content of the improved sequence:')[1].split('\n')[1]

            # split the line into CAI-Value and GC-Content
            cai_value, gc_content = cai_gc_line.split()

            #print('Improved DNA:', improved_dna)
            #print('CAI-Value of the improved sequence:', cai_value)
            #print('GC-Content of the improved sequence:', gc_content)

            # remove all blank spaces, the word "CAI", and line breaks from the improved DNA sequence
            improved_dna = improved_dna.replace(" ", "").replace("CAI", "").replace("\n", "")

            # save the data in a .txt file named after the Gene in the CSV file
            with open(f'C:\\Users\\darkh\\Downloads\\Jcat\\{row["Gene"]}.txt', 'w') as f:
                f.write(f'Improved DNA: {improved_dna}\n')
                f.write(f'CAI-Value of the improved sequence: {cai_value}\n')
                f.write(f'GC-Content of the improved sequence: {gc_content}\n')
        else:
            print(f"The current URL is {current_url}, not https://jcat.de/Result.jsp")

        # close the browser session
        driver.quit()

# get a list of all .txt files in the directory
txt_files = glob.glob('C:\\Users\\darkh\\Downloads\\Jcat\\*.txt')

# create a new CSV file
with open('C:\\Users\\darkh\\Downloads\\Jcat\\Results.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Gene', 'Improved DNA', 'CAI-Value of the improved sequence', 'GC-Content of the improved sequence'])  # write the header

    # for each .txt file...
    for txt_file in txt_files:
        with open(txt_file, 'r') as f:
            lines = f.readlines()
            gene = os.path.basename(txt_file).split('.')[0]  # get the Gene from the filename
            improved_dna = lines[0].split(': ')[1].strip()
            cai_value = lines[1].split(': ')[1].strip()
            gc_content = lines[2].split(': ')[1].strip()
            writer.writerow([gene, improved_dna, cai_value, gc_content])  # write the data to the CSV file