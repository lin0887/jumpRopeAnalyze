import counter
import os
import pandas as pd

def count_score(a1,a2):

    dif = []
    for i in range(len(a1)):
        dif.append(a1[i]-a2[i])
    
    df = pd.DataFrame({'Left':a1,'Right':a2,'dif':dif})
    df.to_csv('..\\data\\'+'dif.csv',index = False)

if __name__ == '__main__':

    left_times = []
    right_times = []
    files = os.listdir('..\\data\\pose_landmarks\\')

    for file in files:
        left_shoulder = counter.Body_point(file,11)
        for i in range(2):
            left_shoulder.get_amplitude()
            left_shoulder.get_wavelength()
      
        ans = left_shoulder.jump_rope_count()  
        left_times.append(ans)
        
        right_shoulder = counter.Body_point(file,12)
        for i in range(2):
            right_shoulder.get_amplitude()
            right_shoulder.get_wavelength()
            
        ans = left_shoulder.jump_rope_count()  
        right_times.append(ans)
        
        
        print(file)

    count_score(left_times,right_times)