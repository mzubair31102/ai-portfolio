document.getElementById("fetchButton").addEventListener("click", fetchData);

function fetchData() {
    fetch("http://127.0.0.1:5000/api/data")
        .then(response => response.json())
        .then(data => displayData(data))
        .catch(error => console.error("Error fetching data:", error));
}

function displayData(data) {
    let container = document.getElementById("dataContainer");
    container.innerHTML = ""; // Clear previous data

    data.forEach(item => {
        let card = document.createElement("div");
        card.className = "card";
        card.innerHTML = `<h3>ID: ${item[0]}</h3><p>${item[1]}</p>`;
        container.appendChild(card);
    });
}
