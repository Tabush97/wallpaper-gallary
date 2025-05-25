const gallery = document.getElementById('gallery');
const categoryButtons = document.querySelectorAll('.category-button');

// How many images to try to load per category
const MAX_IMAGES = 20;

categoryButtons.forEach(button => {
  button.addEventListener('click', () => {
    const category = button.getAttribute('data-category');
    loadCategoryImages(category);
  });
});

function loadCategoryImages(category) {
  gallery.innerHTML = ''; // Clear previous content

  for (let i = 1; i <= MAX_IMAGES; i++) {
    const img = document.createElement('img');
    img.src = `/static/images/pc/${category}/${i}.jpg`;
    img.alt = `${category} wallpaper ${i}`;
    img.classList.add('thumbnail');

    // Only add the image to gallery if it loads successfully
    img.onload = () => {
      gallery.appendChild(img);
    };

    // If image fails to load (not found), stop trying further
    img.onerror = () => {
      // Stop loading more images when one is missing
      // Optionally remove this image element if needed
    };
  }
}
