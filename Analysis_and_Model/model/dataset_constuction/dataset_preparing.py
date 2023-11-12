from torchvision.transforms import v2
from torchvision.datasets import DatasetFolder
from PIL import Image
def get_tfm(mode,data_info):
    if mode in ["val","test"]:
      tfm = v2.Compose([
      v2.ToImage(),
      v2.ToDtype(torch.float32, scale=True),
      v2.Resize(data_info["size"]),
      ])
    elif mode in ["train_origin","train"]:
      tfm = v2.Compose([
      v2.ToImage(),
      v2.ToDtype(torch.float32, scale=True),
#      v2.RandomResizedCrop(size=data_info["size"],scale=(0.8, 1.0), antialias=True),
      v2.Resize(data_info["size"]),
      v2.RandomHorizontalFlip(p=0.5),
      ])
    return tfm
def food_f(mode,data_info):
    dataset = DatasetFolder(data_info[mode]["path"], \
          loader=lambda x: Image.open(x), \
          extensions="jpg", transform=get_tfm(mode,data_info))
    print('Size of {} data: {}'.format(mode,len(list(dataset))))
    return dataset