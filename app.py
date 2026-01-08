from flask import Flask, render_template, request, send_file, jsonify
from PIL import Image
import os
import uuid
from PIL import Image, ImageFilter, ImageEnhance



app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
OUTPUT_FOLDER = "static/output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/preview", methods=["POST"])
def preview_image():
    file = request.files.get("image")
    operation = request.form.get("operation")

    if not file or not operation:
        return jsonify({"error": "Missing image or operation"})

    img = Image.open(file)

    if operation == "cgray":
     img = img.convert("L")
     ext = "jpg"

    elif operation == "resize":
     img = img.resize((800, 800))
     ext = "jpg"

    elif operation == "rotate":
     img = img.rotate(90, expand=True)
     ext = "jpg"

    elif operation == "blur":
     img = img.filter(ImageFilter.BLUR)
     ext = "jpg"

    elif operation == "sharpen":
     img = img.filter(ImageFilter.SHARPEN)
     ext = "jpg"

    elif operation == "edge":
     img = img.filter(ImageFilter.FIND_EDGES)
     ext = "jpg"

    elif operation == "contrast":
     enhancer = ImageEnhance.Contrast(img)
     img = enhancer.enhance(1.8)
     ext = "jpg"

    elif operation == "brightness":
     enhancer = ImageEnhance.Brightness(img)
     img = enhancer.enhance(1.5)
     ext = "jpg"

    elif operation == "sepia":
     img = img.convert("RGB")
     pixels = img.load()
     for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]
            tr = int(0.393*r + 0.769*g + 0.189*b)
            tg = int(0.349*r + 0.686*g + 0.168*b)
            tb = int(0.272*r + 0.534*g + 0.131*b)
            pixels[x, y] = (min(tr,255), min(tg,255), min(tb,255))
    ext = "jpg"


    filename = f"preview_{uuid.uuid4()}.{ext}"
    path = os.path.join(OUTPUT_FOLDER, filename)
    img.save(path)

    return jsonify({"preview_url": f"/static/output/{filename}"})


@app.route("/edit", methods=["POST"])
def edit_image():
    file = request.files.get("image")
    operation = request.form.get("operation")

    if not file or not operation:
        return "Missing image or operation"

    img = Image.open(file)

    if operation == "cgray":
        img = img.convert("L")
        ext = "jpg"
    elif operation == "cpng":
        ext = "png"
    elif operation == "cwebp":
        ext = "webp"
    elif operation == "cjpg":
        ext = "jpg"
    else:
        return "Invalid operation"

    filename = f"{uuid.uuid4()}.{ext}"
    path = os.path.join(OUTPUT_FOLDER, filename)
    img.save(path)

    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
