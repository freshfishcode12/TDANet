from pydub import AudioSegment
import os

# 将指定路径下的MP3双通道文件转换为wav单通道文件

# 指定目录路径
directory = 'E:\\BaiduNetdiskDownload\\ChineseSong'

# 遍历指定目录下的所有文件
i = 0
for filename in os.listdir(directory):
    if filename.endswith(".mp3"):
        i = i + 1
        # 加载MP3文件
        sound = AudioSegment.from_file(os.path.join(directory, filename), format="mp3")

        # 将双通道转换为单通道
        sound = sound.set_channels(1)

        # 生成WAV文件名
        wav_filename = 'E:\\BaiduNetdiskDownload\\r_chinese\\c' + str(i) + ".wav"
        
        # 保存为WAV文件
        sound.export(os.path.join(directory, wav_filename), format="wav")

        print(f"Converted {filename} to {wav_filename}")