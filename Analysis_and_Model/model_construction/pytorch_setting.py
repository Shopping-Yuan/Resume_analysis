#install package with the following command
#conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
#import pytorch and set CNN algorithm
import torch
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
def get_device():
    if torch.cuda.is_available():
        return 'cuda' 
    elif torch.backends.mps.is_available():
        return "mps"
    else :
        return 'cpu'
device = get_device()
 
if __name__ == "__main__":
    print(torch.cuda.is_available())