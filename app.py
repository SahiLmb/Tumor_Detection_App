from flask import Flask, render_template, request, send_file
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import tensorflow as tf
import cv2
from tensorflow.keras.models import load_model
import secrets
import os
import shutil
from fpdf import FPDF
from pdf2image import convert_from_path


app = Flask(__name__)

# Load the VGG16 model
model = load_model('saved_model\Brain_Tumor_Vgg.h5')

# Define the classes
classes = ['glioma', 'meningioma', 'no tumor', 'pituitary']

# Define the path to the static folder
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Create folders for input and predicted images if they don't exist
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'input_images'), exist_ok=True)
os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], 'predicted_images'), exist_ok=True)

def preprocess_image(image):
    """Preprocess the input image for the VGG16 model"""
    img = image.resize((224, 224))
    img = np.expand_dims(img, axis=0)
    img = img / 255.0  # Normalize pixel values
    return img

def overlay_text_on_image(image_path, tumor_name, accuracy):
    """Overlay text on the image and return the path to the modified image"""
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 20)
    text = f"Tumor Type: {tumor_name}\nAccuracy: {accuracy:.2f}"
    draw.text((10, 10), text, fill=(255, 255, 255), font=font)
    modified_image_path = image_path.replace(".png", "_result.png")
    image.save(modified_image_path)
    return modified_image_path

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the uploaded image file
        file = request.files['file']
        
        # Save the uploaded image
        filename = secrets.token_hex(8) + '.png'
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'input_images', filename)
        file.save(filepath)

        # Load and preprocess the image
        img = Image.open(filepath)
        img_array = preprocess_image(img)

        # Perform inference with the model
        prediction = model.predict(img_array)
        predicted_class_idx = np.argmax(prediction)
        predicted_class = classes[predicted_class_idx]
        accuracy = prediction[0][predicted_class_idx]
     
        # Generate filenames for the input and predicted images
        # input_filename = f'input_{filename}'
        predicted_filename = f'predicted_{filename}'
        # input_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'input_images', input_filename)
        predicted_filepath = os.path.join(app.config['UPLOAD_FOLDER'], 'predicted_images', predicted_filename)

        # Save the input and predicted images
        # img.save(input_filepath)
        img.save(predicted_filepath)
        
        # Overlay text on the predicted image
        annotated_image_path = overlay_text_on_image(filepath, predicted_class, accuracy)
     
        # Return the result template with the combined PDF path
        return render_template('result.html', input_image=filepath, predicted_image=annotated_image_path, tumor_name=predicted_class, accuracy=accuracy)
    
    return render_template('index.html')

@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
