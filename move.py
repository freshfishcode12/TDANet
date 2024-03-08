import os
import shutil

# 指定路径
source_path = 'E:\\BaiduNetdiskDownload\\THCHS-30\\data_thchs30\\data_thchs30\\train_441\\'
destination_path = 'E:\\DownLoad\\create-speaker-mixtures\\total\\'

# 获取源文件夹中的所有文件
order_files = [f for f in os.listdir(source_path) if f.endswith('.wav')]

# 遍历文件并复制到目标文件夹
for order_file in order_files:
    # print(order_file)
    source_file = os.path.join(source_path, order_file)
    destination_file = os.path.join(destination_path, order_file)
    shutil.copy(source_file, destination_file)
    # os.remove(source_file)

print("Files copied successfully!")