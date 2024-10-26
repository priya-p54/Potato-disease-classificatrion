<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# Potato Disease Predictor 🌱🥔

## Basic Details
### Team Name: DATA WIZARDS

### Team Members
 Priya Mary Prince - Department of AI and Data Science, Viswajyothi College of Engineering and Technology, Kerala
 Sitalakshmi B - Department of AI and Data Science, Viswajyothi College of Engineering and Technology, Kerala

### Project Description
This project is a potato disease predictor that utilizes a convolutional neural network (CNN) to analyze images and identify diseases affecting potato plants.
Farmers every year face economic loss and crop waste due to various diseases in potato plants. We will use image classification using CNN and built a website using which a farmer can take a picture and site will tell you if the plant has a disease or not. Technology stack for this project will be,

Model Building: tensorflow, CNN, data augmentation, tf dataset

### The Problem (that doesn't exist)
Are your potato plants mysteriously wilting? Is your garden becoming a secret lair for diseases? We're tackling the non-existent crisis of potato plant health awareness!

### The Solution (that nobody asked for)
With our state-of-the-art, totally unnecessary website, you can simply upload a photo of your potato plant, and voilà! Get instant feedback on its health, all while having a great time!

## Technical Details
### Technologies/Components Used
For Software:
- **Languages Used**: Python
- **Frameworks Used**: TensorFlow, Keras, Tkinter
- **Libraries Used**: NumPy, PIL
- **Tools Used**: Jupyter Notebook, Visual Studio Code

For Hardware:
- **Components**: Any computer with a webcam (for capturing potato images)
- **Specifications**: Minimum 4GB RAM, TensorFlow-compatible GPU recommended
- **Tools Required**: Python environment, TensorFlow installation

### Implementation
For Software:

#### Installation
```bash
pip install numpy tensorflow pillow
```

#### Run
```bash
python potato_disease_predictor.py
```

### Project Documentation
For Software:

#### Screenshots
https://drive.google.com/file/d/1XGd5VBvBCAU4U0lVzsm8yaacZ751yAZw/view?usp=sharing
*This screenshot shows the main interface of the app where users can upload images.*

https://drive.google.com/file/d/1O3k_2fKb0_wS99vUjvqZoZeZyjU69GQv/view?usp=sharing
*Here, the app displays the predicted disease and confidence level.*

 https://drive.google.com/file/d/1Ak1be8TSQ7vfX3gK1vg7VguhTyin_Dc6/view?usp=sharing
*This is the upload image dialog where users select a potato image for prediction.*


### Project Demo
#### Video
[Watch our demo video here](https://drive.google.com/file/d/1wjUwyYF6U5k6hlC1TKRHTKKIV5oX-tGq/view?usp=sharing)
*The video showcases the user experience and predictions made by the app.*

## Team Contributions
- Priya Mary Prince: Lead development of the CNN model and user interface design.
- Sitalakshmi: Image processing techniques and integration of prediction logic.

---

Made with ❤️ at TinkerHub Useless Projects

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)

---

## Code Snippets

Here's the core code for the potato disease prediction application:

```python
import tkinter as tk
from tkinter import filedialog, messagebox, font
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Plant Disease Prediction")
root.geometry("1500x1000")

# Load the model
model = tf.keras.models.load_model("path/to/your/model/potatoes.keras")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

def predict(img_path):
    img = keras_image.load_img(img_path, target_size=(256, 256))
    img_array = keras_image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    predictions = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

def upload_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path).resize((250, 250))
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk
        predicted_class, confidence = predict(file_path)
        messagebox.showinfo("Prediction", f"Predicted Class: {predicted_class}\nConfidence: {confidence}%")

# UI Setup
title_label = tk.Label(root, text="PLANT DISEASE PREDICTION", font=("Helvetica", 54, "bold"), fg='#00796b', bg='lightgreen')
title_label.pack(pady=20)

instruction_label = tk.Label(root, text="Select an image to predict the disease.", font=("Helvetica", 34, "bold"), fg='#005f5f', bg='lightgreen')
instruction_label.pack(pady=10)

panel = tk.Label(root)
panel.pack(padx=10, pady=10)

upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=20)

root.mainloop()
```

This code creates a simple GUI application that predicts the health of potato plants based on uploaded images, using a pre-trained CNN model.

---

With this README, your project not only gets an engaging overview but also showcases your innovative approach and technical prowess. Good luck with your project!
