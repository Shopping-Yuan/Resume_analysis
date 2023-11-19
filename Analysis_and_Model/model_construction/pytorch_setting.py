#install package with the following command
#conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
#import pytorch and set CNN algorithm
import torch
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
def get_device():
    return 'cuda' if torch.cuda.is_available() else 'cpu'
device = get_device()
 
if __name__ == "__main__":
    print(torch.cuda.is_available())
#set random variable
import numpy as np
myseed = 1
np.random.seed(myseed)
torch.manual_seed(myseed)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(myseed)