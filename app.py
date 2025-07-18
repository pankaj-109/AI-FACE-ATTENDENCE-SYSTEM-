from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import cv2
import numpy as np
import face_recognition
import pandas as pd
from datetime import datetime
import base64

app = Flask(__name__)

STUDENT_CSV = "students.csv"
ATTENDANCE_CSV = "attendance_log.csv"
KNOWN_FACES_DIR = "known_faces"
os.makedirs(KNOWN_FACES_DIR, exist_ok=True)

# Load student database
def load_students():
    if os.path.exists(STUDENT_CSV):
        df = pd.read_csv(STUDENT_CSV)
        df.columns = df.columns.str.strip().str.lower()
        return df
    else:
        return pd.DataFrame(columns=["name", "roll", "branch", "age", "address", "contact"])

# Load known encodings
def load_known_faces():
    known_encodings = []
    known_names = []
    for file in os.listdir(KNOWN_FACES_DIR):
        path = os.path.join(KNOWN_FACES_DIR, file)
        img = face_recognition.load_image_file(path)
        enc = face_recognition.face_encodings(img)
        if enc:
            known_encodings.append(enc[0])
            known_names.append(os.path.splitext(file)[0])
    return known_encodings, known_names

# Save attendance
def mark_attendance(name):
    students = load_students()
    now = datetime.now()
    row = students[students['name'] == name]
    if not row.empty:
        data = {
            'date': now.strftime('%Y-%m-%d'),
            'time': now.strftime('%H:%M:%S'),
            'name': name,
            'roll': row['roll'].values[0],
            'branch': row['branch'].values[0],
            'age': row['age'].values[0],
            'address': row['address'].values[0],
            'contact': row['contact'].values[0],
        }
        if not os.path.exists(ATTENDANCE_CSV):
            pd.DataFrame([data]).to_csv(ATTENDANCE_CSV, index=False)
        else:
            pd.DataFrame([data]).to_csv(ATTENDANCE_CSV, mode='a', header=False, index=False)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        branch = request.form['branch']
        age = request.form['age']
        address = request.form['address']
        contact = request.form['contact']
        img_data = request.form['image'].split(',')[1]

        img_bytes = base64.b64decode(img_data)
        with open(f"{KNOWN_FACES_DIR}/{name}.jpg", 'wb') as f:
            f.write(img_bytes)

        df = load_students()
        new_row = pd.DataFrame([[name, roll, branch, age, address, contact]],
                               columns=["name", "roll", "branch", "age", "address", "contact"])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(STUDENT_CSV, index=False)
        return redirect(url_for('home'))
    return render_template("register.html")

@app.route('/attendance')
def attendance():
    return render_template("attendance.html")

@app.route('/detect_face', methods=['POST'])
def detect_face():
    data = request.get_json()
    img_data = data['image'].split(',')[1]
    img_bytes = base64.b64decode(img_data)
    np_img = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb)
    known_encodings, known_names = load_known_faces()

    for encoding in encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)
        face_distances = face_recognition.face_distance(known_encodings, encoding)
        if matches and any(matches):
            best_match = np.argmin(face_distances)
            name = known_names[best_match]
            mark_attendance(name)
            return jsonify({"name": name})
    return jsonify({"name": "Unknown"})

if __name__ == '__main__':
    app.run(debug=True)
