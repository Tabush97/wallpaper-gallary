from flask import Flask, render_template, abort
import os

app = Flask(__name__)

IMAGE_FOLDER = os.path.join('static', 'images', 'pc')

@app.route('/')
def index():
    wallpapers = os.listdir(IMAGE_FOLDER)
    wallpapers = [img for img in wallpapers if img.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    return render_template('index.html', wallpapers=wallpapers)

@app.route('/wallpaper/<filename>')
def wallpaper(filename):
    # Security check: make sure file exists in folder and filename is safe
    if filename not in os.listdir(IMAGE_FOLDER):
        abort(404)
    return render_template('wallpaper.html', filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
