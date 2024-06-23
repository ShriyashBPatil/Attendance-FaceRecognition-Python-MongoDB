Face Recognition Attendance System
A real-time face recognition attendance system that logs attendance data into MongoDB.

Table of Contents
Introduction
Features
Installation
Usage
License
Contact
Introduction
This project implements a face recognition attendance system using a webcam to capture video input, verify faces with DeepFace, and log attendance information into a MongoDB database. The application features a graphical user interface built with Tkinter.

Features
Real-time face recognition using webcam input
Verification against reference images
Logging of attendance with timestamps in MongoDB
Tkinter-based GUI for user interaction
Installation
Prerequisites
Ensure you have the following installed:

Python 3.5
MongoDB
CMake
Visual Studio (with C++ build tools)
Clone the Repository
sh
Copy code
git clone https://github.com/yourusername/face-recognition-attendance-system.git
cd face-recognition-attendance-system
Install Dependencies
Install the necessary Python libraries using pip:

sh
Copy code
pip install opencv-python-headless deepface pymongo pillow
Set Up MongoDB
Make sure MongoDB is installed and running on your local machine. The script assumes MongoDB is running on localhost with the default port 27017.

Prepare Reference Images
Place the reference images in the project directory. Ensure the file paths in the reference_images dictionary within the script are correct.

Usage
Run the following command to start the face recognition attendance system:

sh
Copy code
python face_recognition_attendance.py
This will open a GUI window with the video stream from your webcam. Use the "Scan Now" button to capture and recognize faces.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or feedback, please reach out:

Email: your.email@example.com
GitHub: yourusername
Twitter: @yourtwitterhandle
