import cv2
from ultralytics import YOLO
import data



from util import read_license_plate

model=YOLO("best.pt")


video=data.videos[data.video_current_index]
image=data.images[data.image_current_index]

cam_video=data.cam_type


 
if cam_video:
    cam=cv2.VideoCapture(video)
    
    while True:
        open,img=cam.read()
        img=cv2.resize(img,(1400,800))
        
        result=model(img)
        
        for results in result:
            for r in results.boxes.data.tolist():
                
                x1,y1,x2,y2,score,classid=r
                
                
            
                x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
                gray=img[y1:y2,x1:x2,:]
                gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
                
                _, gray = cv2.threshold(gray, 64, 255, cv2.THRESH_BINARY_INV)
                text ,score=read_license_plate(gray)
                text_size,_=cv2.getTextSize(text,1,2,2)
                text_w,text_h=text_size
                
                x1_cen=int((x2+x1)/2)
                
                if(text_w>2):
                    name="UNREGISTERED "
                    color=(0,0,255)
                    color2=(0,0,255)
                    yred=3
                    id=""
                    
                    if text in data.data:
                        name="Name:"+data.data[text][1]
                        id="Lisence:"+data.data[text][0]
                        color=(0,255,0)
                        color2=(0,0,0)
                        yred=4
                        
                    
                    cv2.rectangle(img,(int(x1_cen-len(name)*6),y1-int(5*text_h)),(int(x1_cen+len(name)*6+2),y1-int(2*text_h)),(255,255,255),-1)
                    cv2.putText(img, text=name, org=(int(x1_cen-len(name)*6)+25,y1-int(yred*text_h)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=color2, thickness=1, lineType=cv2.LINE_AA)
                    if id!="":
                        cv2.putText(img, text=id, org=(int(x1_cen-len(name)*6)+25,y1-int((yred-1)*text_h)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=color2, thickness=1, lineType=cv2.LINE_AA)
                    
                    cv2.rectangle(img,(int(x1_cen-len(name)*6),y1-int(5*text_h)),(int(x1_cen+len(name)*6+2),y1-int(2*text_h)),color,2)

                        
                    cv2.rectangle(img,(int(x1_cen-text_w/2-2),y1-2*text_h),(int(x1_cen+text_w/2+2),y1),(255,255,255),-1)
                
                    cv2.putText(img, text=text, org=(int(x1_cen-text_w/2),y1-int(text_h/2)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2, lineType=cv2.LINE_AA)
                    cv2.rectangle(img,(int(x1_cen-text_w/2-2),y1-2*text_h),(int(x1_cen+text_w/2+2),y1),(0,255,0),2)
                
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

        
        cv2.imshow('img',img)
        
        if cv2.waitKey(1) & 0xff==ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

else:
    img=cv2.imread(image)
    img=cv2.resize(img,(1400,800))
    result=model(img)
    
    for results in result:
        for r in results.boxes.data.tolist():
            
            x1,y1,x2,y2,score,classid=r
            
        
            x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
            gray=img[y1:y2,x1:x2,:]
            gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
            
            _, gray = cv2.threshold(gray, 64, 255, cv2.THRESH_BINARY_INV)
            text ,score=read_license_plate(gray)
            text_size,_=cv2.getTextSize(text,1,2,2)
            text_w,text_h=text_size
            
            x1_cen=int((x2+x1)/2)
            
            if(text_w>2):
                name="UNREGISTERED "
                color=(0,0,255)
                color2=(0,0,255)
                yred=3
                id=""
                
                if text in data.data:
                    name="Name:"+data.data[text][1]
                    id="Lisence:"+data.data[text][0]
                    color=(0,255,0)
                    color2=(0,0,0)
                    yred=4
                    
                
                cv2.rectangle(img,(int(x1_cen-len(name)*6),y1-int(5*text_h)),(int(x1_cen+len(name)*6+2),y1-int(2*text_h)),(255,255,255),-1)
                cv2.putText(img, text=name, org=(int(x1_cen-len(name)*6)+25,y1-int(yred*text_h)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=color2, thickness=1, lineType=cv2.LINE_AA)
                if id!="":
                    cv2.putText(img, text=id, org=(int(x1_cen-len(name)*6)+25,y1-int((yred-1)*text_h)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=color2, thickness=1, lineType=cv2.LINE_AA)
                
                cv2.rectangle(img,(int(x1_cen-len(name)*6),y1-int(5*text_h)),(int(x1_cen+len(name)*6+2),y1-int(2*text_h)),color,2)

                    
                cv2.rectangle(img,(int(x1_cen-text_w/2-2),y1-2*text_h),(int(x1_cen+text_w/2+2),y1),(255,255,255),-1)
            
                cv2.putText(img, text=text, org=(int(x1_cen-text_w/2),y1-int(text_h/2)), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0), thickness=2, lineType=cv2.LINE_AA)
                cv2.rectangle(img,(int(x1_cen-text_w/2-2),y1-2*text_h),(int(x1_cen+text_w/2+2),y1),(0,255,0),2)
            
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)

    while True:
        
        cv2.imshow('img',img)
        if cv2.waitKey(1) & 0xff==ord('q'):
            break
        
        

    
