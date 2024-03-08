import os
import torch
from pydub import AudioSegment
import numpy as np
import look2hear.models

os.environ['CUDA_VISIBLE_DEVICES'] = "0"

model =  look2hear.models.BaseModel.from_pretrain("JusperLee/TDANetBest-2ms-LRS2").cuda()
test_data = torch.randn(1, 1, 16000).cuda()
print(test_data.shape)
out = model(test_data)
print(out.shape)