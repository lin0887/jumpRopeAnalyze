#import talib.abstract as ta
import os
import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line,Grid
import math
import numpy as np
import manage_folder

class Body_waveform:
    
    def __init__(self,file):

        self.data = pd.read_csv('..\\data\\pose_landmarks\\'+file)
        self.frame_size = self.data.shape[0]
        self.frame = range(self.frame_size)
        self.file_name = file.split('.')[0]
        self.points_name = ['nose','left_eye_ionner','left_eye','left_eye_outer','right_eye_inner','right_eye','right_eye_outer',
        'left_ear','right_ear','left_month','right_month','left_shoulder','right_shoulder','left_elbow','right_elbow',
        'left_wrist','right_wrist','left_pinky','right_pinky','left_index','right_index','left_thumb','right_thumb',
        'left_hip','right_hip','left_knee','right_knee','left_ankle','right_ankle','left_heel','right_heel',
        'left_foot_index','right_foot_index','center',
        ]
        self.save_path = '..\\data\\image\\'+self.file_name+'\\waveform\\'
        manage_folder.Check_folder(self.save_path)


    def all_parts(self):

        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data=self.frame,
            )
            .add_yaxis(
                series_name= self.points_name[11],
                y_axis= self.data[str(11+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[12],
                y_axis= self.data[str(12+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[13],
                y_axis= self.data[str(13+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[14],
                y_axis= self.data[str(14+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[15],
                y_axis= self.data[str(15+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[16],
                y_axis= self.data[str(16+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[23],
                y_axis= self.data[str(23+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[24],
                y_axis= self.data[str(24+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            ) 
            .add_yaxis(
                series_name= self.points_name[25],
                y_axis= self.data[str(25+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[26],
                y_axis= self.data[str(26+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[27],
                y_axis= self.data[str(27+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[28],
                y_axis= self.data[str(28+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 5, 
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
            )
        )

        line.render(self.save_path+'all.html')


    def body(self):

        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data=self.frame,
            ) 
            .add_yaxis(
                series_name= self.points_name[11],
                y_axis= self.data[str(11+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[12],
                y_axis= self.data[str(12+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[23],
                y_axis= self.data[str(23+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[24],
                y_axis= self.data[str(24+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )    
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 5, 
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
            )
        )

        line.render(self.save_path+'body.html')


    def shoulder(self):
    
        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data=self.frame,
            ) 
            .add_yaxis(
                series_name= self.points_name[11],
                y_axis= self.data[str(11+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 5, 
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
                    #min_='dataMin',
                ), 
            )
            
        )

        line.render(self.save_path+'shoulder.html')
    

    def elbow(self):
       
        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data=self.frame,
            ) 
            .add_yaxis(
                series_name= self.points_name[13],
                y_axis= self.data[str(13+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[14],
                y_axis= self.data[str(14+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 5, 
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
            )
        )

        line.render(self.save_path+'elbow.html')


    def wrist(self):

        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data=self.frame,
            ) 
            .add_yaxis(
                series_name= self.points_name[15],
                y_axis= self.data[str(15+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[16],
                y_axis= self.data[str(16+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 5, 
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
            )
        )

        line.render(self.save_path+'wrist.html')


    def knee(self):

        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data=self.frame,
            ) 
            .add_yaxis(
                series_name= self.points_name[25],
                y_axis= self.data[str(25+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[26],
                y_axis= self.data[str(26+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 5, 
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
            )
        )

        line.render(self.save_path+'knee.html')
    

    def ankle(self):
        
        line=(
            Line(init_opts=opts.InitOpts(width='5000px', height='800px'))
            .add_xaxis(
                xaxis_data=self.frame,
            ) 
            .add_yaxis(
                series_name= self.points_name[27],
                y_axis= self.data[str(27+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .add_yaxis(
                series_name= self.points_name[28],
                y_axis= self.data[str(28+33)],
                symbol="emptyCircle",
                is_symbol_show= 0,
                is_smooth=0,
                label_opts=opts.LabelOpts(is_show=False),
                linestyle_opts= opts.LineStyleOpts(width=1),
            )
            .set_global_opts(
                xaxis_opts=opts.AxisOpts(
                    interval = 5, 
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
            )
        )

        line.render(self.save_path+'ankle.html')    


if __name__=="__main__":
    '''
    files = os.listdir('..\\data\\pose_landmarks\\')
    for file in files:
        all(file)
        body(file)
        shoulder(file)
        elbow(file)
        wrist(file)
        knee(file)
        ankle(file)
        print(file)
    '''
    file = 'A1102.csv'
    a = Body_waveform(file)
    a.all_parts()
    a.body()
    a.shoulder()
    a.elbow()
    a.wrist()
    a.knee()
    a.ankle()
    
    

    
