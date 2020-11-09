import skvideo.io
import skvideo.datasets
import numpy as np
import argparse
import cv2
import time

def threshOneFrame(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(frame, (7, 7), 0)
    """cv2.threshold(blurred,20,255, cv2.THRESH_BINARY)"""
    #thresh = cv2.adaptiveThreshold( blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
    thresh = cv2.Canny(blurred,25,40).astype(np.uint8)
    #thresh = thresh.astype(np.uint8)
    return thresh

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to input video file")
args = vars(ap.parse_args())

video = skvideo.io.FFmpegReader(args["video"])
lapstime = time.time()
videoWriter = skvideo.io.FFmpegWriter("outputvideo"+time.ctime(lapstime)+".mp4")

for frame in video.nextFrame():
    videoWriter.writeFrame(threshOneFrame(frame))

videoWriter.close()