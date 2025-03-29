document.getElementById("fetchButton").addEventListener("click", fetchData);

function getBaseApiUrl() {
    const isLocal = ["127.0.0.1", "localhost"].includes(window.location.hostname);
    return isLocal 
        ? `${window.location.protocol}//${window.location.hostname}:5000` 
        : "https://aiportfolio-dns.eastus.azurecontainer.io";
}

function getApiUrl(endpoint) {
    return `${getBaseApiUrl()}${endpoint}`;
}

function fetchData() {
    const apiUrl = getApiUrl("/api/data");

    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => displayData(data))
        .catch(error => console.error("Error fetching data:", error));
}

function displayData(data) {
    let container = document.getElementById("dataContainer");
    container.innerHTML = ""; // Clear previous data

    data.forEach(item => {
        let card = createCard(item);
        container.appendChild(card);
    });
}

function createCard(item) {
    let card = document.createElement("div");
    card.className = "card";
    card.innerHTML = `<h3>ID: ${item[0]}</h3><p>${item[1]}</p>`;
    return card;
}

























///////////////////////////
// Toggle sidebar on mobile
document.getElementById('sidebarToggle').addEventListener('click', function() {
    document.getElementById('sidebar').classList.toggle('active');
});

// Send message function
document.getElementById('sendButton').addEventListener('click', sendMessage);
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') sendMessage();
});

async function sendMessage() {
    const userInput = document.getElementById('userInput');
    const chatMessages = document.getElementById('chatMessages');

    if (userInput.value.trim() === '') return;

    // Add user message
    chatMessages.innerHTML += `
        <div class="message user-message">
            <strong>You</strong><br>
            ${userInput.value}
        </div>
    `;

    // Add loading indicator for bot
    const loadingId = 'loading-' + Date.now();
    chatMessages.innerHTML += `
        <div class="message bot-message" id="${loadingId}">
            <strong>ChatGPT</strong><br>
            <div class="loading-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;
    chatMessages.scrollTop = chatMessages.scrollHeight;

    // Simulate API call (replace with actual OpenAI API)
    try {
        const response = await fetchOpenAIResponse(userInput.value);
        
        // Replace loading with actual response
        document.getElementById(loadingId).innerHTML = `
            <strong>ChatGPT</strong><br>
            ${formatResponse(response)}
        `;
    } catch (error) {
        document.getElementById(loadingId).innerHTML = `
            <strong>ChatGPT</strong><br>
            <span class="text-danger">Error: ${error.message}</span>
        `;
    }

    userInput.value = '';
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Mock API call (replace with real OpenAI API)
async function fetchOpenAIResponse(query) {
    // Simulate network delay
    await new Promise(resolve => setTimeout(resolve, 1500));

    // Mock response (in a real app, replace with fetch() to OpenAI)
    const mockResponses = [
        "I'm a simulated response. In a real app, this would come from the OpenAI API.",
        "You asked: \"" + query + "\". Here's a detailed answer...",
        "Interesting question! Let me explain...",
        "I can help with that. Here are the steps:"
    ];
    return mockResponses[Math.floor(Math.random() * mockResponses.length)];
}

// Simple formatting (replace with a Markdown library if needed)
function formatResponse(text) {
    return text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')  // **bold**
        .replace(/\*(.*?)\*/g, '<em>$1</em>');              // *italic*
}