document.addEventListener("DOMContentLoaded", () => {
    const scrollY = localStorage.getItem("scrollY");
    if (scrollY !== null) {
        setTimeout(() => {
            window.scrollTo(0, parseInt(scrollY));
        }, 100); 
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
});

// Save scroll position before page unload
window.addEventListener("beforeunload", () => {
    localStorage.setItem("scrollY", window.scrollY);
});
