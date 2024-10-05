import streamlit as st
import cv2
import numpy as np

# Title of the app
st.title("Live Camera Detection with Streamlit")

# Start the camera
camera = cv2.VideoCapture(0)

# Function to process video frames
def process_frame(frame):
    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return gray_frame

# Check if the camera is opened
if not camera.isOpened():
    st.error("Could not access the camera.")
else:
    # Stream the video
    stframe = st.empty()  # Placeholder for video frame
    while True:
        # Read a frame from the camera
        ret, frame = camera.read()
        
        # If frame is read correctly
        if not ret:
            st.error("Failed to read the camera frame.")
            break
        
        # Process the frame (for example, convert to grayscale)
        processed_frame = process_frame(frame)

        # Display the frame using Streamlit
        stframe.image(processed_frame, channels="GRAY", use_column_width=True)
        
        # Break the loop if stream is stopped manually
        if st.button("Stop"):
            break

# Release the camera when done
camera.release()
