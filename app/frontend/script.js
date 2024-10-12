function sendMessage(event) {
    if (event.key === "Enter") {
        var userInput = document.getElementById("user-input").value;
        var chatBody = document.getElementById("chat-body");
        
        // Display user message
        var userMessageDiv = document.createElement("div");
        userMessageDiv.classList.add("message", "user-message");
        userMessageDiv.textContent = userInput;
        chatBody.appendChild(userMessageDiv);

        // Simulate bot response (could be connected to backend)
        var botMessageDiv = document.createElement("div");
        botMessageDiv.classList.add("message", "bot-message");
        botMessageDiv.textContent = "Processing...";
        chatBody.appendChild(botMessageDiv);

        // Clear input field
        document.getElementById("user-input").value = "";
    }
}