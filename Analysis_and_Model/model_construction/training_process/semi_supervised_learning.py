import torch
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.data import ConcatDataset , Subset
from tqdm.auto import tqdm
from Analysis_and_Model.model_construction.pytorch_setting import device
from Analysis_and_Model.model_construction.dataset_constuction.dataset_preparing import food_f,food_semi_f, Label_Changable_dsf
from Analysis_and_Model.model_construction.dataset_constuction.data_info import data_info

def get_pseudo_labels(model, training_loader ,h_paras):

    softmax = nn.Softmax(dim=-1)
    model.eval()
    # Construct a data loader.
    semi_datasetfolder = food_semi_f("train",data_info,Label_Changable_dsf)
    semi_dataset_loader = \
    DataLoader(semi_datasetfolder, \
               batch_size=h_paras["batch_size"], shuffle=True, num_workers=0, pin_memory=True)


    correct_label = []
    correct_index = []

    for batch_num , batch in enumerate(tqdm(semi_dataset_loader)):
        img = batch[0]


        with torch.no_grad():
            img_d = img.to(device)
            prep = model(img_d)
        predicts = softmax(prep)
        max_prob , max_column_index = predicts.max(dim = -1)

        max_prob_list = max_prob.tolist()
        max_column_index_list = max_column_index.tolist()
        correct_label += [max_column_index_list[i]  \
                          for i in range(len(max_column_index_list)) if max_prob_list[i] > h_paras["threshold"]]
        correct_index += [(i + batch_num * h_paras["batch_size"]) \
                          for i in range(len(max_column_index_list)) if max_prob_list[i] > h_paras["threshold"]]

    if len(correct_index)>0:
      semi_datasetfolder.change_targets(correct_label)
      add_train_set = Subset(semi_datasetfolder,correct_index)

      new_train_set = ConcatDataset([food_f("train_origin",data_info),add_train_set])
      training_loader = DataLoader(new_train_set, batch_size=h_paras["batch_size"], shuffle=True, num_workers=0, pin_memory=True)


      #build a dic to print the number of label of each class added to add_train_set
      label_dict = {}
      label_set = set(correct_label)
      for i in label_set:
        label_dict[i] = correct_label.count(i)
      print("add total {} datas to training dataset, each label numbers as follow {}".format(len(correct_index),label_dict))

    return training_loader