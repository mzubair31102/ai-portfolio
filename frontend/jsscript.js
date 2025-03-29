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
    const message = encodeURIComponent(userInput.value.trim()); // Encode message for URL

    if (!message) return;

    // Add user message to chat
    addMessageToChat('user', userInput.value.trim());
    userInput.value = "";
    
    // Create loading indicator
    const loadingId = 'loading-' + Date.now();
    addLoadingIndicator(loadingId);
    
    try {
      // Send GET request to API with message as a query parameter
      const response = await fetch(`http://localhost:5000/api/chat?message=${message}`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        }
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
