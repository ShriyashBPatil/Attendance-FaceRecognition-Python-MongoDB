"""
=================================================================================================
|Github Repository - https://github.com/ShriyashBPatil/Attendance-FaceRecognition-Python-MongoDB |
|This repository houses an innovative attendance management system developed using Python.       |
|Leveraging the power of computer vision, DeepFace, and MongoDB, this application simplifies     |
|the attendance tracking process with just a snap!                                               |
=================================================================================================
"""
import cv2
import time
import tkinter as tk
from PIL import Image, ImageTk
from deepface import DeepFace
import pymongo
from datetime import datetime

client = pymongo.MongoClient("mongodb://localhost:27017/")
database_name = "SYCS"
database_name = "SYCS"
collection_name = "Attendence"
db = client[database_name]
collection = db[collection_name]

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
recognized_person = None 
recognition_timeout = 180  

reference_images = {
    "Shriyash": {"id": 1, "image": cv2.imread("img.jpg"),"class":"SY CS B"},
   
}

# Tkinter setup
root = tk.Tk()
root.title("Face Recognition")

# Canvas for displaying video stream
canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

# Tkinter label to display recognition result
result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack(pady=20)

def show_recognition_result(person_id, person_name):
    result_label.config(text=f"Successful Recognition!\nID: {person_id}, Person: {person_name}")
    root.after(5000, reset_recognition_result) 
    current_time = datetime.now()
    cur_time=str(current_time.time())
    current_datetime = datetime.now()
    cur_date = str(current_datetime.date())
    data={"Name":person_name, "RollNo:":person_id, "Time":cur_time, "Date":cur_date}
    result = collection.insert_one(data)

    if result.inserted_id:
      print(f"Data inserted successfully. Inserted ID: {result.inserted_id}")
    else:
     print("Failed to insert data.")
def reset_recognition_result():
    result_label.config(text="")
    global recognized_person
    recognized_person = None  

def start_next_scan():
    global recognized_person
    if recognized_person is None :
        ret, frame = cap.read()
        if ret:
            person_id, person_name = check_face(frame.copy())
            if person_name:
                recognized_person = {"id": person_id, "name": person_name}
                print(f"Recognized: ID={person_id}, Name={person_name}")
                show_recognition_result(person_id, person_name)

# Function to check face
def check_face(frame):
    try:
        for person_name, info in reference_images.items():
            result = DeepFace.verify(frame, info["image"].copy())
            if result['verified']:
                return info["id"], person_name
        return None, None
    except Exception as e:
        print(f"Error in face verification: {e}")
        return None, None

# Main loop
def main_loop():
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame.")
        root.destroy()
        return
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    imgtk = ImageTk.PhotoImage(image=img)
    canvas.imgtk = imgtk
    canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)

    key = cv2.waitKey(1)
    if key == ord("q"):
        root.destroy()
        return

    root.after(10, main_loop)  

next_scan_button = tk.Button(root, text="Scan Now", command=start_next_scan)
next_scan_button.pack(pady=10)
root.after(10, main_loop)
root.mainloop()
cv2.destroyAllWindows()
cap.release()
