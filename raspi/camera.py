import cv2
import pyshine as ps
address = ('100.113.29.118',9000)

def stream(): # Enter your IP address 
    StreamProps = ps.StreamProps
    StreamProps.set_Mode(StreamProps,'cv2')
    capture = cv2.VideoCapture(0)
    capture.set(cv2.CAP_PROP_BUFFERSIZE,4)
    capture.set(cv2.CAP_PROP_FRAME_WIDTH,320)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    capture.set(cv2.CAP_PROP_FPS,30)
    StreamProps.set_Capture(StreamProps,capture)
    StreamProps.set_Quality(StreamProps,90)
    server = ps.Streamer(address,StreamProps)

def captureFrame(cam):
    ret, frame = cam.read()
    return frame



