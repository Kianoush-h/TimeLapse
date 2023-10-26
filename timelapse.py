
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""






import cv2
import os

# Path to the folder containing the images
folder_path = '20231025_dayLight'

# Getting the list of image file names in the folder
images = [img for img in os.listdir(folder_path) if img.endswith(".jpg")]

# Sorting the images based on their names
images.sort(key=lambda x: int(x.split('.')[0]))

# Setting the frame size and frames per second for the video
frame_width, frame_height = 1280, 720
fps = 10
video_name = 'timelapse_video_20231025_dayLight.mp4'  # Change the extension to the desired format, e.g., .avi, .mkv, .mov

# Initializing the video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change to the appropriate codec for your desired format
out = cv2.VideoWriter(video_name, fourcc, fps, (frame_width, frame_height))

# Loop through the images and add them to the video
for image in images:
    image_path = os.path.join(folder_path, image)
    frame = cv2.imread(image_path)
    out.write(frame)

# Release the video writer and destroy any open CV windows
out.release()
cv2.destroyAllWindows()
print("Timelapse video has been created successfully.")




































