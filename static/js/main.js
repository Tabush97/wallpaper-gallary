// Smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Fade-in effect for images on page load
window.addEventListener('load', () => {
  const images = document.querySelectorAll('img');
  images.forEach(img => {
    img.style.opacity = 0;
    img.style.transition = 'opacity 1s ease-in-out';
    setTimeout(() => {
      img.style.opacity = 1;
    }, 100);
  });
});
