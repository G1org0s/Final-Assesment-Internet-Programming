
// DARK MODE

document.addEventListener("DOMContentLoaded", function () {
    const darkModeToggle = document.querySelector("#darkModeToggle");

    if (!darkModeToggle) {
        return;
    }

    if (localStorage.getItem("darkMode") === "enabled") {
        document.body.classList.add("dark-mode");
        darkModeToggle.textContent = "Light Mode";
    }

    darkModeToggle.addEventListener("click", function () {
        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {
            localStorage.setItem("darkMode", "enabled");
            darkModeToggle.textContent = "Light Mode";
        } else {
            localStorage.setItem("darkMode", "disabled");
            darkModeToggle.textContent = "Dark Mode";
        }
    });
});
