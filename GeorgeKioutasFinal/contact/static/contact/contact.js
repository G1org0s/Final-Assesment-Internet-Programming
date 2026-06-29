const contactForm = document.querySelector("#contactForm");
const contactName = document.querySelector("#contactName");
const contactEmail = document.querySelector("#contactEmail");
const contactSubject = document.querySelector("#contactSubject");
const contactMessage = document.querySelector("#contactMessage");

function submitContactForm(event) {
    // Stop the form from reloading the page after submit.
    event.preventDefault();

    // This message shows the details that user typed.
    const confirmation =
        "Thank you, " + contactName.value + "!\n" +
        "Email: " + contactEmail.value + "\n" +
        "Subject: " + contactSubject.value + "\n" +
        "Message: " + contactMessage.value;

    alert(confirmation);
    contactForm.reset();
}

contactForm.addEventListener("submit", submitContactForm);
