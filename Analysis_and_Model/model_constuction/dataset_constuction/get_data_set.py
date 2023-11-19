# Download the dataset
# You may choose where to download the data.

# Google Drive
#!gdown --id '1awF7pZ9Dz7X1jn1_QAiKN-_v56veCEKy' --output food-11.zip

# Dropbox
# !wget https://www.dropbox.com/s/m9q6273jl3djall/food-11.zip -O food-11.zip

# MEGA
# !sudo apt install megatools
# !megadl "https://mega.nz/#!zt1TTIhK!ZuMbg5ZjGWzWX1I6nEUbfjMZgCmAgeqJlwDkqdIryfg"

# Unzip the dataset.
# This may take some time.
#!unzip -q food-11.zip

from torch.utils.data import DataLoader
from dataset_preparing import food_f
from data_info import data_info
from Analysis_and_Model.model.hyper_parameters import h_paras
# Construct data loaders.
train_loader = DataLoader(food_f("train_origin",data_info), batch_size=h_paras["batch_size"], shuffle=True, num_workers=0, pin_memory=True)
valid_loader = DataLoader(food_f("val",data_info), batch_size=h_paras["batch_size"], shuffle=True, num_workers=0, pin_memory=True)
test_loader = DataLoader(food_f("test",data_info), batch_size=h_paras["batch_size"], shuffle=False)