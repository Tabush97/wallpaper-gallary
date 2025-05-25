from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Auto-reload templates

# Configuration
WALLPAPER_DIR = os.path.join('static', 'images')
DEVICES = {'Desktop': 'pc', 'Mobile': 'mobile'}

def get_wallpapers():
    wallpapers = {}
    categories = set()
    
    for device, folder in DEVICES.items():
        path = os.path.join(WALLPAPER_DIR, folder)
        wallpapers[device] = []
        
        for root, _, files in os.walk(path):
            category = os.path.basename(root)
            if category not in DEVICES.values():  # Skip base folders
                categories.add(category)
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                        wallpapers[device].append({
                            'url': os.path.join(root, file).replace('\\', '/'),
                            'category': category,
                            'filename': file
                        })
    
    return wallpapers, sorted(categories)

@app.route('/')
def home():
    wallpapers, categories = get_wallpapers()
    return render_template('index.html', wallpapers=wallpapers, categories=categories)

@app.route('/download/<device>/<path:filename>')
def download(device, filename):
    return send_from_directory(
        os.path.join(WALLPAPER_DIR, DEVICES[device]),
        filename,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True, extra_files=['templates/index.html'])  # Watch template files toofrom flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True  # Auto-reload templates

# Configuration
WALLPAPER_DIR = os.path.join('static', 'images')
DEVICES = {'Desktop': 'pc', 'Mobile': 'mobile'}

def get_wallpapers():
    wallpapers = {}
    categories = set()
    
    for device, folder in DEVICES.items():
        path = os.path.join(WALLPAPER_DIR, folder)
        wallpapers[device] = []
        
        for root, _, files in os.walk(path):
            category = os.path.basename(root)
            if category not in DEVICES.values():  # Skip base folders
                categories.add(category)
                for file in files:
                    if file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                        wallpapers[device].append({
                            'url': os.path.join(root, file).replace('\\', '/'),
                            'category': category,
                            'filename': file
                        })
    
    return wallpapers, sorted(categories)

@app.route('/')
def home():
    wallpapers, categories = get_wallpapers()
    return render_template('index.html', wallpapers=wallpapers, categories=categories)

@app.route('/download/<device>/<path:filename>')
def download(device, filename):
    return send_from_directory(
        os.path.join(WALLPAPER_DIR, DEVICES[device]),
        filename,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run(debug=True, extra_files=['templates/index.html'])  # Watch template files too