document.getElementById('startButton').addEventListener('click', function() {
  chrome.runtime.sendMessage({message: 'start'});
});
