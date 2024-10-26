import tkinter as tk
from tkinter import filedialog, messagebox, font
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Plant Disease Prediction")
root.geometry("1500x1000")  # Set the size of the window

# Load the model
model = tf.keras.models.load_model("../potatoes.keras")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

# Load background image
try:
    bg_image = Image.open("C:/Users/acer/potato_disease/background.png")  # Replace with your image file path
    bg_image = bg_image.resize((1500, 1000))  # Resize to fit the window
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Create a Label to hold the background image
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)  # Make the label fill the window
except Exception as e:
    print(f"Error loading background image: {e}")

def predict(img_path):
    img = keras_image.load_img(img_path, target_size=(256, 256))
    img_array = keras_image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize the image
    predictions = model.predict(img_array)
    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)
    return predicted_class, confidence

def upload_image():
    file_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img = img.resize((250, 250))  # Resize for display
        img_tk = ImageTk.PhotoImage(img)

        # Update the panel with the uploaded image
        panel.config(image=img_tk)
        panel.image = img_tk  # Keep a reference to avoid garbage collection

        # Predict the image
        predicted_class, confidence = predict(file_path)
        messagebox.showinfo("Prediction", f"Predicted Class: {predicted_class}\nConfidence: {confidence}%")

# Custom font
custom_font = font.Font(family="Helvetica", size=34, weight="bold")

# Title label
title_label = tk.Label(root, text="PLANT DISEASE PREDICTION", font=("Helvetica", 54, "bold"), fg='#00796b', bg='lightgreen')
title_label.pack(pady=20)

# Instruction label
instruction_label = tk.Label(root, text="Select an image to predict the disease.", font=custom_font, fg='#005f5f', bg='lightgreen')
instruction_label.pack(pady=10)

# Create a panel for the image
panel = tk.Label(root)
panel.pack(padx=10, pady=10)

# Create upload button
upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=20)

# Run the GUI
root.mainloop()
