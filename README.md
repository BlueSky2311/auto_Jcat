# Overview
The script uses Selenium WebDriver to interact with the JCat web tool, which is used for optimizing DNA sequences. It inputs a DNA sequence, selects an organism, checks certain options, and submits the form. It then waits for the results page to load, retrieves the text data from the webpage, and processes the text data to extract the improved DNA sequence, the Codon Adaptation Index (CAI) value, and the GC content of the improved sequence.

The DNA sequences are read from a CSV file, and the results are saved in a text file named after the gene in the CSV file. After all the text files have been created, the script combines all the text files into a new CSV file.

# Usage

1. **Setup**: Start a new Chrome browser session, maximize the window, and navigate to the JCat home page.
2. **Input DNA sequence**: Find a textarea element on the page and input a specific DNA sequence.
3. **Select organism**: Find a dropdown menu and select 'Escherichia coli (strain K12)' as the organism.
4. **Check options**: Check certain options ('hairpin', 'rbs', 'restriction') on the page.
5. **Submit**: Find a button on the page and click it to submit the form.
6. **Check results**: Wait for the results page to load, check the current URL to confirm it's on the correct page, and then retrieve all the text data from the webpage.
7. **Process results**: Process the text data to remove line numbers and extract the improved DNA sequence, the Codon Adaptation Index (CAI) value, and the GC content of the improved sequence.
8. **Save results**: Save these results into a text file named after the gene in the CSV file.
9. **Combine results**: After all the text files have been created, combine all the text files into a new CSV file named 'Results.csv'.
    
## Note
This Python script is designed to automate the process of comparing DNA optimization results between JCat and ours own results. It's intended for academic research purposes only. 
Please note that web scraping should be done responsibly, respecting the website's terms of service and not causing undue load on the server. 
Always ensure that your activities are in compliance with the law and any applicable terms of service. Use this script responsibly and ethically.

