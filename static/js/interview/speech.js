console.log("speech.js")

// Function to read a paragraph aloud
function readParagraph(text) {
    const ut = new SpeechSynthesisUtterance(text);
    speechSynthesis.speak(ut);
}





