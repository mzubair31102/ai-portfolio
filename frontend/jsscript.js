
  // Toggle sidebar on mobile
  document.getElementById("sidebarToggle").addEventListener("click", function() {
    document.getElementById("sidebar").classList.toggle("active");
  });

  // Send message function
  document.getElementById("sendButton").addEventListener("click", sendMessage);
  document.getElementById("userInput").addEventListener("keypress", function(e) {
    if (e.key === "Enter") sendMessage();
  });

  async function sendMessage() {
    const userInput = document.getElementById("userInput");
    const chatMessages = document.getElementById("chatMessages");
    const message = userInput.value.trim();

    if (!message) return;

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
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      // Remove loading and add API response
      removeLoadingIndicator(loadingId);
      addMessageToChat('assistant', data.response || "Sorry, I couldn't process that.");
      
    } catch (error) {
      console.error('API call failed:', error);
      removeLoadingIndicator(loadingId);
      addMessageToChat('assistant', "Sorry, there was an error processing your request.");
    }
  }

  // Helper function to add messages to chat
  function addMessageToChat(sender, message) {
    const chatMessages = document.getElementById("chatMessages");
    const messageClass = sender === 'user' ? 'user-message' : 'bot-message';
    const senderName = sender === 'user' ? 'You' : 'Assistant';
    
    chatMessages.innerHTML += `
      <div class="message ${messageClass}">
        <strong>${senderName}</strong><br>
        ${message}
      </div>
    `;
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Helper function to add loading indicator
  function addLoadingIndicator(id) {
    const chatMessages = document.getElementById("chatMessages");
    chatMessages.innerHTML += `
      <div class="message bot-message" id="${id}">
        <strong>Assistant</strong><br>
        <div class="loading-dots">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    `;
    chatMessages.scrollTop = chatMessages.scrollHeight;
  }

  // Helper function to remove loading indicator
  function removeLoadingIndicator(id) {
    const element = document.getElementById(id);
    if (element) {
      element.remove();
    }
  }
  window.onload = function() {
    alert("Page has loaded successfully!");
};
