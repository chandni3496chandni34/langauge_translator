// Parallax scrolling effect
window.addEventListener('scroll', function() {
    const parallax = document.querySelector('.background');
    let scrollPosition = window.pageXOffset;
    parallax.style.backgroundPositionY = scrollPosition * 0.7 + 'px'; // Adjust the parallax effect speed here
  });
// script.js

// Function to repeat the translated text
function repeatTranslation() {
  var translatedText = "{{ translated_text }}"; // Fetch translated text from server-side template
  var languageChoice = document.getElementById("language_choice").value; // Get selected language
  var xhttp = new XMLHttpRequest(); // Create new XMLHttpRequest object
  xhttp.onreadystatechange = function() { // Define callback function
      if (this.readyState == 4 && this.status == 200) { // Check if request is complete and successful
          var response = this.responseText; // Get response text
          var parser = new DOMParser(); // Create new DOMParser object
          var doc = parser.parseFromString(response, "text/html"); // Parse response text as HTML
          var repeatedText = doc.querySelector('#translatedText').innerText; // Get repeated text from response
          var audio = new Audio('translated_voice.mp3'); // Create new Audio object with translated voice
          audio.play(); // Play audio
      }
  };
  // Prepare and send AJAX request
  xhttp.open("POST", "/", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("input_text=" + translatedText + "&language_choice=" + languageChoice);
}
