import os
from moviepy.editor import *

def to_mov(file_name,file_type):
    file_path = '.\\videos\\'
    video = VideoFileClip('.\\'+file_name+file_type) 
    video.write_videofile(file_path+file_name+'.MOV',temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac")

to_mov('part1','.mov')
print('ok')