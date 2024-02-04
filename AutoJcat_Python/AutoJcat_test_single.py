import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# create a new Chrome session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

# navigate to the application home page
driver.get("https://jcat.de/Start.jsp")

# find the textarea and input text
textarea = driver.find_element(By.TAG_NAME, "textarea")
textarea.send_keys("ATGAAACGCATTAGCACCACCATTACCACCACCATCACCATTACCACAGGTAACGGTGCGGGCTGA")

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

    cai_gc_line = text_data.split('CAI-Value of the improved sequence: GC-Content of the improved sequence:')[1].split('\n')[1]
    cai_value, gc_content = cai_gc_line.split()

    print('Improved DNA:', improved_dna)
    print('CAI-Value of the improved sequence:', cai_value)
    print('GC-Content of the improved sequence:', gc_content)

    # save the data in a .txt file
    with open('C:\\Users\\darkh\\Downloads\\Jcat\\output.txt', 'w') as f:
        f.write(f'Improved DNA: {improved_dna}\n')
        f.write(f'CAI-Value of the improved sequence: {cai_value}\n')
        f.write(f'GC-Content of the improved sequence: {gc_content}\n')
else:
    print(f"The current URL is {current_url}, not https://jcat.de/Result.jsp")
