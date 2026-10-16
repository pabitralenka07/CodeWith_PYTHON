# 🐘 Lord Ganesh Python Color Sketch Drawing

A Python script that uses **OpenCV** and **Turtle Graphics** to draw a detailed, animated color sketch of Lord Ganesh (or any custom image) directly on screen in real time.

---

## ✨ Features

- 🎨 **Color Contour Sketching**: Uses OpenCV edge detection and contour extraction to outline and color-fill artwork.
- 🖥️ **80% Screen Coverage Box**: Automatically sets window dimensions to 80% of your screen size.
- ⚡ **Optimized Fast Animation**: Smooth turtle drawing powered by dynamic frame tracing (`screen.tracer(20, 0)`).
- 🖼️ **Custom Image Support**: Easily swap in any PNG/JPG photo (e.g. `ganesh.png`).

---

## 📋 Requirements

This project requires **Python 3.x** and the following packages:

- `opencv-python`
- `numpy`

### Installation

Install the required dependencies using pip:
```bash
pip install opencv-python numpy
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Place your image file (e.g., `ganesh.png`) in the project directory.
3. Run the drawing script:
   ```bash
   python ganesh.py
   ```
   *(or run `python krishna.py`)*

---

## ⚙️ Customization

- **Change Image**: Update the `image_path` variable in `ganesh.py`:
  ```python
  image_path = 'ganesh.png'
  ```
- **Adjust Animation Speed**: Modify the tracer setting to speed up or slow down the drawing animation:
  ```python
  screen.tracer(20, 0)  # Lower number = slower, Higher number = faster
  ```
- **Window Size**: Change the screen box percentage in `screen.setup()`:
  ```python
  screen.setup(width=0.8, height=0.8)  # 80% screen size
  ```
