
// DARK MODE

document.addEventListener("DOMContentLoaded", function () {
    // Find the dark mode button after the page has loaded
    const darkModeToggle = document.querySelector("#darkModeToggle");

    // Stop here if this page does not contain the button
    if (!darkModeToggle) {
        return;
    }

    // Keep dark mode after the user moves to another page
    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
        darkModeToggle.textContent = "Light Mode";
    }

    // Change the page colours whenever the button is pressed
    darkModeToggle.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");

        // Save the selected mode and change the button text
        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
            darkModeToggle.textContent = "Light Mode";
        } else {
            localStorage.setItem("darkMode", "disabled");
            darkModeToggle.textContent = "Dark Mode";
        }
    });
});
