// MOBILE MENU
const menuToggle = document.getElementById("menuToggle");
const mobileMenu = document.getElementById("mobileMenu");

if (menuToggle) {
  menuToggle.addEventListener("click", () => {
    mobileMenu.classList.toggle("show");
    menuToggle.textContent = mobileMenu.classList.contains("show") ? "✕" : "☰";
  });
}

// CART COUNT
function updateCartCount() {
  const cart = JSON.parse(localStorage.getItem("sereignCart")) || [];
  const count = document.getElementById("cartCount");

  if (count) {
    count.textContent = cart.length;
  }
}

updateCartCount();

// HERO LIBRARY IMAGE ROTATION
const heroLibrary = document.getElementById("heroLibrary");

const libraryImages = [
  "assets/library-01.webp",
  "assets/library-02.webp",
  "assets/library-03.webp"
];

let currentLibrary = 0;

if (heroLibrary) {
  setInterval(() => {
    currentLibrary = (currentLibrary + 1) % libraryImages.length;

    heroLibrary.style.opacity = "0";

    setTimeout(() => {
      heroLibrary.src = libraryImages[currentLibrary];
      heroLibrary.style.opacity = "0.48";
    }, 500);

  }, 7000);
}

// SIMPLE SCROLL REVEAL
const revealElements = document.querySelectorAll(
  ".intro-section, .featured-section, .editions-section, .quote-section, .poems-preview"
);

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("revealed");
      }
    });
  },
  { threshold: 0.12 }
);

revealElements.forEach((element) => {
  element.classList.add("reveal");
  revealObserver.observe(element);
});