import torch
from torchvision.transforms import v2
from torchvision.datasets import DatasetFolder
from torch.utils.data import ConcatDataset
from PIL import Image

#
def get_tfm(data_info):
    tfm = v2.Compose([
    v2.ToImage(),
    v2.ToDtype(torch.float32, scale=True),
    v2.Resize(data_info["size"]),
    ])
    return tfm
def get_tfm_flip(data_info):
    tfm_flip = v2.Compose([
    v2.ToImage(),
    v2.ToDtype(torch.float32, scale=True),
    v2.Resize(data_info["size"]),
    v2.RandomHorizontalFlip(p=1),
    ])
    return tfm_flip
def food_f(mode,data_info):
    dataset = DatasetFolder(data_info[mode]["path"], \
          loader=lambda x: Image.open(x), \
          extensions="jpg", transform=get_tfm(data_info))
    if mode in ["train_origin"]:
      dataset_flip = DatasetFolder(data_info[mode]["path"], \
          loader=lambda x: Image.open(x), \
          extensions="jpg", transform=get_tfm_flip(data_info))
      dataset = ConcatDataset([dataset,dataset_flip])
    print('Size of {} data: {}'.format(mode,len(list(dataset))))
    return dataset

# This part is for semi- supervised learning
class Label_Changable_dsf(DatasetFolder):
    def __init__(self,root,loader,extensions,transform):
            super().__init__(root, loader, extensions , transform,)
    def change_targets(self ,correct_target):
      for i , t in enumerate(correct_target):
        self.targets[i] = t

def food_semi_f(mode,data_info,DatasetFolder):
    dataset = DatasetFolder(data_info[mode]["path"], \
          loader=lambda x: Image.open(x), \
          extensions="jpg", transform=get_tfm(data_info))

    print('Size of data for semi-supervised-learning: {}'.format(len(list(dataset))))
    return dataset