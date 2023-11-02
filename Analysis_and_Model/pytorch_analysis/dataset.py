#rewrite class Dataset
import torch
import pandas as pd
from torch.utils.data import Dataset, DataLoader
#https://drive.google.com/uc?id=19CCyCgJrUxtvgZF53vnctJiOJ23T5mqF
#https://drive.google.com/uc?id=1CE240jLm2npU-tdz81-oVKEF3T2yfT1O
class my_Dataset(Dataset):
    def __init__(self,name,mode,data_set_function):
        self.mode = mode
        self.name = name
        if self.mode == 'test':
            test_set = data_set_function["test"]()
            self.data = torch.FloatTensor(test_set)
        else:
            if self.mode == 'train':
                train_set = data_set_function["train_dev"]()[0]
                self.data = torch.FloatTensor(train_set["data"])
                self.label = torch.FloatTensor(train_set["label"])
            elif mode == 'dev':
                dev_set = data_set_function["train_dev"]()[1]
                self.data = torch.FloatTensor(dev_set["data"])
                self.label = torch.FloatTensor(dev_set["label"])
        self.dim = self.data.shape[1]

        print('Finished reading the {name} set of {data} Dataset ({len} samples found, each dim = {dim})'
              .format(name = mode, data = self.name, len =len(self.data), dim=self.dim))
        
    def __getitem__(self, index):
        if self.mode in ['train', 'dev']:
            return self.data[index], self.label[index]
        elif self.mode == "test":
            return self.data[index]

    def __len__(self):
        return len(self.data)

#write data_set_function
def normalize(df):
    return (df.apply(lambda x : (x - df.mean(axis = 0))/df.std(axis = 0)))
def covid19_train_dev_f(data):
    data = pd.read_csv(path)
    feats = list(range(93))
    target = data[:, -1]
    data = data[:, feats]
    if mode == 'train':
        indices = [i for i in range(len(data)) if i <= range(len(data))/10]
    elif mode == 'dev':
        indices = [i for i in range(len(data)) if i > range(len(data))/10]
    data_tensor = torch.FloatTensor(data[indices])
    target_tensor = torch.FloatTensor(target[indices])
    return()
def covid19_test_f(data):
    pass
data_set_function = {"train_dev":covid19_train_dev_f,
                     "test":covid19_test_f}

#decide how to load data
def prep_dataloader(path, mode, batch_size, name , data_set_function , n_jobs=0,):
    dataset = my_Dataset(path, name ,mode,data_set_function)
    dataloader = DataLoader(
        dataset, batch_size,
        shuffle=(mode == 'train'), drop_last=False,
        num_workers=n_jobs, pin_memory=True) 
    return dataloader