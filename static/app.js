let chatHistory = [];

let isRequestPending = false; // Variable, um den Status der aktuellen Anfrage zu verfolgen

function updateChatDisplay() {
    let chatDisplay = document.getElementById("chat-display");
    chatDisplay.innerHTML = '';

    chatHistory.forEach(chatItem => {
        let messageContainer = document.createElement('div');
        let nameElement = document.createElement('strong');
        let messageElement = document.createElement('span');

        if (chatItem.name === 'You') {
            nameElement.textContent = 'Kunde: ';
        } else {
            nameElement.textContent = 'Guru: ';
        }

        messageElement.textContent = chatItem.message;

        messageContainer.appendChild(nameElement);
        messageContainer.appendChild(messageElement);
        chatDisplay.appendChild(messageContainer);
    });
}

function askQuestion(question) {
    console.log("Inside askQuestion, question is: ", question);

    // Überprüfen, ob bereits eine Anfrage aussteht
    if (isRequestPending) {
        return;
    }

    // Extrahiert den Pfad aus der URL
    let category = window.location.pathname.slice(1); 
    if (category === '') {
        category = 'index';
    }
  
    const request = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            question: question
        })
    };
  
    // Setzen Sie den Status der aktuellen Anfrage auf "ausstehend"
    isRequestPending = true;

    fetch("/" + category, request)
        .then(response => response.json())
        .then(data => {
            console.log("Response from server: ", data);
            chatHistory.push({ name: 'Guru', message: data.answer });
            updateChatDisplay();
        })
        .catch(error => console.error("Error: ", error))
        .finally(() => {
            // Setzen Sie den Status der aktuellen Anfrage auf "nicht ausstehend"
            isRequestPending = false;
        });
}

// Event listeners for the send button and the question field
document.getElementById("sendButton").addEventListener("click", function(){
    var question = document.getElementById("questionField").value;

    // Überprüfen, ob bereits eine Anfrage aussteht
    if (isRequestPending) {
        return;
    }

    chatHistory.push({ name: 'You', message: question });
    document.getElementById("questionField").value = '';
    askQuestion(question);
});

// Allow pressing enter to send the question
document.getElementById("questionField").addEventListener("keyup", function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();

        // Überprüfen, ob bereits eine Anfrage aussteht
        if (isRequestPending) {
            return;
        }

        document.getElementById("sendButton").click();
    }
});
