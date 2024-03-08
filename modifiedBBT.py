from scipy import signal
import soundfile as sf
import os

source_path = 'E:\\BaiduNetdiskDownload\\THCHS-30\\data_thchs30\\data_thchs30\\train\\'
destination_path = 'E:\\BaiduNetdiskDownload\\THCHS-30\\data_thchs30\\data_thchs30\\train_441\\'

# 获取源文件夹中的所有文件
order_files = [f for f in os.listdir(source_path) if f.endswith('.wav')]

# 遍历文件并复制到目标文件夹
for order_file in order_files:
    source_file = os.path.join(source_path, order_file)
    destination_file = os.path.join(destination_path, order_file)
    y, sr = sf.read(source_file)
    # 重新采样到44100Hz
    y_resampled = signal.resample(y, int(len(y) * 44100 / sr))

    # 保存新的音频文件
    sf.write(destination_file, y_resampled, 44100)
    # os.remove(source_file)

print("Files modified successfully!")
