// Generate a new session ID
function generateSessionId() {
  return 'session-' + Date.now() + '-' + Math.random().toString(36).substr(2, 9);
}

// Initialize session ID if not already set
if (!sessionStorage.getItem("sessionId")) {
  sessionStorage.setItem("sessionId", generateSessionId());
}

// Function to start a new chat session
document.querySelector(".btn-new-chat").addEventListener("click", function () {
  sessionStorage.setItem("sessionId", generateSessionId());
  document.getElementById("chatMessages").innerHTML = ""; // Clear chat messages
  // Add New Chat Indicator message
  const newChatMessage = document.createElement("div");
  newChatMessage.classList.add("message", "bot-message", "new-chat-message");
  newChatMessage.innerHTML = `<strong>Optaex</strong><br><em>New chat started!</em><br>How can I assist you today?`;
  chatMessages.appendChild(newChatMessage);
});

// Toggle sidebar on mobile
document.getElementById("sidebarToggle").addEventListener("click", function() {
  document.getElementById("sidebar").classList.toggle("active");
});

// Send message event listeners
document.getElementById("sendButton").addEventListener("click", sendMessage);
document.getElementById("userInput").addEventListener("keypress", function(e) {
  if (e.key === "Enter") sendMessage();
});

async function sendMessage() {
  const userInput = document.getElementById("userInput");
  const message = userInput.value.trim();
  
  if (!message) return;

  // Get session ID
  const sessionId = sessionStorage.getItem("sessionId");

  // Add user message to chat
  addMessageToChat('user', message);
  userInput.value = "";

  // Create loading indicator
  const loadingId = 'loading-' + Date.now();
  addLoadingIndicator(loadingId);

  try {
    // Send POST request to API
    const response = await fetch('http://localhost:5000/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ sessionId: sessionId, message: message })  // Include session ID
    });

    if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);

    const data = await response.json();
    
    // Remove loading and add API response with Markdown conversion
    removeLoadingIndicator(loadingId);
    addMessageToChat('assistant', data.response || "Sorry, I couldn't process that.", true);

  } catch (error) {
    console.error('API call failed:', error);
    removeLoadingIndicator(loadingId);
    addMessageToChat('assistant', "Sorry, there was an error processing your request.");
  }
}

// Helper function to add messages to chat
function addMessageToChat(sender, message, isMarkdown = false) {
  const chatMessages = document.getElementById("chatMessages");
  const messageClass = sender === 'user' ? 'user-message' : 'bot-message';
  const senderName = sender === 'user' ? 'You' : 'Assistant';

  // Create a new message element
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", messageClass);
  messageDiv.innerHTML = `<strong>${senderName}</strong><br>${message}`;
  chatMessages.appendChild(messageDiv);

  // If message is Markdown, convert it to HTML
  if (isMarkdown) {
    setTimeout(() => {
      messageDiv.innerHTML = `<strong>${senderName}</strong><br>${marked.parse(message)}`;
    }, 500); // Small delay for UX improvement
  }

  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Helper function to add loading indicator
function addLoadingIndicator(id) {
  const chatMessages = document.getElementById("chatMessages");
  const loadingDiv = document.createElement("div");
  loadingDiv.classList.add("message", "bot-message");
  loadingDiv.id = id;
  loadingDiv.innerHTML = `<strong>Assistant</strong><br><div class="loading-dots"><span></span><span></span><span></span></div>`;
  chatMessages.appendChild(loadingDiv);
  chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Helper function to remove loading indicator
function removeLoadingIndicator(id) {
  const element = document.getElementById(id);
  if (element) element.remove();
}

// Alert on page load
window.onload = function() {
  alert("Page has loaded successfully!");
};
