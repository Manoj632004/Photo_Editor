import os
from flask import Flask, render_template, request, redirect, url_for, send_file
from PIL import Image, ImageEnhance, ImageFilter
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file part"
    file = request.files['image']
    if file.filename == '':
        return "No selected file"
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return redirect(url_for('edit_image', filename=filename))

@app.route('/edit/<filename>', methods=['GET', 'POST'])
def edit_image(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img = Image.open(filepath)

    # Store edited image in a session variable if POST
    if request.method == 'POST':
        operations = request.form.getlist('operations')
        img = Image.open(filepath)  # Reset to original image

        # Apply operations based on selected checkboxes
        if 'blur' in operations:
            img = img.filter(ImageFilter.BLUR)
        if 'emboss' in operations:
            img = img.filter(ImageFilter.EMBOSS)
        if 'contour' in operations:
            img = img.filter(ImageFilter.CONTOUR)
        if 'smooth' in operations:
            img = img.filter(ImageFilter.SMOOTH)
        if 'mirror' in operations:
            img = ImageOps.mirror(img)
        if 'sharpen' in operations:
            img = img.filter(ImageFilter.SHARPEN)
        if 'solarize' in operations:
            img = ImageOps.solarize(img)
        if 'grayscale' in operations:
            img = img.convert('L')
        if 'crop' in operations:
            img = img.crop((50, 50, img.width - 50, img.height - 50))  # Example crop
        if 'brightness' in operations:
            brightness_factor = float(request.form.get('brightness_value', 1))
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness_factor)
        if 'rotate' in operations:
            angle = int(request.form.get('rotate_value', 0))
            img = img.rotate(angle)

        # Save the edited image
        img.save(filepath)
        return redirect(url_for('edit_image', filename=filename))

    return render_template('edit.html', filename=filename)

@app.route('/download/<filename>')
def download_image(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
