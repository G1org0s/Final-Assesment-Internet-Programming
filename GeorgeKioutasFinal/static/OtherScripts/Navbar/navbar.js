const navbar = document.querySelector("#navbar");

// This navbar is shown when the user is logged in.
if (userIsLoggedIn == "True") {
    navbar.innerHTML = `
        <nav class="navbar navbar-expand-lg navbar-dark p-0">
            <!-- This button opens the full menu when screen is small. -->
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
                    <a href="/profile/" class="btn btn-light">Profile</a>

                    <!-- The extra pages are here so navbar dont get too full. -->
                    <div class="dropdown">
                        <button class="navbar-toggler d-block"
                                type="button"
                                data-bs-toggle="dropdown"
                                aria-expanded="false"
                                aria-label="Open more pages menu">
                            <span class="navbar-toggler-icon"></span>
                        </button>

                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="/analytics/">Analytics</a></li>
                            <li><a class="dropdown-item" href="/reviews/">Reviews</a></li>
                            <li><a class="dropdown-item" href="/about/">About</a></li>
                            <li><a class="dropdown-item" href="/contact/">Contact</a></li>
                        </ul>
                    </div>

                    <button id="darkModeToggle" class="btn btn-dark" type="button">
                        Dark Mode
                    </button>

                    <a href="/logout/" class="btn btn-light">Logout</a>
                </div>
            </div>
        </nav>
    `;
} else {
    // This navbar is shown when the user is not logged in.
    navbar.innerHTML = `
        <nav class="navbar navbar-expand-lg navbar-dark p-0">
            <!-- This button opens the full menu when screen is small. -->
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

                    <!-- The extra pages are here so navbar dont get too full. -->
                    <div class="dropdown">
                        <button class="navbar-toggler d-block"
                                type="button"
                                data-bs-toggle="dropdown"
                                aria-expanded="false"
                                aria-label="Open more pages menu">
                            <span class="navbar-toggler-icon"></span>
                        </button>

                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="/analytics/">Analytics</a></li>
                            <li><a class="dropdown-item" href="/reviews/">Reviews</a></li>
                            <li><a class="dropdown-item" href="/about/">About</a></li>
                            <li><a class="dropdown-item" href="/contact/">Contact</a></li>
                        </ul>
                    </div>

                    <button id="darkModeToggle" class="btn btn-dark" type="button">
                        Dark Mode
                    </button>

                    <a href="/register/" class="btn btn-light">Register</a>
                    <a href="/login/" class="btn btn-light">Login</a>
                </div>
            </div>
        </nav>
    `;
}
