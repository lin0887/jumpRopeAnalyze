import cv2
import mediapipe as mp
import pandas as pd
import manage_folder 
import numpy as np
import os
import logging
def dection(video,data_path):
    
    #Init all file path
    input_path = data_path+'\\input\\'+video
    output_path = data_path+'\\output\\'+video
    file_name = video.split('.')
    image_path = data_path+'\\image\\'+file_name[0]+'\\video_frame\\'
    pose_landmark_path = data_path+'\\pose_landmarks\\'+file_name[0]+'.csv'

    manage_folder.Check_folder(data_path+'\\output\\')
    manage_folder.Check_folder(data_path+'\\pose_landmarks\\')
    manage_folder.Check_folder(image_path)
    
    # Init image data
    BG_COLOR = (192, 192, 192) # gray
    cap = cv2.VideoCapture(input_path)
    totle_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    out_video = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
     
    
    # Initialize mediapipe drawing class - to draw the landmarks points.
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_pose = mp.solutions.pose 
    
    # Define output csv dataframe
    pose_landmark_data = []
    
    idx = 0

    # 設定模型參數
    with mp_pose.Pose(static_image_mode=False, model_complexity=2, enable_segmentation=True, min_detection_confidence=0.5) as pose:
        while True:
            # 將影片切割成圖片處理
            success, image = cap.read()
            
            if not success:
                break
        
            # 呼叫姿勢追蹤API
            # 在處理之前將 BGR 圖像轉換為 RGB
            results = pose.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
            annotated_image = image.copy()
            
            '''
            # 去除背景
            condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
            bg_image = np.zeros(image.shape, dtype=np.uint8)
            bg_image[:] = BG_COLOR
            annotated_image = np.where(condition, annotated_image, bg_image)
            '''
            
           
            if results.pose_landmarks is not None:
                
                # 將關節畫在圖片上面
                mp_drawing.draw_landmarks(
                        image = annotated_image,
                        landmark_list = results.pose_landmarks,
                        connections = mp_pose.POSE_CONNECTIONS,
                        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style()
                        )   
                
                # make pose landmark data
                x = []
                y = []
                z = []
                visibility = []
                for i in mp_pose.PoseLandmark:
                    x.append (results.pose_landmarks.landmark[i].x)
                    y.append (results.pose_landmarks.landmark[i].y)
                    z.append (results.pose_landmarks.landmark[i].z)
                    visibility.append(results.pose_landmarks.landmark[i].visibility)
                pose_landmark_data.append(x + y + z + visibility)
                
            else :
                if len(pose_landmark_data) != 0 :
                    pose_landmark_data.append(pose_landmark_data[-1])
                    
            #cv2.imwrite(image_path + str(idx) + '.png', annotated_image)
            out_video.write(annotated_image)
            
            
            '''
            顯示圖片
            cv2.imshow('image',annotated_image)
            cv2.waitKey(30)
            '''
            
            
            print('\rprocess: {}/{}'.format(idx+1,totle_frames), end = ' ')
            idx += 1
            
        out_video.release()
        df = pd.DataFrame(pose_landmark_data)
        df.to_csv(pose_landmark_path,index = False)
  
    
if __name__ == '__main__':
    
    
    data_path = '..\\2023_data'

    videos = os.listdir(data_path+'\\input\\')
    logging.basicConfig(filename='..\\2023_data\\dectionError.log', level=logging.ERROR)
    
    flag = False
    
    for video in videos:
        if video =='12077.MOV':
             flag = True
        print(video)
        if flag == True:
            try: 
                    dection(video,data_path)
            except :
                    logging.error(str(video)+' have error ')
    
    
    #dection('12025.MOV','..\\2023_data\\')

