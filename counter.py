import os
import pandas as pd
import pyecharts.options as opts
import matplotlib.pyplot as plt
from pyecharts.charts import Line,Bar
import numpy as np
import manage_folder
import statistics

class Body_point:

    def __init__(self,file,point):

        points_name = ['nose','left_eye_ionner','left_eye','left_eye_outer','right_eye_inner','right_eye','right_eye_outer',
        'left_ear','right_ear','left_month','right_month','left_shoulder','right_shoulder','left_elbow','right_elbow',
        'left_wrist','right_wrist','left_pinky','right_pinky','left_index','right_index','left_thumb','right_thumb',
        'left_hip','right_hip','left_knee','right_knee','left_ankle','right_ankle','left_heel','right_heel',
        'left_foot_index','right_foot_index','center',
        ]

        pose_data = pd.read_csv('..\\data\\pose_landmarks\\'+file)
        self.data = pose_data[str(point+33)]
        self.frame_num = len(self.data)
        self.frame = range(self.frame_num)
        self.file_name = file.split('.')[0]
        self.var = 2.5
        self.body_part = points_name[point]
        self.save_path = '..\\data\\image\\'+self.file_name+'\\'+self.body_part+'\\'
        manage_folder.Check_folder(self.save_path)
        self.average_wavelength = 0

    def get_amplitude(self):
        
        self.L_maximum = []
        self.R_maximum = []
        self.minimum = []
        self.amplitude = []
        self.wavelength = []
        self.dobule_amplitude = []
        
        # 找出所有區間極值，並過濾偽區間極值
        max_tmp = []
        min_tmp = []
        for i in range(1,self.frame_num-1):
            if self.data[i-1] < self.data[i] and self.data[i+1]< self.data[i]:
                
                left = i - int(( self.average_wavelength / 2 ) )
                right = i + int(( self.average_wavelength / 2 ) )
                
                if 0 > left :
                    left = 0
                if right > self.frame_num :
                    right = self.frame_num   
                if self.average_wavelength == 0 :
                    right =  i+1
                
                if self.data[i] == np.max(self.data[left:right]):
                    max_tmp.append(i)
                    
            elif self.data[i-1]>self.data[i] and self.data[i+1]>self.data[i]:
                
                left = i - int(( self.average_wavelength * 0.3) )
                right = i + int(( self.average_wavelength *0.3 ) )
                
                if 0 > left :
                    left = 0
                if right > self.frame_num :
                    right = self.frame_num   
                if self.average_wavelength == 0 :
                    right =  i+1    
                
                if self.data[i] == np.min(self.data[left:right]) :
                    min_tmp.append(i)
                
        #print(len(min_tmp))
        # 找出所有的波、振幅、波長  
        i = 0
        j = 0
        k = 1
        minsize = len(min_tmp)
        maxsize = len(max_tmp)
        while i != minsize and j+k != maxsize:
            if  max_tmp[j] < min_tmp[i] < max_tmp[j+k] :           
                self.minimum.append(min_tmp[i])
                self.L_maximum.append(max_tmp[j])
                self.R_maximum.append(max_tmp[j+k])
                self.amplitude.append(np.min( [self.data[max_tmp[j]]-self.data[min_tmp[i]],
                                            self.data[max_tmp[j+k]]-self.data[min_tmp[i]] ]))
                self.dobule_amplitude.append(self.data[max_tmp[j]]-self.data[min_tmp[i]]+
                                self.data[max_tmp[j+k]]-self.data[min_tmp[i]] )
                self.wavelength.append(max_tmp[j+k]-max_tmp[j]+1)
                i += 1
                j += k                      
            elif max_tmp[j] > min_tmp[i]:
                i += 1
            else:
                j += 1     

        #print(len(self.amplitude))
        # 正規化振幅，並分段
        self.normalization_amplitude = self.amplitude/np.linalg.norm(self.amplitude)
        self.section_normalization_amplitude = []
        tmp2 = []
        for i in self.normalization_amplitude:
            if i > 0.05:
                num = round(i+0.025, 3)
                if num - round(num,1) < 0.05:
                    num = round(num,1)
                else:
                    num = round(num,1) + 0.5
                self.section_normalization_amplitude.append(num)
                tmp2.append(num)
            else:
                self.section_normalization_amplitude.append(0)
       
        #　取振幅眾數
        self.mode_amplitude = statistics.mode(tmp2)

        # 取振幅眾數平均數
        tmp = []
        for i in range(len(self.section_normalization_amplitude)):
            if self.section_normalization_amplitude[i] == self.mode_amplitude:
                tmp.append(self.amplitude[i])
        self.average_amplitude = np.mean(tmp)

        # 取振幅標準差
        self.std_amplitude = np.std(tmp, ddof=1)
        
        # 取振幅區間
        self.amplitude_upper_bound = self.average_amplitude + self.std_amplitude * self.var
        self.amplitude_lower_bound = self.average_amplitude - self.std_amplitude * self.var
        
        
       
    def get_wavelength(self):

        # 取波長平均數
        tmp = []
        for idx in range(len(self.section_normalization_amplitude)):
            if self.section_normalization_amplitude[idx] == self.mode_amplitude:
                tmp.append(self.wavelength[idx])      
        self.average_wavelength = int( np.mean(tmp) + 0.5 )
        
        # 取波長區間
        self.wavelength_upper_bound = int(self.average_wavelength  * 1.5 + 0.5 )
        self.wavelength_lower_bound = int(self.average_wavelength  * 0.5 + 0.5 ) 
        #print(self.wavelength_upper_bound,self.wavelength_lower_bound,int(self.average_wavelength))

    def jump_rope_count(self):

        times = 0
        self.flag = []
        for i in range(len(self.minimum)):
            if self.dobule_amplitude[i] >= self.average_amplitude * 0.7 :
                if self.wavelength_lower_bound <= self.wavelength[i] <= self.wavelength_upper_bound:
                    self.flag.append(2)
                    times += 1
                else:
                    self.flag.append(1)
            else :
                self.flag.append(0)
       
        df = pd.DataFrame({'maxL':self.L_maximum,'min':self.minimum,'maxR':self.R_maximum,
                           'amplitude':self.amplitude,'wavelength':self.wavelength,'flag':self.flag})
        
        df.to_csv(self.save_path+'flag.csv',index=False)

        info = ['amplitude','wavelength']
        num = [self.average_amplitude,self.average_wavelength]
        df =  pd.DataFrame([info,num])
        df.to_csv(self.save_path+'info.csv',index=False)
        
        return times
                

    def amplitude_waveform(self):
        
        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data= self.frame,
            ) 
            .add_yaxis(
                series_name= 'amplitude',
                y_axis= self.amplitude,
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 1, 
                    is_show = True,
                    splitline_opts=opts.SplitLineOpts(  #顯示x軸線
                        is_show=True
                    ),
                    axislabel_opts=opts.LabelOpts(      #x軸文字設定
                        color='red',
                        font_size=10,
                        rotate = 60                    #旋轉角度90~-90
                    )
                ), 
                yaxis_opts=opts.AxisOpts(
                    #min_=0.005
                ), 
            )
        )
        line.render(self.save_path+'amplitude.html')
      
    
    def normalize_amplitude_waveform(self):

        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data= self.frame,
            ) 
            .add_yaxis(
                series_name= 'amplitude',
                y_axis= self.normalization_amplitude,
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 1, 
                    is_show = True,
                    splitline_opts=opts.SplitLineOpts(  #顯示x軸線
                        is_show=True
                    ),
                    axislabel_opts=opts.LabelOpts(      #x軸文字設定
                        color='red',
                        font_size=10,
                        rotate = 60                    #旋轉角度90~-90
                    )
                ), 
                yaxis_opts=opts.AxisOpts(
                    #min_=0.005
                ), 
            )
        )

        line.render(self.save_path+'normalization_amplitude.html')
        

    def section_normalize_amplitude_waveform(self):

        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data= self.frame,
            ) 
            .add_yaxis(
                series_name= 'amplitude',
                y_axis= self.section_normalization_amplitude,
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 1, 
                    is_show = True,
                    splitline_opts=opts.SplitLineOpts(  #顯示x軸線
                        is_show=True
                    ),
                    axislabel_opts=opts.LabelOpts(      #x軸文字設定
                        color='red',
                        font_size=10,
                        rotate = 60                    #旋轉角度90~-90
                    )
                ), 
                yaxis_opts=opts.AxisOpts(
                    #min_=0.005
                ), 
            )
        )
        
        line.render(self.save_path+'section_normalization_amplitude.html')


    def average_amplitude_waveform(self):
        
        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data= self.frame,
            ) 
            .add_yaxis(
                series_name= 'amplitude',
                y_axis= self.amplitude,
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            
            )
            .add_yaxis(
                series_name= 'average_amplitude',
                y_axis= [ self.average_amplitude for i in range(len(self.amplitude))],
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            
            )
            .add_yaxis(
                series_name= 'upper bound',
                y_axis= [ self.amplitude_upper_bound for i in range(len(self.amplitude))],
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            
            )
            .add_yaxis(
                series_name= 'lower bound',
                y_axis= [ self.amplitude_lower_bound for i in range(len(self.amplitude))],
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 1, 
                    is_show = True,
                    splitline_opts=opts.SplitLineOpts(  #顯示x軸線
                        is_show=True
                    ),
                    axislabel_opts=opts.LabelOpts(      #x軸文字設定
                        color='red',
                        font_size=10,
                        rotate = 60                    #旋轉角度90~-90
                    )
                ), 
                yaxis_opts=opts.AxisOpts(
                    #min_=0.005
                ), 
            )
        )
        
        line.render(self.save_path+'average_amplitude.html')
    

    def body_parts_waveform(self):

        maximum = [None]*self.frame_num
        f0 = [None]*self.frame_num
        f1 = [None]*self.frame_num
        f2 = [None]*self.frame_num
        
        for i in range(len(self.L_maximum)):
            maximum[self.L_maximum[i]] = self.data[self.L_maximum[i]]
        for i in range(len(self.R_maximum)):
            maximum[self.R_maximum[i]] = self.data[self.R_maximum[i]]
        for i in range(len(self.minimum)):
            if self.flag[i] == 2:
                f2[self.minimum[i]] = self.data[self.minimum[i]]
            elif self.flag[i] == 0:
                f0[self.minimum[i]] = self.data[self.minimum[i]]
            else:
                f1[self.minimum[i]] = self.data[self.minimum[i]]
              
        minimam = min(self.data)
        minimam = round(minimam-0.025, 2)
        line=(
            Line(init_opts=opts.InitOpts(width='10000px', height='800px'))
            .add_xaxis(
                xaxis_data=self.frame,
            ) 
            .add_yaxis(
                series_name= self.body_part,
                y_axis= self.data,
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
                color = '#007FFF'
            )
            .add_yaxis(
                series_name= 'maximum',
                y_axis= maximum,
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=0),
                color = '#F28500'
            )
            .add_yaxis(
                series_name= 'amplitude',
                y_axis= f0,
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=0),
                color = '#008000'
            )
            .add_yaxis(
                series_name= 'wavelength',
                y_axis= f1,
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=0),
                color = '#FF00FF'
            )
            .add_yaxis(
                series_name= 'count',
                y_axis= f2,
                symbol="emptyCircle",
                is_symbol_show= 1,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=0),
                color = '#FF0000'
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 2, 
                    is_show = True,
                    splitline_opts=opts.SplitLineOpts(  #顯示x軸線
                        is_show=True
                    ),
                axislabel_opts=opts.LabelOpts(      #x軸文字設定
                        color='red',
                        font_size=10,
                        rotate = 60,                    #旋轉角度90~-90
                    
                    )
                ), 
                yaxis_opts=opts.AxisOpts(
                    min_=minimam,
                ), 
            )
            
        )

        line.render(self.save_path+self.body_part+'.html')
        line.render('..\\data\\shoulder_waveform\\'+self.file_name+'.html')
    

