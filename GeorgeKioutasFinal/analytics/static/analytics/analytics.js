const trips = JSON.parse(localStorage.getItem("fishTheBoxTrips") || "[]");

const tripNames = [];
const tripNumbers = [];
const namesForChecking = [];

let totalCompletedTrips = 0;

// Only completed trips are counted for the analytics chart.
for (let i = 0; i < trips.length; i++) {
    if (trips[i].status === "completed") {
        totalCompletedTrips++;

        const nameForChecking = trips[i].name.trim().toLowerCase();
        const namePosition = namesForChecking.indexOf(nameForChecking);

        // Same trip names are counted together, even if capitals are different.
        if (namePosition === -1) {
            namesForChecking.push(nameForChecking);
            tripNames.push(trips[i].name.trim());
            tripNumbers.push(1);
        } else {
            tripNumbers[namePosition]++;
        }
    }
}

document.querySelector("#completedTripsTotal").textContent =
    "Total completed trips: " + totalCompletedTrips;

// Chart.js makes the pie chart from the arrays above.
new Chart(document.querySelector("#completedTripsChart"), {
    type: "pie",
    data: {
        labels: tripNames,
        datasets: [
            {
                data: tripNumbers,
                backgroundColor: [
                    "#03045e",
                    "#0077b6",
                    "#00b4d8",
                    "#90e0ef",
                    "#caf0f8",
                    "#1466fd",
                    "#1814d8"
                ]
            }
        ]
    }
});
