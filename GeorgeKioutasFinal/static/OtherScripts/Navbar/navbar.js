// Find the empty navbar area from each html page
const navbar = document.querySelector("#navbar");

// This stays empty for customers and public users
let manageProductsButton = "";

// The profile button is shown for every visitor
let profileButton = `<a href="/profile/" class="btn btn-light">Profile</a>`;

// Add the management link only for managers and salesmen
if (userCanManageProducts == "True") {
    manageProductsButton = `<a href="/shop/manage/" class="btn btn-light">Manage Products</a>`;
}

// This navbar is shown when the user is logged in
if (userIsLoggedIn == "True") {
    // innerHTML places the shared navbar inside the empty navbar area
    navbar.innerHTML = `
        <nav class="navbar navbar-expand-lg navbar-dark p-0">
            <!-- This button appears only when the browser gets small -->
            <button class="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#mainNavbar"
                    aria-controls="mainNavbar"
                    aria-expanded="false"
                    aria-label="Open navigation menu">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="mainNavbar">
                <div class="d-grid d-lg-flex gap-2 gap-lg-3 mt-3 mt-lg-0">
                    <a href="/home/" class="btn btn-light">Home</a>
                    <a href="/shop/" class="btn btn-light">Shop</a>
                    <a href="/trips/" class="btn btn-light">Trips</a>
                    ${manageProductsButton}

                    <a href="/reviews/" class="btn btn-light">Reviews</a>
                    <a href="/about/" class="btn btn-light">About</a>
                    <a href="/contact/" class="btn btn-light">Contact</a>

                    <button id="darkModeToggle" class="btn btn-dark" type="button">
                        Dark Mode
                    </button>

                    ${profileButton}
                    <a href="/logout/" class="btn btn-light">Logout</a>
                </div>
            </div>
        </nav>
    `;
} else {
    // This navbar is shown when the user is not logged in
    // It shows Register and Login instead of Logout
    navbar.innerHTML = `
        <nav class="navbar navbar-expand-lg navbar-dark p-0">
            <!-- This button appears only when the browser gets small -->
            <button class="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#mainNavbar"
                    aria-controls="mainNavbar"
                    aria-expanded="false"
                    aria-label="Open navigation menu">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="mainNavbar">
                <div class="d-grid d-lg-flex gap-2 gap-lg-3 mt-3 mt-lg-0">
                    <a href="/home/" class="btn btn-light">Home</a>
                    <a href="/shop/" class="btn btn-light">Shop</a>
                    <a href="/trips/" class="btn btn-light">Trips</a>

                    <a href="/reviews/" class="btn btn-light">Reviews</a>
                    <a href="/about/" class="btn btn-light">About</a>
                    <a href="/contact/" class="btn btn-light">Contact</a>

                    <button id="darkModeToggle" class="btn btn-dark" type="button">
                        Dark Mode
                    </button>

                    ${profileButton}
                    <a href="/register/" class="btn btn-light">Register</a>
                    <a href="/login/" class="btn btn-light">Login</a>
                </div>
            </div>
        </nav>
    `;
}
