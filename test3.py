import ffmpeg
import wave
import numpy as np
import os

folder_path = 'E:\\BaiduNetdiskDownload\\musdb18\\train\\'
out_path = 'E:\\BaiduNetdiskDownload\\musdb18\\wav\\train\\'
# 获取文件夹下所有wav文件的文件名
wav_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

for wav_file in wav_files:
    input_file = folder_path + wav_file
    file_name = os.path.splitext(os.path.split(input_file)[1])[0]
    # 读取MP4文件
    probe = ffmpeg.probe(input_file)

    # 获取音频流信息
    audio_streams = [stream for stream in probe['streams'] if stream['codec_type'] == 'audio']

    # 保存Stream 0和Stream 4的音频数据
    for stream in audio_streams:
        stream_index = stream['index']
        if stream_index == 0:
            output_file = out_path + file_name + '.wav'
            stream_data, _ = (
                ffmpeg
                .input(input_file)
                .output('-', format='s16le', ac=1, ar=44100)
                .run(capture_stdout=True)
            )
            
            # 将音频数据写入wav文件
            with wave.open(output_file, 'wb') as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(44100)
                wf.writeframes(np.frombuffer(stream_data, np.int16))

print("Stream 0 and Stream 4 saved as single channel wav files.")