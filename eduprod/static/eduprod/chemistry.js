document.addEventListener('DOMContentLoaded', function() {
    // Function to reveal the answer
    function revealAnswer(button) {
        button.nextElementSibling.style.display = 'block';
        button.style.display = 'none';
    }

    // Event listener for the "Reveal Answer" buttons
    document.querySelectorAll('.reveal-answer').forEach(button => {
        button.addEventListener('click', function() {
            revealAnswer(button);
        });
    });

    // Event listener for the "Next Sentence" button
    document.getElementById('next-sentence').addEventListener('click', function(event) {
        event.preventDefault();
        const sentences = document.querySelectorAll('.sentence');
        const lastIndex = sentences.length - 1;
        const lastSentence = sentences[lastIndex];
        const answerButton = lastSentence.querySelector('.reveal-answer');
        if (answerButton) {
            revealAnswer(answerButton);
        } else {
            console.log('No more sentences available.');
        }
    });
});
