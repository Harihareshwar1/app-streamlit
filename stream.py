import av
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase

# Video processor class to handle video frame processing
class VideoProcessor(VideoProcessorBase):
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")

        # Example: Convert the image to grayscale
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Stack the single channel grayscale to 3-channel to match expected output format
        gray_img_bgr = np.stack((gray_img,) * 3, axis=-1)

        return av.VideoFrame.from_ndarray(gray_img_bgr, format="bgr24")

# Streamlit UI
st.title("Live Camera Detection with Streamlit")

# Use the webrtc_streamer to capture the video feed from the webcam via browser
webrtc_streamer(key="example", video_processor_factory=VideoProcessor)
