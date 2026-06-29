const dailyQuote = document.querySelector("#dailyQuote");
const newQuoteBtn = document.querySelector("#newQuoteBtn");
const lastActivity = document.querySelector("#lastActivity");

// These quotes are shown when the user press the quote button.
const quotes = [
    "A good day fishing is a good day outside.",
    "Fishing teaches patience one cast at a time.",
    "The best trips start with a simple plan.",
    "A calm sea makes every fishing trip better."
];

function changeQuote() {
    const randomNumber = Math.floor(Math.random() * quotes.length);
    dailyQuote.textContent = quotes[randomNumber];
}

function showLatestActivity() {
    // Trips are saved from the Trips page in the browser storage.
    const savedTrips = localStorage.getItem("fishTheBoxTrips");

    if (savedTrips === null) {
        lastActivity.innerHTML = "<li class='list-group-item'>No recent activity</li>";
        return;
    }

    const trips = JSON.parse(savedTrips);
    lastActivity.innerHTML = "";

    if (trips.length === 0) {
        lastActivity.innerHTML = "<li class='list-group-item'>No recent activity</li>";
        return;
    }

    trips.reverse();

    // Each trip becomes one item in the Latest Activity list.
    for (let i = 0; i < trips.length; i++) {
        const item = document.createElement("li");
        const status = document.createElement("span");

        item.className = "list-group-item d-flex justify-content-between align-items-center";
        item.textContent = trips[i].name + " - " + trips[i].location + " (" + trips[i].date + ")";

        if (trips[i].status === "completed") {
            status.textContent = "Completed";
            status.className = "badge bg-info text-dark";
        } else {
            status.textContent = "Pending";
            status.className = "badge bg-warning text-dark";
        }

        item.appendChild(status);
        lastActivity.appendChild(item);
    }
}

newQuoteBtn.addEventListener("click", changeQuote);
showLatestActivity();
