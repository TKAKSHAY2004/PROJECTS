from flask import Flask, request, jsonify
import openai
import pytesseract
import cv2
import face_recognition
from PIL import Image
import base64
import io

app = Flask(__name__)

openai.api_key = "your_openai_api_key"

def extract_text_from_image(image_data):
    image = Image.open(io.BytesIO(base64.b64decode(image_data)))
    text = pytesseract.image_to_string(image)
    return text

def verify_face(image1_data, image2_data):
    image1 = face_recognition.load_image_file(io.BytesIO(base64.b64decode(image1_data)))
    image2 = face_recognition.load_image_file(io.BytesIO(base64.b64decode(image2_data)))

    encoding1 = face_recognition.face_encodings(image1)[0]
    encoding2 = face_recognition.face_encodings(image2)[0]

    results = face_recognition.compare_faces([encoding1], encoding2)
    return results[0]

@app.route('/process_document', methods=['POST'])
def process_document():
    image_data = request.json.get('image_data')
    extracted_text = extract_text_from_image(image_data)
    return jsonify({"extracted_text": extracted_text})

@app.route('/verify_face', methods=['POST'])
def verify_face_route():
    image1_data = request.json.get('image1')
    image2_data = request.json.get('image2')
    verification_result = verify_face(image1_data, image2_data)
    return jsonify({"verification_result": verification_result})

@app.route('/conversation', methods=['POST'])
def conversation():
    user_message = request.json.get('message')

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful AI Branch Manager assisting users with loan applications."},
            {"role": "user", "content": user_message}
        ]
    )

    response_text = response['choices'][0]['message']['content']
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
