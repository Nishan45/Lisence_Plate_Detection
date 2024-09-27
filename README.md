# Description
An automatic lisence plate detector using Yolov8 model and opencv

# Demo
Here is a <a href="https://tinyurl.com/3t5sc9yk">Video</a> of this Project.

# Packages
* `Opencv` to capture the video
* `ultralytics` to get yolov8 model
* `easyocr` is used to extract text from images

# Installation
Clone the repository
```
git clone https://github.com/Nishan45/Lisence_Plate_Detection.git
```
Install the requirements using pip
```
pip install -r requirements.txt
```

# Usage
## Add path of videos and photos to videos and images list in data.py
Befor running run.py file change the image_current_index
or video_current_index according to the size of the data 
available in videos and images

if video_current_index=0 then it will run on videos[0]
if image_current_index=0 then it will run on images[0]

cam_type=True means it will run on video accoring to the
        video_current_index given
        
cam_type=False means it will run on image accoring to the
        image_current_index given
        
* Run the run.py file within the directory


