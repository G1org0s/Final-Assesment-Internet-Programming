const reviewForm = document.querySelector("#reviewForm");
const reviewName = document.querySelector("#reviewName");
const reviewLocation = document.querySelector("#reviewLocation");
const fishCaught = document.querySelector("#fishCaught");
const reviewMessage = document.querySelector("#reviewMessage");
const recommendTrip = document.querySelector("#recommendTrip");
const reviewsTable = document.querySelector("#reviewsTable");
const noReviewsMessage = document.querySelector("#noReviewsMessage");
const clearReviews = document.querySelector("#clearReviews");

let reviews = [];

// If reviews already exist, load them from the browser.
const savedReviews = localStorage.getItem("fishTheBoxReviews");

if (savedReviews !== null) {
    reviews = JSON.parse(savedReviews);
}

function saveReviews() {
    localStorage.setItem("fishTheBoxReviews", JSON.stringify(reviews));
}

function showReviews() {
    reviewsTable.innerHTML = "";

    // Show this message when there is no review yet.
    if (reviews.length === 0) {
        noReviewsMessage.hidden = false;
        return;
    }

    noReviewsMessage.hidden = true;

    // Each saved review becomes a new row in the table.
    for (let i = 0; i < reviews.length; i++) {
        const row = reviewsTable.insertRow();

        row.insertCell(0).textContent = reviews[i].name;
        row.insertCell(1).textContent = reviews[i].location;
        row.insertCell(2).textContent = reviews[i].fish;
        row.insertCell(3).textContent = reviews[i].message;
        row.insertCell(4).textContent = reviews[i].recommend;
    }
}

function submitReview(event) {
    event.preventDefault();

    // One review is saved as one object with the form values.
    const newReview = {
        name: reviewName.value,
        location: reviewLocation.value,
        fish: fishCaught.value,
        message: reviewMessage.value,
        recommend: recommendTrip.value
    };

    reviews.push(newReview);
    saveReviews();
    showReviews();
    reviewForm.reset();

    alert("Your review was saved.");
}

function removeReviews() {
    // Empty the array and update localStorage also.
    reviews.length = 0;
    saveReviews();
    showReviews();
}

reviewForm.addEventListener("submit", submitReview);
clearReviews.addEventListener("click", removeReviews);
showReviews();
