const navbar = document.querySelector("#navbar");

// First check if the user is logged in and can manage products
// This is for managers and salesmen because they need the manage page
if (userIsLoggedIn == "True" && userCanManageProducts == "True") {
    // innerHTML places the navbar code inside the empty navbar div
    navbar.innerHTML = `
        <nav class="navbar navbar-expand-lg navbar-dark p-0">
            <!-- This button appears only when the browser gets small -->
            <!-- It opens and closes the navbar links on small screens -->
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
                <!-- These are the links that managers and salesmen can use -->
                <div class="d-grid d-lg-flex gap-2 gap-lg-3 mt-3 mt-lg-0">
                    <a href="/home/" class="btn btn-light">Home</a>
                    <a href="/shop/" class="btn btn-light">Shop</a>
                    <a href="/trips/" class="btn btn-light">Trips</a>
                    <!-- Only managers and salesmen see this button -->
                    <a href="/shop/manage/" class="btn btn-light">Manage Products</a>
                    <a href="/reviews/" class="btn btn-light">Reviews</a>
                    <a href="/about/" class="btn btn-light">About</a>
                    <a href="/contact/" class="btn btn-light">Contact</a>

                    <button id="darkModeToggle" class="btn btn-dark" type="button">
                        Dark Mode
                    </button>

                    <!-- Profile and cart are also useful for logged in staff users -->
                    <a href="/profile/" class="btn btn-light">Profile</a>
                    <a href="/cart/" class="btn btn-light"><i class="bi bi-cart"></i></a>
                    <a href="/logout/" class="btn btn-light">Logout</a>
                </div>
            </div>
        </nav>
    `;
}

// If the user is logged in as a normal customer
else if (userIsLoggedIn == "True") {
    // This version does not show Manage Products
    navbar.innerHTML = `
        <nav class="navbar navbar-expand-lg navbar-dark p-0">
            <!-- This button appears only when the browser gets small -->
            <!-- It opens and closes the navbar links on small screens -->
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
                <!-- These are the normal links for a logged in customer -->
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

                    <!-- Customers can open their profile, cart, and logout -->
                    <a href="/profile/" class="btn btn-light">Profile</a>
                    <a href="/cart/" class="btn btn-light"><i class="bi bi-cart"></i></a>
                    <a href="/logout/" class="btn btn-light">Logout</a>
                </div>
            </div>
        </nav>
    `;
}

// If the user is not logged in, show the public navbar
else {
    // It shows Register and Login instead of Logout
    navbar.innerHTML = `
        <nav class="navbar navbar-expand-lg navbar-dark p-0">
            <!-- This button appears only when the browser gets small -->
            <!-- It opens and closes the navbar links on small screens -->
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
                <!-- These links are shown to visitors before login -->
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

                    <!-- Public visitors can still open profile, but Django sends them to login -->
                    <a href="/profile/" class="btn btn-light">Profile</a>
                    <a href="/cart/" class="btn btn-light"><i class="bi bi-cart"></i></a>
                    <a href="/register/" class="btn btn-light">Register</a>
                    <a href="/login/" class="btn btn-light">Login</a>
                </div>
            </div>
        </nav>
    `;
}
