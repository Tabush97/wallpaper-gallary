import os
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

def get_all_wallpapers():
    wallpapers = []
    base_path = 'static/images'
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')) and not file.lower().endswith('-thumb.jpg'):
                path = os.path.join(root, file).replace('\\', '/')  # Fix for Windows paths
                relative_path = '/' + path
                category = os.path.basename(root)
                parent_folder = os.path.basename(os.path.dirname(root))
                device_type = parent_folder if parent_folder in ['mobile', 'pc'] else 'general'
                # Look for category-specific thumbnail (e.g., gaming-thumb.jpg)
                thumb_filename = f"{category.lower()}-thumb.jpg"
                thumb_path = f"/{base_path}/{parent_folder}/{category}/{thumb_filename}"
                # Fallback to main image if thumbnail is missing
                if not os.path.exists(os.path.join(app.root_path, thumb_path[1:])):
                    thumb_path = relative_path
                wallpapers.append({
                    'url': relative_path,
                    'thumbnail': thumb_path,
                    'category': category,
                    'device_type': device_type,
                    'tags': [category.lower(), device_type.lower()]
                })
    return wallpapers

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/wallpapers')
def api_wallpapers():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 20, type=int)
    category = request.args.get('category', None)
    search = request.args.get('search', None)
    
    all_wallpapers = get_all_wallpapers()
    filtered_wallpapers = all_wallpapers
    
    if category and category != 'all':
        filtered_wallpapers = [w for w in filtered_wallpapers if w['category'].lower() == category.lower()]
    
    if search:
        search_lower = search.lower()
        filtered_wallpapers = [w for w in filtered_wallpapers if any(search_lower in tag for tag in w['tags'])]
    
    total = len(filtered_wallpapers)
    start = (page - 1) * limit
    end = start + limit
    paginated_wallpapers = filtered_wallpapers[start:end]
    has_more = end < total
    
    return jsonify({
        'wallpapers': paginated_wallpapers,
        'total': total,
        'page': page,
        'has_more': has_more
    })

if __name__ == '__main__':
    app.run(debug=True)