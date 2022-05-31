from fileinput import filename
import os 
from moviepy.editor import *
from os import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from notifypy import Notify




var_path=str(input("Enter the path of the video : "))

l=os.listdir(var_path)
VIDEO_LIST=[]


for i in l:
    if i.endswith('.mp4') or i.endswith(".MP4"):
        VIDEO_LIST.append(i)


for i in VIDEO_LIST:
    filename=i

    clip = VideoFileClip(i)

    
    clip = clip.subclip(0,-4)

    
    clip.write_videofile(i+"new.mp4")
    

notification = Notify()
notification.title = "FILIREMOVE"
notification.message = "The processing of your videos is complete."
notification.send()



