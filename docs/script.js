document.addEventListener('DOMContentLoaded', () => {
    let currentIndex = 0;
    const button = document.getElementById('next');
    const contentDiv = document.getElementById('content');
    let ids = [];

    // fetch ids
    fetch('data.csv')
        .then(response => response.text())
        .then(data => {
            ids = data.trim().split('\n');
            // shuffle
            //ids.sort(() => Math.random() - 0.5);
            currentIndex = 0;

            fetchAndSet(ids[currentIndex]);
            prefetch(ids[(currentIndex + 1) % ids.length]);
        });

    function fetchAndSet(id) {
        fetch(`data/${id}.json`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('bio-image').src = data.files.image.substring("docs/".length);
                document.getElementById('bio-image').alt = data.vars_html["Image Prompt"];
                document.getElementById('name').textContent = data.vars_html["Title Data"]["name"];
                document.getElementById('date-range').textContent = `${data.vars_html["Title Data"]["exact birth date"]} - ${data.vars_html["Title Data"]["exact death date"]}`;
                document.getElementById('home-area').textContent = data.vars_html["Title Data"]["home area"];
                document.getElementById('bio-text').textContent = data.vars_html["Biography"];
            })
            .catch(error => {
                console.error("Error fetching data: ", error);
            });
    }

    function prefetch(id) {
        fetch(`data/${id}.json`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('bio-image-2').src = data.files.image.substring("docs/".length);
                document.getElementById('bio-text-2').textContent = data.vars_html["Biography"];
            })
            .catch(error => {
                console.error("Error fetching data: ", error);
            });
    }

    button.addEventListener('click', () => {
        // fade out current content
        const fadeOutTime = 500;
        const fadeBufferTime = 500;

        // wait for fade out to complete
        // then switch content
        // wait for buffer time
        // then fade in new content

        contentDiv.classList.toggle('fade');
        setTimeout(() => {
            currentIndex = (currentIndex + 1) % ids.length;
            fetchAndSet(ids[currentIndex]);
            prefetch(ids[(currentIndex + 1) % ids.length]);
            contentDiv.classList.toggle('fade');
        }, fadeOutTime);
    });
});