def count_score(mycount):

    df = pd.read_csv('..\\data\\all.csv')
    a = []
    for i in range(df.shape[0]):
        if df['score'][i] == 'X':
            a.append(mycount[i])
        else:
            a.append(mycount[i]-int(df['score'][i]))
    df['count'] = mycount    
    df['dif'] = a
    
    df.to_csv('..\\data\\'+'my_count.csv',index = False)


if __name__=="__main__":

    #'''
    times = []
    files = os.listdir('..\\data\\pose_landmarks\\')
    for file in files:
        a = Body_point(file,11)
        for i in range(2):
            a.get_amplitude()
            a.get_wavelength()

        ans = a.jump_rope_count()  
        times.append(ans)  
        
        #a.amplitude_waveform()
        #a.normalize_amplitude_waveform()
        #a.section_normalize_amplitude_waveform()
        #a.average_amplitude_waveform()
        a.body_parts_waveform()
        
        print(file)

    count_score(times)

    '''
    
    a = Body_point('A1103.csv',11)
    for i in range(2):
        a.get_amplitude()
        a.get_wavelength()
    ans = a.jump_rope_count()  
    
    #a.amplitude_waveform()
    #a.normalize_amplitude_waveform()
    #a.average_amplitude_waveform()
    #a.section_normalize_amplitude_waveform()
    a.body_parts_waveform()
    #print('times = {}'.format(ans))
    
    #'''
    
    
    

   
    