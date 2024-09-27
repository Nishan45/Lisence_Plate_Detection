'''
Befor running run.py file change the image_current_index
or video_current_index according to the size of the data 
available in videos and images

if video_current_index=0 then it will run on videos[0]
if image_current_index=0 then it will run on images[0]

cam_type=True means it will run on video accoring to the
        video_current_index given
        
cam_type=False means it will run on image accoring to the
        image_current_index given
        
'''
cam_type=False
image_current_index=0
video_current_index=0

data={
    "NA13NRU":["029292","Aarya Ghosh"],
    "GX15OGJ":["023839","Aashish Das"],
    "APO5JGO":["019292","Aashutosh Barman"],
    "AK64DMV":["983848","Bhuvan Pandey"],
    "KHO5ZZK":["928383","Chanchal Das"],
    "EY61NBG":["019293","Bikram Saha"],
    "BG65USJ":["039393","Debabirta Sen"],
    "LN15ZZC":["929839","Debjit Choudhury"],  
}

videos=[]

images=[
    "Number-Plates-Illegal.webp" 
]
