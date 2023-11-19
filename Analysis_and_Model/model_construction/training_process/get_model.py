# Construct model
import torch
import numpy as np
from train_val_process import train_val_process
from Analysis_and_Model.model_construction.cnn_model import Classifier
from Analysis_and_Model.model_construction.pytorch_setting import device
from Analysis_and_Model.model_construction.hyper_parameters import h_paras
from Analysis_and_Model.model_construction.dataset_constuction.data_info import data_info
from Analysis_and_Model.model_construction.dataset_constuction.get_data_set import train_loader, valid_loader
#set random variable
myseed = 1
np.random.seed(myseed)
torch.manual_seed(myseed)
if torch.cuda.is_available():
    torch.cuda.manual_seed_all(myseed)

model = Classifier()
model_acc_record, model_loss_record = train_val_process(train_loader, valid_loader, data_info, model, h_paras, device, do_semi = True)