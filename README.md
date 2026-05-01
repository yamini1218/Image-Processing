# 📸 Image Processing App

A simple and interactive **Image Editor built with Streamlit** that allows users to upload an image, apply multiple filters, and download the processed result.

---

## ✨ Features

* 📤 Upload images (JPG, JPEG, PNG)
* 🎚 Adjustable filters:

  * Blur
  * Sharpness
  * Brightness
  * Contrast
* 🖤 Grayscale conversion
* 🧠 Edge Detection (Canny with adjustable thresholds)
* 📐 Resize image (width & height)
* 🔄 Real-time processing
* 📥 Download processed image
* 🖼 Side-by-side comparison (Original vs Processed)

---

## 🛠 Tech Stack

* **Frontend/UI:** Streamlit
* **Image Processing:** PIL (Pillow), OpenCV
* **Backend Logic:** Python
* **Utilities:** NumPy

---

## 📁 Project Structure

```
image-editor/
│── app.py          # Main Streamlit app
│── filters.py      # Image processing pipeline
│── utils.py        # Helper functions
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/image-editor.git
cd image-editor
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the App

```
streamlit run app.py
```

Then open the local URL shown in terminal.

---

## 🎯 How It Works

1. Upload an image
2. Adjust filters using sidebar sliders
3. Toggle features like grayscale or edge detection
4. View processed output in real-time
5. Download the final image

---

## 🧠 Key Concepts Used

* Image transformations using PIL
* Edge detection using OpenCV (Canny Algorithm)
* Streamlit UI components (sliders, toggles, columns)
* Modular code design (separating filters and utilities)

---

## 🚀 Future Improvements

* 🎨 More filters (cartoon, sketch, HDR)
* 🖱 Drag slider comparison (before/after)
* ⚡ Performance optimization
* 🌐 Deployment (Streamlit Cloud)
* 📱 Better UI/UX design

---

## 🤝 Contributing

Feel free to fork this repo and improve it. Pull requests are welcome.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Built by **Yamini**
