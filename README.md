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
<img width="1920" height="1080" alt="Screenshot_20250717_231234" src="https://github.com/user-attachments/assets/fc089fa4-6db2-4f73-b00b-d87644cdcfea" />
<img width="1920" height="1080" alt="Screenshot_20250717_231410-1" src="https://github.com/user-attachments/assets/c7f77ad7-c3aa-4c82-8066-368ee9d525ed" />
<img width="1920" height="1080" alt="Screenshot_20250717_231432" src="https://github.com/user-attachments/assets/d9c9e15f-00d1-47b7-ad79-d3aaf12afeb1" />


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
