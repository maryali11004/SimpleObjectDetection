# 🦗 **Simple Insect Detector** 🐜

Welcome to the **Simple Insect Detector**! This is a straightforward Python script designed to count insects in images using basic computer vision techniques.

## 🌟 **Features**

- **Grayscale Conversion**: Simplifies images for easier processing.
- **Basic Thresholding**: Filters out the background and isolates insects.
- **Contour Detection**: Counts and highlights insects in the image.
  
  
---

## 🚀 **Quick Start**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/insect-detector.git
   ```
2.**Install Dependencies**
   ```bash
   pip install opencv-python numpy matplotlib
```
3.**Run the script**
Replace 'ML-Intro/insect.jpeg' with the path to your image file and execute:
```bash
python insect_detector.py
```
---

## 📊 What You’ll See

- Histogram: A plot showing the distribution of pixel values in the grayscale image.
- Insects Detected: The number of insects detected and highlighted in the image.
---
## 🔧 Customization

Threshold Values: Modify lower_threshold and upper_threshold in the script to better detect insects based on your specific images.

---
## 💡 How It Works

- Read the Image: Loads the image and converts it to grayscale.
- Thresholding: Creates a mask to isolate background and foreground.
- Contour Detection: Identifies and counts the contours of detected insects.
- Display Results: Shows the histogram and the image with detected insects highlighted.
 ---
  
## 🤝 Contributions

Feel free to contribute or suggest improvements! For issues or feature requests, please open an issue on GitHub.

---

## 📷 Example


Here’s a sample of what the output looks like:
![inse](https://github.com/user-attachments/assets/e4c86efd-1bef-4b45-b54e-472289255a07)

---

## 📝 Notes

- Make sure your image path is correctly set in the script.
- Adjust threshold values according to your image for optimal results.




