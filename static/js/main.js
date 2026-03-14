document.addEventListener("DOMContentLoaded", function () {
    // Reveal animation
    const revealItems = document.querySelectorAll(
        ".reveal, .reveal-up, .reveal-left, .reveal-right, .slide-left, .slide-right"
    );

    if (revealItems.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("active");
                }
            });
        }, {
            threshold: 0.15
        });

        revealItems.forEach((item) => observer.observe(item));
    }

    // Portfolio image slider
    const sliders = document.querySelectorAll(".portfolio-slider");

    sliders.forEach((slider) => {
        const img = slider.querySelector("img");
        const imagesAttr = slider.getAttribute("data-images");

        if (!img || !imagesAttr) return;

        const images = imagesAttr.split(",").map(item => item.trim()).filter(Boolean);

        if (images.length < 2) return;

        let currentIndex = 0;

        slider.addEventListener("click", function () {
            slider.classList.add("is-switching");

            setTimeout(() => {
                currentIndex = (currentIndex + 1) % images.length;
                img.src = images[currentIndex];
                slider.classList.remove("is-switching");
            }, 180);
        });
    });
});