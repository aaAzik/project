// JavaScript to handle page transitions

function loadPage(pageId) {
    const pages = document.querySelectorAll('.page');

    // Hide all pages
    pages.forEach(page => {
        page.classList.remove('active');
    });

    // Show the selected page
    const selectedPage = document.getElementById(pageId);
    selectedPage.classList.add('active');
}

// Example: Show the initial page
loadPage('page1');

// Add similar event listeners for other pages or triggers
