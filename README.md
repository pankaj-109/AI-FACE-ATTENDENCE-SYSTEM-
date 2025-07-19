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

<img width="1920" height="1080" alt="Screenshot_20250717_231432" src="https://github.com/user-attachments/assets/ddb06429-03c6-47ac-9abf-bde0e86cda21" />
<img width="1920" height="1080" alt="Screenshot_20250717_231410-1" src="https://github.com/user-attachments/assets/f9d37ba2-8304-4cb6-b704-887573593562" />
<img width="1920" height="1080" alt="Screenshot_20250717_231234" src="https://github.com/user-attachments/assets/239496aa-a266-4d9b-bd81-0b2edbe46234" />


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
