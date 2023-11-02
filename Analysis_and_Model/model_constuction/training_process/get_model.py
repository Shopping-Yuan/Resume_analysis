# Cocnstruct model
# conda install -c anaconda pandas
import pandas as pd
from Analysis_and_Model.model_constuction.data_info import data_info
from Analysis_and_Model.model_constuction.hyper_parameters import h_paras
from Analysis_and_Model.model_constuction.cnn_model import Classifier
from train_val_process import train_val_process
import Analysis_and_Model.model_constuction.dataset_constuction.get_data_set as gd
import Analysis_and_Model.model_constuction.pytorch_setting as setting

def save_pred(preds, file_path):
    print('Saving results to {}'.format(file_path))
    df = pd.DataFrame(preds,columns=["tested_positive"])
    df.to_csv(file_path)

model = Classifier()
model_acc_record, model_loss_record = \
train_val_process(gd.train_loader, gd.valid_loader, data_info, model, h_paras, setting.device, do_semi = True)
#preds = test(gd.test_set, model, setting.device)  # predict COVID-19 cases with your model
#save_pred(preds, 'pred.csv')         # save prediction file to pred.csv

