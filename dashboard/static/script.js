const minSlider  = document.getElementById("minSlider");
const maxSlider  = document.getElementById("maxSlider");
const minValue   = document.getElementById("minValue");
const maxValue   = document.getElementById("maxValue");
const sliderFill = document.getElementById("sliderFill");

const MIN = 50, MAX = 500;

function updateSlider() {
  let lo = parseInt(minSlider.value);
  let hi = parseInt(maxSlider.value);

  // Keep minimum 50 gap
  if (lo > hi - 50) {
    if (this === minSlider) {
      lo = hi - 50;
      minSlider.value = lo;
    } else {
      hi = lo + 50;
      maxSlider.value = hi;
    }
  }

  minValue.textContent = lo;
  maxValue.textContent = hi;

  // Update orange fill between thumbs
  const leftPct  = ((lo - MIN) / (MAX - MIN)) * 100;
  const rightPct = ((hi - MIN) / (MAX - MIN)) * 100;
  sliderFill.style.left  = leftPct + "%";
  sliderFill.style.width = (rightPct - leftPct) + "%";
}

minSlider.addEventListener("input", function() { updateSlider.call(this); });
maxSlider.addEventListener("input", function() { updateSlider.call(this); });

// Init on page load
updateSlider.call(minSlider);

// Submit loading state
const form = document.getElementById("search-form");
if (form) {
  form.addEventListener("submit", () => {
    const btn = form.querySelector(".search-btn .btn-text");
    if (btn) btn.textContent = "Searching…";
  });
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener("click", e => {
    e.preventDefault();
    const target = document.querySelector(a.getAttribute("href"));
    if (target) target.scrollIntoView({ behavior: "smooth" });
  });
});

// Auto-scroll to results after submit
window.addEventListener("DOMContentLoaded", () => {
  const winner = document.querySelector(".winner-banner");
  if (winner) {
    setTimeout(() => {
      winner.scrollIntoView({ behavior: "smooth", block: "center" });
    }, 300);
  }
});