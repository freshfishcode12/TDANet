import os
# import shutil

# # 指定路径
# source_path = 'E:\\BaiduNetdiskDownload\\speechocean\\Wav\\Channel1\\'
# destination_path = 'E:\\BaiduNetdiskDownload\\speechocean\\Wav\\s1\\'

# # 获取源文件夹中的所有文件
# files = os.listdir(source_path)

# # 遍历文件并移动到目标文件夹
# # 遍历文件并复制到目标文件夹
# for file in files:
#     source_file_path = os.path.join(source_path, file)
#     # print(source_file_path)
#     order_files = [f for f in os.listdir(source_file_path) if f.endswith('.wav')]
#     for order_file in order_files:
#         # print(order_file)
#         source_file = os.path.join(source_file_path, order_file)
#         destination_file = os.path.join(destination_path, order_file)
#         shutil.copy(source_file, destination_file)
#         # os.remove(source_file)

# print("Files copied successfully!")

# import os
# import random
# import shutil

# # 指定原始文件夹和目标文件夹路径
# source_folder = 'E:\\BaiduNetdiskDownload\\speechocean\\Wav\\s1\\'
# destination_folder = 'E:\\BaiduNetdiskDownload\\speechocean\\Wav\\s2\\'

# # 获取源文件夹中的所有.wav文件
# wav_files = [f for f in os.listdir(source_folder) if f.endswith('.wav')]

# # 随机选取一半文件
# selected_files = random.sample(wav_files, len(wav_files)//2)

# # 移动选中的文件到目标文件夹
# for file in selected_files:
#     source_file = os.path.join(source_folder, file)
#     destination_file = os.path.join(destination_folder, file)
#     shutil.move(source_file, destination_file)

# print("Files moved successfully!")

# 打开txt文件
# 打开txt文件，以读取模式打开
folder_path = 'E:\\BaiduNetdiskDownload\\deal_song\\'

# 获取文件夹下所有wav文件的文件名
wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]

second_data = [0]*20000
fourth_data = [0]*20000
with open('E:\\DownLoad\\create-speaker-mixtures\\mix_2_spk_cv.txt', 'r') as file:
    # 逐行读取文件内容
    i = 0
    for line in file:
        # 将每行数据按空格分割成列表
        data = line.split()
        if len(data) >= 4:
            # 获取第二个和第四个数据
            second_data[i] = data[1]
            fourth_data[i] = data[3]
            i = i + 1

folder_path2 = 'E:\\BaiduNetdiskDownload\\THCHS-30\\data_thchs30\\data_thchs30\\train_441\\'

# 获取文件夹下所有wav文件的文件名
wav_files2 = [f for f in os.listdir(folder_path2) if f.endswith('.wav')]

# 新建一个txt文件并写入wav文件名
with open('mix_2_spk_cv.txt', 'w') as file:
    for i in range(100):
        file.write(wav_files[300+i] + ' ' + str(second_data[i]) + ' ' + wav_files2[800+i] + ' '+ str(fourth_data[i]) + '\n')
    # for j in range(100):
    #     file.write(wav_files[j] + ' ' + str(second_data[400+j]) + ' ' + wav_files2[400+j] + ' '+ str(fourth_data[400+j]) + '\n')