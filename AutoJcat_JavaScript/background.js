// The URL of the .csv file
var url = 'https://raw.githubusercontent.com/BlueSky2311/auto_Jcat/main/JCat_test.csv';

// Create an array to store the IDs and sequences
var data = [];

// Fetch the .csv file
fetch(url)
    .then(response => response.text())
    .then(text => {
        // Parse the .csv file
        var rows = text.split('\n');
        for (var i = 1; i < rows.length; i++) {
            var cells = rows[i].split(',');

            // Get the ID and sequence from the appropriate columns
            var id = cells[0];
            var sequence = cells[5];

            // Add the ID and sequence to the data array
            data.push({id: id, sequence: sequence});
        }

        // Start the process for the first row
        startProcess(0);
    })
    .catch(error => console.error('Error:', error));

function startProcess(index) {
    if (index >= data.length) {
        // All rows have been processed
        return;
    }

    // Get the ID and sequence for this row
    var id = data[index].id;
    var sequence = data[index].sequence;

    // Save the current index to localStorage
    localStorage.setItem('currentIndex', index);

    // Send a message to the content script to start the process
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
        chrome.tabs.sendMessage(tabs[0].id, {message: 'start', data: {id: id, sequence: sequence}});
    });
}

// Listen for a message from the content script
chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.message === 'done') {
        // The content script has finished processing the current row
        // Process the next row
        startProcess(request.index + 1);
    }
});

// Listen for when a webpage has completely finished loading
chrome.webNavigation.onCompleted.addListener(function(details) {
    // Check if the URL of the tab that has finished loading matches the URL you're interested in
    if (details.url === 'https://jcat.de/Result.jsp') {
        // The webpage has finished loading, now you can run your code
        // Send a message to the content script to continue the process
        chrome.tabs.sendMessage(details.tabId, {message: 'continue'});
    }
}, {url: [{urlMatches : 'https://jcat.de/Result.jsp'}]});
