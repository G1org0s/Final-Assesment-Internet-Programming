const dailyQuote = document.querySelector("#dailyQuote");
const newQuoteBtn = document.querySelector("#newQuoteBtn");

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

newQuoteBtn.addEventListener("click", changeQuote);
