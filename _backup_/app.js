document.addEventListener('DOMContentLoaded', (event) => {
  console.log("DOM fully loaded and parsed");
  let chatHistory = [];
  let chatDisplay = document.getElementById('chat-display');

  function updateChatDisplay() {
    chatDisplay.innerHTML = '';
    for (let message of chatHistory) {
        let messageElement = document.createElement('p');
        messageElement.textContent = message.name + ': ' + message.message;
        chatDisplay.appendChild(messageElement);
    }
  }

  document.querySelector("#sendButton").addEventListener("click", () => {
    const inputField = document.querySelector("#questionField");
    const userQuestion = inputField.value;
    inputField.value = "";
    chatHistory.push({ name: 'Kunde', message: userQuestion });
    updateChatDisplay();
    
    console.log("Button clicked, user question is: ", userQuestion);
    
    askQuestion(userQuestion);
  });
  
  function askQuestion(question) {
    console.log("Inside askQuestion, question is: ", question);
    
    const request = {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        question: question
      })
    };
    
    fetch("/answer", request)
      .then(response => response.json())
      .then(data => {
        console.log("Response from server: ", data);
        chatHistory.push({ name: 'Guru', message: data.answer });
        updateChatDisplay();
      })
      .catch(error => console.error("Error: ", error));
  }
});
