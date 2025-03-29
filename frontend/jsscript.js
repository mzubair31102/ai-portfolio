document.getElementById("sidebarToggle").addEventListener("click", function () {
  document.getElementById("sidebar").classList.toggle("active");
});

// Send message function
document.getElementById("sendButton").addEventListener("click", sendMessage);
document.getElementById("userInput").addEventListener("keypress", function (e) {
  if (e.key === "Enter") sendMessage();
});

async function sendMessage() {
  const userInput = document.getElementById("userInput");
  const chatMessages = document.getElementById("chatMessages");
  const message = userInput.value.trim();

  if (!message) return;

  // Add user message to chat
  addMessageToChat("user", message);
  userInput.value = "";

  // Create loading indicator
  const loadingId = "loading-" + Date.now();
  addLoadingIndicator(loadingId);

  try {
    // Send GET request to API
    const response = await fetch(`http://localhost:5000/api/chat?message=${encodeURIComponent(message)}`);

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();

    // Remove loading and add API response
    removeLoadingIndicator(loadingId);
    addMessageToChat("assistant", data.response || "Sorry, I couldn't process that.");
  } catch (error) {
    console.error("API call failed:", error);
    removeLoadingIndicator(loadingId);
    addMessageToChat("assistant", "Sorry, there was an error processing your request.");
  }
}

function addMessageToChat(sender, message) {
  const chatMessages = document.getElementById("chatMessages");
  const senderName = sender === "user" ? "You" : "Assistant";
  chatMessages.innerHTML += `<div class="message ${sender}-message"><strong>${senderName}</strong><br>${message}</div>`;
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Helper function to add loading indicator
function addLoadingIndicator(id) {
  const chatMessages = document.getElementById("chatMessages");
  const loadingHTML = `
    <div class="message bot-message" id="${id}">
      <strong>Assistant</strong><br>
      <div class="loading-dots">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>
  `;
  chatMessages.insertAdjacentHTML("beforeend", loadingHTML);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

function removeLoadingIndicator(id) {
  const element = document.getElementById(id);
  if (element) element.remove();
}

  window.onload = function() {
    alert("Page has loaded successfully!");
};
