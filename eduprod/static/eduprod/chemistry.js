document.addEventListener('DOMContentLoaded', function() {
    let currentIndex = 0; // Start index for loading sentences
    const sentences = document.querySelectorAll('.sentence');

    // Function to reveal the answer
    function revealAnswer(button) {
        button.nextElementSibling.style.display = 'block';
        button.style.display = 'none';
    }

    // Function to load the next batch of sentences
    function loadNextSentences() {
        for (let i = currentIndex; i < currentIndex + 1; i++) {
            if (i < sentences.length) {
                sentences[i].style.display = 'block';
            } else {
                // If all sentences are displayed, show "Finished" message
                document.getElementById('finished').style.display = 'block';
                return; // Exit the function
            }
        }
        currentIndex += 1;
        setTimeout(loadNextSentences, 2000); // Load next batch after 2 seconds
    }

    // Event listener for the "Reveal Answer" buttons
    document.addEventListener('click', function(event) {
        if (event.target.classList.contains('reveal-answer')) {
            revealAnswer(event.target);
        }
    });

    // Load the first batch of sentences initially
    loadNextSentences();
});



