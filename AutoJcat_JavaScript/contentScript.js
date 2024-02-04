// Listen for a message from the background script
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.message === 'start') {
        var id = request.data.id;
        var sequence = request.data.sequence;

        // Store the ID in localStorage before navigating to the new page
        localStorage.setItem('currentId', id);

        // Set the textarea value
        var textarea = document.querySelector('textarea');
        textarea.value = sequence;

        // Select the dropdown element
        var dropdown = document.querySelector('select');

        // Loop through each option in the dropdown
        for (var i = 0; i < dropdown.options.length; i++) {
            var option = dropdown.options[i];

            // Check if the option's text or value matches what you want
            if (option.text === 'Escherichia coli (strain K12)' || option.value === '42 Escherichia coli (strain K12)') {
                // If it does, select this option and break out of the loop
                dropdown.selectedIndex = i;
                break;
            }
        }

        // The names of the checkboxes you want to check
        var names = ['hairpin', 'rbs', 'restriction'];

        // Loop through each name
        for (var i = 0; i < names.length; i++) {
            // Select the checkbox with the current name
            var checkbox = document.querySelector('input[name="' + names[i] + '"]');

            // Check the checkbox
            checkbox.checked = true;
        }

        // Select the button element
        var button = document.querySelector('button');

        // Click the button
        button.click();

        // Wait for 5 seconds before running the rest of the code
        setTimeout(function() {
            // The webpage has finished loading, now you can run the rest of your code

            // After the page has navigated, retrieve the ID from localStorage
            id = localStorage.getItem('currentId');

            // After website navigated
            let text = document.body.innerText;

            // Remove line numbers
            text = text.replace(/\d+\n/g, '\n');

            // Extract the Improved DNA sequence
            let improvedDNA = text.match(/Improved DNA:\n([A-Z\s\d]+)(?=\n\n\nCAI)/);
            console.log('improvedDNA:', improvedDNA);
            improvedDNA = improvedDNA ? improvedDNA[1].trim() : 'Not found';    

            // Extract the CAI-Value of the improved sequence
            let caiValueIndex = text.indexOf('CAI-Value of the improved sequence:');
            let caiValue = text.slice(caiValueIndex).split('\n')[1].split('\t')[0];
            console.log('caiValue:', caiValue);
            caiValue = caiValue.trim();

            // Extract the GC-Content of the improved sequence
            let gcContentIndex = text.indexOf('GC-Content of the improved sequence:');
            let gcContent = text.slice(gcContentIndex).split('\n')[1].split('\t')[1];
            console.log('gcContent:', gcContent);
            gcContent = gcContent.trim();

            console.log('Improved DNA:', improvedDNA);
            console.log('CAI-Value of the improved sequence:', caiValue);
            console.log('GC-Content of the improved sequence:', gcContent);

            // Create a string with the values
            var resultString = 'Improved DNA: ' + improvedDNA + '\n' +
                               'CAI-Value of the improved sequence: ' + caiValue + '\n' +
                               'GC-Content of the improved sequence: ' + gcContent;

            // Get the existing results from localStorage
            var results = JSON.parse(localStorage.getItem('results')) || [];

            // Add the new result to the beginning of the results array
            results.unshift({id: id, resultString: resultString});

            // If there are more than 10 results, remove the oldest one
            if (results.length > 10) {
                results.pop();
            }

            // Store the results back in localStorage
            localStorage.setItem('results', JSON.stringify(results));

            // Send a message to the background script to indicate that processing is done
            chrome.runtime.sendMessage({message: 'done', index: request.index});
        }, 5000);  // 5000 milliseconds = 5 seconds
    }
});
