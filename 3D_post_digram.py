import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D
import pandas as pd
import manage_folder
from matplotlib.pyplot import MultipleLocator

class post:

    def __init__(self,file):
       
       self.df = pd.read_csv('..\\data\\pose_landmarks\\'+file)
       self.totle_frames = self.df.shape[0]
       file = file.split('.')[0]
       self.save_path = '..\\data\\image\\'+ file+'\\3D_pose\\'
       manage_folder.Check_folder(self.save_path)


    def draw_one_frame(self,frame):

        x = []
        y = []
        z = []
        for i in range(0,33):
            x.append(self.df[str(i)][frame]*-1)
            y.append(self.df[str(i+33)][frame]*-1)
            z.append(self.df[str(i+66)][frame]*-1)
        
        # 製作figure
        ax = plt.axes(projection='3d')
        ax.set_xlabel('x')
        ax.set_ylabel('z')
        ax.set_zlabel('y')

        #ax.plot(x, y, z,c ='black')
        # 設定ax為散佈圖
        ax.scatter(x, z , y, c ='black')
    
        # face
        ax.plot([x[8], x[6]], [z[8],z[6]],[y[8],y[6]])
        ax.plot([x[6], x[5]], [z[6],z[5]],[y[6],y[5]])
        ax.plot([x[5], x[4]], [z[5],z[4]],[y[5],y[4]])
        ax.plot([x[4], x[0]], [z[4],z[0]],[y[4],y[0]])
        ax.plot([x[0], x[1]], [z[0],z[1]],[y[0],y[1]])
        ax.plot([x[1], x[2]], [z[1],z[2]],[y[1],y[2]])
        ax.plot([x[2], x[3]], [z[2],z[3]],[y[2],y[3]])
        ax.plot([x[3], x[7]], [z[3],z[7]],[y[3],y[7]])
        ax.plot([x[9], x[10]], [z[9],z[10]],[y[9],y[10]])

        # body
        ax.plot([x[11], x[12]], [z[11],z[12]],[y[11],y[12]])
        ax.plot([x[23], x[24]], [z[23],z[24]],[y[23],y[24]])
        ax.plot([x[11], x[23]], [z[11],z[23]],[y[11],y[23]])
        ax.plot([x[12], x[24]], [z[12],z[24]],[y[12],y[24]])

        # Right arm
        ax.plot([x[12], x[14]], [z[12],z[14]],[y[12],y[14]])
        ax.plot([x[14], x[16]], [z[14],z[16]],[y[14],y[16]])
        ax.plot([x[16], x[22]], [z[16],z[22]],[y[16],y[22]])
        ax.plot([x[16], x[18]], [z[16],z[18]],[y[16],y[18]])
        ax.plot([x[16], x[20]], [z[16],z[20]],[y[16],y[20]])
        ax.plot([x[18], x[20]], [z[18],z[20]],[y[18],y[20]])

        # Left arm
        ax.plot([x[11], x[13]], [z[11],z[13]],[y[11],y[13]])
        ax.plot([x[13], x[15]], [z[13],z[15]],[y[13],y[15]])
        ax.plot([x[15], x[21]], [z[15],z[21]],[y[15],y[21]])
        ax.plot([x[15], x[17]], [z[15],z[17]],[y[15],y[17]])
        ax.plot([x[15], x[19]], [z[15],z[19]],[y[15],y[19]])
        ax.plot([x[17], x[19]], [z[17],z[19]],[y[17],y[19]])

        # Left leg
        ax.plot([x[23], x[25]], [z[23],z[25]],[y[23],y[25]])
        ax.plot([x[25], x[27]], [z[25],z[27]],[y[25],y[27]])
        ax.plot([x[27], x[31]], [z[27],z[31]],[y[27],y[31]])
        ax.plot([x[27], x[29]], [z[27],z[29]],[y[27],y[29]])
        ax.plot([x[29], x[31]], [z[29],z[31]],[y[29],y[31]])

        # Right leg
        ax.plot([x[24], x[26]], [z[24],z[26]],[y[24],y[26]])
        ax.plot([x[26], x[28]], [z[26],z[28]],[y[26],y[28]])
        ax.plot([x[28], x[30]], [z[28],z[30]],[y[28],y[30]])
        ax.plot([x[28], x[32]], [z[28],z[32]],[y[28],y[32]])
        ax.plot([x[30], x[32]], [z[30],z[32]],[y[30],y[32]]) 

        ax.xaxis.set_major_locator(MultipleLocator(0.05))
        ax.yaxis.set_major_locator(MultipleLocator(0.1))

        plt.savefig(self.save_path+str(frame)+'.png')
        #plt.show()
        plt.clf()
        plt.close()
    

    def draw_post(self):
        
        for frame in range(self.totle_frames):
            self.draw_one_frame(frame)
            print('\rprocess: {}/{}'.format(frame,self.totle_frames), end = ' ')
        

if __name__ == '__main__':
    file = 'A1102.csv' 
    p = post(file)
    p.draw_post()