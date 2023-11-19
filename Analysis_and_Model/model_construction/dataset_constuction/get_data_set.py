# step 1 : Download the dataset
# You may choose where to download the data.

# 1.Dropbox
# !wget https://www.dropbox.com/s/m9q6273jl3djall/food-11.zip -O food-11.zip

# 2.MEGA
# !sudo apt install megatools
# !megadl "https://mega.nz/#!zt1TTIhK!ZuMbg5ZjGWzWX1I6nEUbfjMZgCmAgeqJlwDkqdIryfg"

# step 2 : Unzip the dataset in this folder.
# This may take some time.

from torch.utils.data import DataLoader
from dataset_preparing import food_f
from data_info import data_info
from model_construction.hyper_parameters import h_paras
# Construct data loaders.
train_loader = DataLoader(food_f("train_origin",data_info), batch_size=h_paras["batch_size"], shuffle=True, num_workers=0, pin_memory=True)
valid_loader = DataLoader(food_f("val",data_info), batch_size=h_paras["batch_size"], shuffle=True, num_workers=0, pin_memory=True)
test_loader = DataLoader(food_f("test",data_info), batch_size=h_paras["batch_size"], shuffle=False)