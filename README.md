<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Face Recognition Attendance System</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        code {
            background-color: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 4px;
        }
        a {
            color: #1a0dab;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Face Recognition Attendance System</h1>
    <p><em>A real-time face recognition attendance system that logs attendance data into MongoDB.</em></p>
    
    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#features">Features</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#license">License</a></li>
        <li><a href="#contact">Contact</a></li>
    </ul>

    <h2 id="introduction">Introduction</h2>
    <p>This project implements a face recognition attendance system using a webcam to capture video input, verify faces with DeepFace, and log attendance information into a MongoDB database. The application features a graphical user interface built with Tkinter.</p>

    <h2 id="features">Features</h2>
    <ul>
        <li>Real-time face recognition using webcam input</li>
        <li>Verification against reference images</li>
        <li>Logging of attendance with timestamps in MongoDB</li>
        <li>Tkinter-based GUI for user interaction</li>
    </ul>

    <h2 id="installation">Installation</h2>
    <h3>Prerequisites</h3>
    <p>Ensure you have the following installed:</p>
    <ul>
        <li>Python 3.5</li>
        <li>MongoDB</li>
        <li>CMake</li>
        <li>Visual Studio (with C++ build tools)</li>
    </ul>

    <h3>Clone the Repository</h3>
    <pre><code>git clone https://github.com/yourusername/face-recognition-attendance-system.git
cd face-recognition-attendance-system</code></pre>

    <h3>Install Dependencies</h3>
    <pre><code>pip install opencv-python-headless deepface pymongo pillow</code></pre>

    <h3>Set Up MongoDB</h3>
    <p>Make sure MongoDB is installed and running on your local machine. The script assumes MongoDB is running on <code>localhost</code> with the default port <code>27017</code>.</p>

    <h3>Prepare Reference Images</h3>
    <p>Place the reference images in the project directory. Ensure the file paths in the <code>reference_images</code> dictionary within the script are correct.</p>

    <h2 id="usage">Usage</h2>
    <p>Run the following command to start the face recognition attendance system:</p>
    <pre><code>python face_recognition_attendance.py</code></pre>
    <p>This will open a GUI window with the video stream from your webcam. Use the "Scan Now" button to capture and recognize faces.</p>

    <h2 id="license">License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2 id="contact">Contact</h2>
    <p>For any questions or feedback, please reach out:</p>
    <ul>
        <li>Email: your.email@example.com</li>
        <li>GitHub: <a href="https://github.com/yourusername">yourusername</a></li>
        <li>Twitter: <a href="https://twitter.com/yourtwitterhandle">@yourtwitterhandle</a></li>
    </ul>
</body>
</html>
