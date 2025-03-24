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
