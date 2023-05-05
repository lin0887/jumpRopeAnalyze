import cv2
import manage_folder
def cut(video,data_path):
    
    #Init all file path
    file_name = video.split('.')
    image_path = data_path+'\\image\\'+file_name[0]+'\\video_frame\\'
    
    manage_folder.Check_folder(image_path)
    
    # Init image data
    cap = cv2.VideoCapture(data_path+'\\output\\'+video)
    totle_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
  
    idx = 0

    while True:
        # 將影片切割成圖片處理
        success, image = cap.read()
        if not success:
            break     
        cv2.imwrite(image_path + str(idx) + '.png', image)
       
        print('\rprocess: {}/{}'.format(idx+1,totle_frames), end = ' ')
        idx += 1

if __name__ == '__main__':
    
    data_path = '..\\2023_data'
    student_id = input('input id : ')
    
    cut(student_id+'.MOV',data_path)