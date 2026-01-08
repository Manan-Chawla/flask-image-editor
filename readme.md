# 🖼️ Flask Image Editor Web App

A **Flask-based Image Editor Web Application** that allows users to upload images, apply multiple image processing operations **with live preview**, and download the final edited image — **without using OpenCV** (fully compatible with newer Python versions like 3.13 / 3.14).

This project is beginner-friendly and demonstrates **Flask backend + frontend interaction + image processing using Pillow (PIL)**.

---

## 📌 Features

### ✅ Core Features
- Upload images from device
- Select image operations from dropdown
- Live preview before downloading
- Download processed image
- No OpenCV dependency

### 🎨 Image Operations Supported
- Convert to Grayscale
- Resize Image (800 × 800)
- Rotate Image (90°)
- Blur
- Sharpen
- Edge Detection
- Increase Contrast
- Increase Brightness
- Sepia Filter
- Convert image format (JPG / PNG / WEBP)

---

## 🛠️ Tech Stack Used

| Technology | Purpose |
|----------|--------|
| Python | Backend logic |
| Flask | Web framework |
| Pillow (PIL) | Image processing |
| HTML5 | Frontend structure |
| CSS / Bootstrap | Styling |
| JavaScript | Live preview |
| UUID | Unique filenames |
| JSON API | Preview response |

---

## 📂 Project Structure
flask-image-editor/
│
├── app.py                     # Main Flask application
├── README.md                  # Project documentation
│
├── templates/
│   └── index.html             # Main UI page
│
├── static/
│   ├── uploads/               # Uploaded images (temporary)
│   └── output/                # Processed & preview images
│
└── requirements.txt           # Python dependencies




---

## 🚀 How the Application Works

1. User opens homepage
2. Uploads an image
3. Selects an operation
4. Image is sent to backend for preview
5. Processed image preview is returned
6. User downloads final image

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Manan-Chawla/flask-image-editor
cd flask-image-editor

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv

Activate:
Windows --> venv\Scripts\activate


3️⃣ Install Dependencies
pip install flask pillow



4️⃣ Run Application
python app.py


🌐 Frontend Features
- Navbar with multiple sections
- Side panel for live preview
- JavaScript Fetch API
- No page reloads

🚧 Current Limitations
- No crop tool
- Fixed resize dimensions
- Single operation at a time
- No undo functionality


🔮 Future Enhancements
- Sliders for brightness & contrast
- Crop and flip options
- Multiple filters chaining
- Before/After comparison
- User authentication
- Deployment on cloud




