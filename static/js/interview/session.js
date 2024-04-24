console.log('session running')

// croussel of questions to be asked to user

var slideshow = document.querySelectorAll('.question');


console.log(slideshow);

// function to move to the next question
function nextQuestion() {
    console.log('next question')
    for (var i = 0; i < slideshow.length; i++) {
        if (slideshow[i].classList.contains('active')) {
            slideshow[i].classList.remove('active');
            if (i === slideshow.length - 1) {
                var text = "That all for this session. You will get your feedback. Thank you ";
                readParagraph(text)
                
            } else {
                slideshow[i + 1].classList.add('active');
                console.log(i)
            }
            break;
        }
    }
}

// reading a queestion 
function readParagraph(text) {
    const ut = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(ut);
}


// create a function which speak the question when page loads 
function speakQuestion() {
    var question = document.querySelector('.question.active .question-text').value;
    console.log(question)
    var msg = new SpeechSynthesisUtterance(question);
    window.speechSynthesis.speak(msg);
}

// call the function when page loads
window.onload = speakQuestion;

// go to the next quesiton 
function nextQuestionSpeak() {
    nextQuestion();

    setTimeout(speakQuestion, 1000)

}


// start speech recognitation 
function listenAnswers() {
    takeSpeechInput();
}

// take a speech input function 
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
        answer = document.querySelector('.question.active .answer-input')
        const transcript = event.results[0][0].transcript;
        console.log('You said: ', transcript);
        answer.value += transcript + ' ';
    };

    // Event fired when there's an error
    recognition.onerror = function (event) {
        console.error('Speech recognition error:', event.error);
    };
}
