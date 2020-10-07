import cv2;

from random import randrange
# Load some pre-trained data on face frontals from opncv(haarcascade_frontalface_default)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Choose an image to detect faces in
# img = cv2.imread('RDJ.png')

# To capture video from webcam
webcam = cv2.VideoCapture(0)

# Iterate forever over frames 
while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # Draw rectangle around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, v), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 2)

    # Display the image with the faces spotted 
    cv2.imshow('Clever Programmer Face Detector', frame)

    # Wait here in the code and listen for a Key press
    key = cv2.waitKey(1)

    # stop if Q or q key is pressed
    if key == 81 or key == 113:
        break

# Release the videocapture object
webcam.release()

print("Code Completed")