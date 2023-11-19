# Construct model
from model_construction.cnn_model import Classifier
from train_val_process import train_val_process
from model_construction.pytorch_setting import device
from model_construction.hyper_parameters import h_paras
from model_construction.dataset_constuction.data_info import data_info
from model_construction.dataset_constuction.get_data_set import train_loader, valid_loader
model = Classifier()
model_acc_record, model_loss_record = train_val_process(train_loader, valid_loader, data_info, model, h_paras, device, do_semi = True)