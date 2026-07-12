// Find the empty footer area from each html page
const footer = document.querySelector("#footer");

// The same footer is placed in every page from here
footer.innerHTML = `
    <footer class="bg-light text-dark py-4">
        <div class="container d-flex justify-content-between align-items-center flex-wrap gap-4">
            <img src="/static/shop/logo.png" alt="Fish The.Box logo" width="100" height="80">

            <p class="mb-0">&copy; 2026 Fish The.Box. All rights reserved.</p>

            <p class="mb-0">
                Email:
                <a href="mailto:fishthebox@example.com">fishthebox@example.com</a>
            </p>

            <div class="d-flex gap-3 fs-3">
                <a href="https://github.com/G1org0s/Final-Assesment-Internet-Programming.git" aria-label="GitHub">
                    <i class="bi bi-github"></i>
                </a>
            </div>
        </div>
    </footer>
`;
