from utils.vit import ImageMainObjectDetectionDemo
from utils.picture_deal import modify_image,capture_frames_from_video
from utils.label_vit import label_image 
from utils.speak_model import speak 
from utils.Key_word_choose import extract_keywords
from utils.sound import asr_updata,record 
from utils.post_pro import post_pro
from utils.tx import Serial_Rx,Serial_Tx
import time 
import cv2 


vit_model=ImageMainObjectDetectionDemo()

word_file=r"D:\2024_match\huawei\new_robo_Project\txt\identifed_cur.txt"
image_path=r"D:\2024_match\huawei\new_robo_Project\picture\231301202.jpg"
image_save_path=r"D:\2024_match\huawei\new_robo_Project\save_picture\save.jpg"
image_save_path2=r"D:\2024_match\huawei\new_robo_Project\save_picture\save2.jpg"
image_save_path3=r"D:\2024_match\huawei\new_robo_Project\save_picture\save3.jpg"
model_speak_audio_path=r"D:\2024_match\huawei\new_robo_Project\audio\model_speak_audio_path.mp3"
user_speak_wav_path=r"D:\2024_match\huawei\new_robo_Project\audio\user_speak_wav_path.wav"

rx=[]
# if __name__ == '__main__':
while 1:    
    rx=Serial_Rx()
    if rx:
        if rx[0]==2:

            print("rx[0]:",rx[0])
            capture_frames_from_video(0,image_path)
            bounding_box,main_object_box= vit_model.main(image_path)
            bounding_box2,main_object_box2,first_center,second_center= label_image(image_path)
            print("bounding_box1:",bounding_box2)
            print("bounding_box2:",main_object_box2)
            category_list=[bounding_box2[5],main_object_box2[5]]
            modify_image(bounding_box,main_object_box,image_path,image_save_path)
            modify_image(bounding_box2,main_object_box2,image_path,image_save_path2)
            speak(word_file,model_speak_audio_path)
            time.sleep(1)
            record(user_speak_wav_path)
            user_spoken_words=asr_updata(user_speak_wav_path)
            Key_words=extract_keywords(user_spoken_words)
            bound_center,Target_postion=post_pro(category_list,Key_words,bounding_box2,main_object_box2)
            print("category_list:",category_list)
            Serial_Tx(1,int(bound_center[0]),int(bound_center[1]),1)
            time.sleep(1)
            img=cv2.imread(image_save_path2)
            cv2.circle(img, (int(bound_center[0]), int(bound_center[1])), 10, (0, 0, 255), -1)
            cv2.putText(img, "bound", (int(bound_center[0]), int(bound_center[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            cv2.circle(img, (int(Target_postion[0]), int(Target_postion[1])), 10, (0, 255, 0), -1)
            cv2.putText(img, "postion", (int(Target_postion[0]), int(Target_postion[1])), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2)
            cv2.imwrite(image_save_path3,img)
            cv2.imshow("img",img)
            cv2.waitKey(10000)
    Serial_Tx(0,0,0,0)
    # else:
    #         ret1,frame=cv2.VideoCapture(0).read()
    #         cv2.imshow("video",frame)
    #         cv2.waitKey(1)
