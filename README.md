# 👨‍💻 AI-Based Face Attendance System

This is a smart and secure **Face Recognition Attendance System** built using Python, OpenCV, Flask, and the Face Recognition library. It allows students to register and mark their attendance by simply scanning their face via webcam or image upload.

---

## 📌 Features

- 🧠 Real-time Face Detection & Recognition
- 📝 Student Registration with Photo Capture
- ⏰ Automatic Date-Time Attendance Logging
- 📁 Stores Attendance in CSV Files
- 🌐 Web Interface using Flask

---

## 🛠️ Technologies Used

| Technology       | Purpose                      |
|------------------|-------------------------------|
| Python           | Core programming language     |
| Flask            | Web backend framework         |
| OpenCV           | Image handling and preprocessing |
| face_recognition | Face encoding & comparison    |
| Pandas           | Data handling (CSV)           |
| HTML/CSS         | Frontend templates            |
| JavaScript       | Webcam image capture (if used)|

---

## 🖼️ Screenshots

*(You can add screenshots of your UI here)*

---

## 🧪 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/face-attendance-system.git
cd face-attendance-system

# (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Run the app
python app.py
