from flask import Flask, render_template, abort
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Correct path using absolute path relative to this file
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
IMAGE_FOLDER = os.path.join(BASE_DIR, 'static', 'images', 'pc')

@app.route('/')
def index():
    wallpapers = os.listdir(IMAGE_FOLDER)
    wallpapers = [img for img in wallpapers if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    return render_template('index.html', wallpapers=wallpapers)

@app.route('/wallpaper/<filename>')
def wallpaper(filename):
    if filename not in os.listdir(IMAGE_FOLDER):
        abort(404)
    return render_template('wallpaper.html', filename=filename)

# Only for local testing
if __name__ == '__main__':
    app.run()
