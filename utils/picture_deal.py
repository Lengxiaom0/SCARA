import cv2 
import numpy as np 
import os 


def modify_image(bounding_box, main_object,image_path="D:\2024_match\huawei\new_robo_Project\picture\231301202.jpg", save_path="D:\2024_match\huawei\new_robo_Project\save_picture\save.jpg"):
    img = cv2.imread(image_path)
    cv2.rectangle(img, (bounding_box[0], bounding_box[1]), (bounding_box[0]+bounding_box[2], bounding_box[1]+bounding_box[3]), (0, 255, 0), 2)
    cv2.rectangle(img, (main_object[0], main_object[1]), (main_object[0]+main_object[2], main_object[1]+main_object[3]), (0, 0, 255), 2)
    cv2.putText(img,str(bounding_box[4]),(bounding_box[0],bounding_box[1]),cv2.FONT_HERSHEY_DUPLEX,1,(0,255,0),2)
    cv2.putText(img,str(main_object[4]),(main_object[0],main_object[1]),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)
    cv2.imwrite(save_path,img)
    cv2.imshow("image", img)
    cv2.waitKey(5000)

def capture_frames_from_video(camera_idx, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cap=cv2.VideoCapture(camera_idx) 
    if not cap.isOpened():
        print("Error opening video stream or file")
        return
    while True:
        ret,frame=cap.read()
        if ret:
            cv2.waitKey(1) 
            cv2.imshow("Frame",frame) 
            # if cv2.waitKey(1) & 0xFF == ord('k'):
            cv2.imwrite(output_dir,frame)
            break 
        else:
            break  
