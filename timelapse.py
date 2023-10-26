
"""
@author: Kianoush 

GitHUb: https://github.com/Kianoush-h
YouTube: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA
LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/

Email: haratiank2@gmail.com

"""



import os
import imageio

# Folder containing the images
image_folder = '20231025_dayLight'

# List of images in the folder
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]  # Change the extension as required

# Sort the images based on their names to ensure proper sequence
# images = sorted(images, key=lambda x: int(os.path.splitext(x)[0]))

# Initialize the writer
video_name = 'timelapse_output.mp4'
writer = imageio.get_writer(video_name, fps=1/0.05)  # Adjust the fps as needed

# Loop through the images and add them to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    if os.path.isfile(img_path):
        writer.append_data(imageio.imread(img_path))

# Close the writer
writer.close()

print(f'Timelapse video saved as {video_name}')

























