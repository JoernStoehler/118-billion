document.addEventListener('DOMContentLoaded', function() {
    let ids = [];
    const container = document.querySelector('.container');
    const contentImage = document.getElementById('contentImage');
    const textContent = document.getElementById('textContent');
    const loadButton = document.getElementById('loadButton');

    // Initially make the container visible
    container.style.opacity = '1';

    // Load CSV data
    fetch('data.csv')
    .then(response => response.text())
    .then(data => {
        ids = data.split("\n").filter(id => id.trim() !== '');
    })
    .catch(error => {
        console.error('Error fetching CSV:', error);
    });

    loadButton.addEventListener('click', function() {
        // Fade out the container
        container.style.opacity = '0';

        // Delay content update to after the fade-out completes
        setTimeout(() => {
            // Choose a random id
            const randomId = ids[Math.floor(Math.random() * ids.length)];

            // Load image and text associated with the chosen id
            fetchImage(randomId);
            fetchText(randomId);
            
            // After updating content, fade in the container
            container.style.opacity = '1';
        }, 500);  // Matching the CSS transition time
    });

    function fetchImage(id) {
        const newImage = new Image();
        newImage.src = `data/${id}.png`;

        newImage.onload = function() {
            contentImage.src = newImage.src;
        };
    }

    function fetchText(id) {
        fetch(`data/${id}.html`)
        .then(response => response.text())
        .then(data => {
            textContent.innerHTML = data;
        })
        .catch(error => {
            console.error('Error fetching text:', error);
        });
    }

    // Load initial content
    loadButton.click();
});
