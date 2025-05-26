let currentPage = 1;
let hasMore = true;
let currentFilters = { category: 'all', search: '' };

async function loadWallpapers() {
    let url = `/api/wallpapers?page=${currentPage}&limit=20`;
    if (currentFilters.category && currentFilters.category !== 'all') {
        url += `&category=${currentFilters.category}`;
    }
    if (currentFilters.search) {
        url += `&search=${currentFilters.search}`;
    }
    const response = await fetch(url);
    const data = await response.json();
    data.wallpapers.forEach(wallpaper => {
        const galleryItem = document.createElement('div');
        galleryItem.classList.add('gallery-item');
        galleryItem.innerHTML = `
            <img src="${wallpaper.thumbnail}" alt="Wallpaper" loading="lazy">
            <div class="overlay">
                <a href="${wallpaper.url}" download class="download-btn">Download</a>
            </div>
        `;
        document.getElementById('gallery').appendChild(galleryItem);
    });
    hasMore = data.has_more;
    document.getElementById('loadMore').style.display = hasMore ? 'block' : 'none';
}

// Initial load
loadWallpapers();

// Load more button
document.getElementById('loadMore').addEventListener('click', () => {
    if (hasMore) {
        currentPage++;
        loadWallpapers();
    }
});

// Category buttons
document.querySelectorAll('.category-btn').forEach(button => {
    button.addEventListener('click', () => {
        document.querySelector('.category-btn.active').classList.remove('active');
        button.classList.add('active');
        currentFilters.category = button.dataset.category;
        currentPage = 1;
        document.getElementById('gallery').innerHTML = '';
        loadWallpapers();
    });
});

// Search input
document.getElementById('searchInput').addEventListener('input', function(e) {
    currentFilters.search = e.target.value;
    currentPage = 1;
    document.getElementById('gallery').innerHTML = '';
    loadWallpapers();
});

// Theme toggle
document.getElementById('themeToggle').addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    const icon = document.querySelector('#themeToggle i');
    icon.classList.toggle('fa-moon');
    icon.classList.toggle('fa-sun');
});