import wave
import numpy as np
import os

# 将指定路径下的wav文件截取前15s数据，然后保存

# 打开wav文件
input_file = 'E:\\BaiduNetdiskDownload\\r_chinese\\'
wav_files = [f for f in os.listdir(input_file) if f.endswith('.wav')]

for wave_file in wav_files:
    wave_file_path = input_file + wave_file
    with wave.open(wave_file_path, 'rb') as wf:
        # 获取wav文件的参数
        params = wf.getparams()
        num_frames = wf.getnframes()
        sample_rate = wf.getframerate()
        
        # 读取音频数据
        audio_data = np.frombuffer(wf.readframes(num_frames), dtype=np.int16)
        
        # 去除前15秒钟的数据
        num_frames_to_keep = int(sample_rate * 15)
        audio_data_cut = audio_data[num_frames_to_keep:]
        output_file = 'c' + wave_file 
        # 写入新的wav文件
        with wave.open(output_file, 'wb') as wf_out:
            wf_out.setparams(params)
            wf_out.writeframes(audio_data_cut.tobytes())

    print(f'{input_file} processed, removed first 10 seconds, and saved as {output_file}')