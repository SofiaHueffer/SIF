document.addEventListener("DOMContentLoaded", () => {
    // Check if the page was reloaded
    const navType = performance.getEntriesByType("navigation")[0]?.type || performance.navigation.type;

    if (navType === "reload" || navType === 1) {
        // Restore scroll position only if it's a reload
        const scrollY = localStorage.getItem("scrollY");
        if (scrollY !== null) {
            setTimeout(() => {
                window.scrollTo(0, parseInt(scrollY));
            }, 100); // Adjust delay if needed
        }
    } else {
        // Clear any stored scroll position on first load or normal navigation
        localStorage.removeItem("scrollY");
    }

    // Scroll animation observer
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("animate");
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.3
    });

    document.querySelectorAll(".about-text").forEach(el => {
        observer.observe(el);
    });

    // Dropdown mobile toggle
    const dropdowns = document.querySelectorAll(".dropdown-container");

    dropdowns.forEach(dropdown => {
        const label = dropdown.querySelector(".menu-label");
        if (label) {
            label.addEventListener("click", (e) => {
                e.preventDefault();
                dropdown.classList.toggle("active");
            });
        }
    });

    // Save scroll position before reload
    window.addEventListener("beforeunload", () => {
        localStorage.setItem("scrollY", window.scrollY);
    });
});

