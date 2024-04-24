console.log("creating new session...")

// to speak a para 
function readParagraph(text) {
    const ut = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(ut);
}



// Function to setup speech recognition

function takeSpeechInput() {
    const recognition = new webkitSpeechRecognition() || new SpeechRecognition();    // Create an instance of SpeechRecognition
    // Start listening
    recognition.start();

    // Event fired when speech recognition starts
    recognition.onstart = function () {
        console.log('Listening...');
    };

    // Event fired when speech recognition ends
    recognition.onend = function () {
        console.log('Speech recognition ended.');
    };

    // Event fired when speech is recognized
    recognition.onresult = function (event) {
        const transcript = event.results[0][0].transcript;
        console.log('You said: ', transcript);

        if (transcript.toLowerCase().includes('yes')) {
            var text = "okay lets start the interview.";
            console.log(text);
            readParagraph(text);
            // Redirect to the interview page
            var domainForm = document.getElementById('domain-form');
            domainForm.submit();
        }
        else if (transcript.toLowerCase().includes('no')) {

            var text = "okay, let me know when you are ready.";
            console.log(text);
            readParagraph(text)

        }
        else {
            var text = "I am sorry, I did not understand that. Please say 'yes, I am ready' or 'no, I am not ready'"
            console.log(text);
            readParagraph(text)
            setTimeout(takeSpeechInput,2000)
        }
    };

    // Event fired when there's an error
    recognition.onerror = function (event) {
        console.error('Speech recognition error:', event.error);
    };
}

// function which takes input 
function askToStart() {

    var text = "Would you like to start the interview? say 'yes, I am ready' to start or  'no, I am not ready'  to cancel the interview";
    console.log(text);
    readParagraph(text);
    // run this function with 6.5 second delay 
    setTimeout(takeSpeechInput, 8000);
}


// Call the askToStart function when form submit
var domainForm = document.getElementById('domain-form');

domainForm.addEventListener('submit', function (event) {

    event.preventDefault();

    askToStart();

});
