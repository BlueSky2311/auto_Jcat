# Overview
These script uses Selenium, AutoIT, Jave Script, etc. to interact with the some web codon optimization tools, which is used for optimizing DNA sequences. It inputs a DNA sequence, selects an organism, checks certain options, and submits the form. It then waits for the results page to load, retrieves the text data from the webpage, and processes the text data to extract the improved DNA sequence, the Codon Adaptation Index (CAI) value, and the GC content of the improved sequence.

The DNA sequences are read from a CSV file, and the results are saved in a text file named after the gene in the CSV file. After all the text files have been created, the script combines all the text files into a new CSV file.
    
## Note
This Python script is designed to automate the process of comparing DNA optimization results between other codon optimaze tools and results in ours tool. It's intended for academic research purposes only. 
Please note that web scraping should be done responsibly, respecting the website's terms of service and not causing undue load on the server. 
Always ensure that your activities are in compliance with the law and any applicable terms of service. Use this script responsibly and ethically.

