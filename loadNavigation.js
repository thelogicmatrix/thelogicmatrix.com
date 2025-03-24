// Load the navigation dynamically
fetch('nav.html')
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.text();
    })
    .then(data => {
        document.getElementById('navigation-placeholder').innerHTML = data;
    })
    .catch(error => {
        console.error('Error loading navigation:', error);
    });