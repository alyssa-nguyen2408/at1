document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 1; // Start index for loading sentences

    // Function to reveal the answer
    function revealAnswer(button) {
        button.nextElementSibling.style.display = 'block';
        button.style.display = 'none';
    }

    // Function to load the next sentence
    function loadNextSentence() {
        const container = document.getElementById('sentences-container');
        const nextSentence = document.querySelector(`[data-index="${currentIndex}"]`);
        
        if (nextSentence) {
            container.appendChild(nextSentence.cloneNode(true));
            currentIndex++;
        } else {
            container.innerHTML += '<p>Finished</p>';
            document.getElementById('next-sentence').style.display = 'none'; // Hide the next question button
        }
    }

    // Event listener for the "Reveal Answer" buttons
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('reveal-answer')) {
            revealAnswer(event.target);
        }
    });

    // Event listener for the "Next Sentence" button
    document.getElementById('next-sentence').addEventListener('click', function(event) {
        event.preventDefault();
        loadNextSentence();
    });

    // Load the first sentence initially
    loadNextSentence();
});

