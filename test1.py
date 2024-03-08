import torch
import wave
import numpy as np
import look2hear.models

import torch
import torchaudio
import wave

def vec2wav(pcm_vec, wav_file, framerate=44100):
    if np.max(np.abs(pcm_vec)) > 1.0:
        pcm_vec = pcm_vec / np.max(np.abs(pcm_vec))  # 将数据范围归一化到[-1, 1]
    pcm_vec = (pcm_vec * 32767).astype(np.int16)  # 缩放数据到[-32767, 32767]

    wave_out = wave.open(wav_file, 'wb')
    wave_out.setnchannels(1)
    wave_out.setsampwidth(2)
    wave_out.setframerate(framerate)
    wave_out.writeframes(pcm_vec.tobytes())
    wave_out.close()

krag = {'sample_rate': 8000, 'enc_kernel_size': 4, 'in_channels': 512, 'num_blocks': 16, 'num_sources': 2, 'out_channels': 128, 'upsampling_depth': 5}
model = look2hear.models.BaseModel.from_pretrain("Experiments\\checkpoint\\TDANet\\best_model.pth",**krag)
model.to('cpu')
torch.cuda.empty_cache()

input_file = 'test1.wav'
waveform, sample_rate = torchaudio.load(input_file)

tensor_data = torch.tensor(waveform)
tensor_data = tensor_data.reshape(1, 1, -1)

with torch.no_grad():
    out = model(tensor_data)

selected_data = out[:, 1, :]
data_np = selected_data.detach().cpu().numpy()
vec2wav(data_np, 'output.wav',sample_rate)

selected_data1 = out[:, 0, :]
data_np1 = selected_data1.detach().cpu().numpy()
vec2wav(data_np1,'output1.wav',sample_rate)

# # Reshape the numpy array
# data_np = data_np.reshape(-1)

# # Scale the data to the range of int16
# data_scaled = np.int16(data_np * 32767)

# # Create a new WAV file
# output_file = 'output.wav'
# with wave.open(output_file, 'wb') as wav:
#     wav.setparams((1, 2, 48000, 0, 'NONE', 'not compressed'))

#     # Write the data to the WAV file
#     wav.writeframes(data_scaled.tobytes())

# print(f"Data saved to {output_file}")
# print(out.shape)