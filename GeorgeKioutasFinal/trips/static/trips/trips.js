const tripForm = document.querySelector("#tripForm");
const tripName = document.querySelector("#tripName");
const tripLocation = document.querySelector("#tripLocation");
const tripDate = document.querySelector("#tripDate");
const tripDescription = document.querySelector("#tripDescription");

const weatherResult = document.querySelector("#weatherResult");
const pendingTable = document.querySelector("#pendingTripsTable");
const completedTable = document.querySelector("#completedTripsTable");
const sortTrips = document.querySelector("#sortTrips");
const totalTrips = document.querySelector("#totalTrips");
const pendingTrips = document.querySelector("#pendingTrips");
const completedTrips = document.querySelector("#completedTrips");

// All trips are stored in localStorage so they stay after refresh.
const trips = JSON.parse(localStorage.getItem("fishTheBoxTrips") || "[]");

function saveTrips() {
    localStorage.setItem("fishTheBoxTrips", JSON.stringify(trips));
}

// The weather API gives a code, this function turns it to simple words.
function getWeatherText(code) {
    if (code === 0) {
        return "Clear sky";
    } else if (code <= 3) {
        return "Partly cloudy";
    } else if (code >= 51 && code <= 67) {
        return "Rain";
    } else if (code >= 80 && code <= 82) {
        return "Rain showers";
    } else if (code >= 95) {
        return "Thunderstorm";
    } else {
        return "Other weather";
    }
}

async function showWeather() {
    weatherResult.textContent = "Loading weather...";

    try {
        const url =
            "https://api.open-meteo.com/v1/forecast" +
            "?latitude=37.9838" +
            "&longitude=23.7275" +
            "&current=temperature_2m,weather_code" +
            "&timezone=Europe%2FAthens";

        const response = await fetch(url);
        const data = await response.json();

        const code = data.current.weather_code;
        const temperature = data.current.temperature_2m;

        weatherResult.textContent = getWeatherText(code) + " (" + temperature + " C)";
    } catch {
        weatherResult.textContent = "Today's weather is not available.";
    }
}

function showTrips() {
    // Clear the tables first, then create them again from the array.
    pendingTable.innerHTML = "";
    completedTable.innerHTML = "";

    let pendingCount = 0;
    let completedCount = 0;

    trips.sort(function (firstTrip, secondTrip) {
        // The select menu decides if the newest or earliest trip goes first.
        if (sortTrips.value === "latest") {
            if (firstTrip.date < secondTrip.date) {
                return 1;
            } else {
                return -1;
            }
        } else {
            if (firstTrip.date > secondTrip.date) {
                return 1;
            } else {
                return -1;
            }
        }
    });

    for (let i = 0; i < trips.length; i++) {
        let row;

        // Completed and pending trips goes in different tables.
        if (trips[i].status === "completed") {
            row = completedTable.insertRow();
            completedCount++;
        } else {
            row = pendingTable.insertRow();
            pendingCount++;
        }

        row.insertCell(0).textContent = trips[i].name;
        row.insertCell(1).textContent = trips[i].location;
        row.insertCell(2).textContent = trips[i].date;

        const buttonCell = row.insertCell(3);

        if (trips[i].status === "pending") {
            buttonCell.innerHTML = '<button type="button" class="btn btn-info btn-sm">Complete</button>';

            const completeButton = buttonCell.querySelector("button");

            completeButton.addEventListener("click", function () {
                completeTrip(i);
            });
        } else {
            buttonCell.innerHTML =
                '<button type="button" class="btn btn-warning btn-sm edit-button mb-2">Edit</button> ' +
                '<button type="button" class="btn btn-danger btn-sm delete-button">Delete</button>';

            const editButton = buttonCell.querySelector(".edit-button");
            const deleteButton = buttonCell.querySelector(".delete-button");

            editButton.addEventListener("click", function () {
                editTrip(i);
            });

            deleteButton.addEventListener("click", function () {
                deleteTrip(i);
            });
        }
    }

    totalTrips.textContent = trips.length;
    pendingTrips.textContent = pendingCount;
    completedTrips.textContent = completedCount;
}

function completeTrip(index) {
    trips[index].status = "completed";
    saveTrips();
    showTrips();
}

function editTrip(index) {
    const newName = prompt("Edit the trip name:", trips[index].name);

    if (newName === null) {
        return;
    }

    const newLocation = prompt("Edit the location:", trips[index].location);

    if (newLocation === null) {
        return;
    }

    const newDate = prompt("Edit the date:", trips[index].date);

    if (newDate === null) {
        return;
    }

    const newDescription = prompt("Edit the description:", trips[index].description);

    if (newDescription === null) {
        return;
    }

    trips[index].name = newName;
    trips[index].location = newLocation;
    trips[index].date = newDate;
    trips[index].description = newDescription;

    saveTrips();
    showTrips();
}

function deleteTrip(index) {
    trips.splice(index, 1);
    saveTrips();
    showTrips();
}

function addTrip(event) {
    event.preventDefault();

    // This object keeps all the input values for one trip.
    const newTrip = {
        name: tripName.value,
        location: tripLocation.value,
        date: tripDate.value,
        description: tripDescription.value,
        status: "pending"
    };

    trips.push(newTrip);
    saveTrips();
    showTrips();
    tripForm.reset();
}

const today = new Date().toISOString().split("T")[0];
tripDate.min = today;

showWeather();
showTrips();

tripForm.addEventListener("submit", addTrip);
sortTrips.addEventListener("change", showTrips);
