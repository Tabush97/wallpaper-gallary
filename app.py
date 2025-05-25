from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# --- Configuration ---
WALLPAPER_DIR = os.path.join('static', 'images')
DEVICES = {'Desktop': 'pc', 'Mobile': 'mobile'}
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp'}

# --- Helper Functions ---
def is_allowed_file(filename):
    return os.path.splitext(filename)[1].lower() in ALLOWED_EXTENSIONS

def get_wallpapers():
    wallpapers = {}
    categories = set()

    for device, folder in DEVICES.items():
        path = os.path.join(WALLPAPER_DIR, folder)
        wallpapers[device] = []

        for root, _, files in os.walk(path):
            category = os.path.basename(root)
            if category not in DEVICES.values():
                categories.add(category)
                for file in files:
                    if is_allowed_file(file):
                        wallpapers[device].append({
                            'url': os.path.join(root, file).replace('\\', '/'),
                            'category': category,
                            'filename': file
                        })

    return wallpapers, sorted(categories)

# --- Routes ---
@app.route('/')
def home():
    wallpapers, categories = get_wallpapers()
    return render_template('index.html', wallpapers=wallpapers, categories=categories)

@app.route('/download/<device>/<path:filename>')
def download(device, filename):
    if device not in DEVICES:
        abort(404)

    # Security: prevent directory traversal
    safe_path = os.path.normpath(filename)
    if '..' in safe_path or safe_path.startswith('/'):
        abort(403)

    directory = os.path.join(WALLPAPER_DIR, DEVICES[device])
    file_path = os.path.join(directory, filename)

    if not os.path.isfile(file_path) or not is_allowed_file(filename):
        abort(404)

    return send_from_directory(directory, filename, as_attachment=True)

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)
