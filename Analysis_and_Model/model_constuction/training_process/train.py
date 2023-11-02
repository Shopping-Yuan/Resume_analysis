#using conda install -c conda-forge tqdm command
import tqdm
import torch
from torch import nn
def train(train_loader,model_d,optimizer,device):
    # set model to training mode
    model_d.train()
    total_correct_number = 0
    train_loss_list = []
    print(type(train_loader))
    # iterate through the dataloader
    for data , label in tqdm(train_loader):
      # move data to device (cpu/cuda)
      data_d , label_d = data.to(device), label.to(device)
      # forward pass (compute output tensor)
      pred = (model_d(data_d))
      # get the index of the class with the highest probability
      max_prob_values, max_prob_indexs = torch.max(pred, dim = 1)
      correct_number = (max_prob_indexs.cpu() == label_d.cpu()).sum().item()
#      print(correct_number)
      total_correct_number += correct_number
      # compute loss
      loss = model_d.cal_loss(pred , label_d)
      # compute gradient (backpropagation)
      loss.backward()
      # Clip the gradient norms for stable training.
      nn.utils.clip_grad_norm_(model_d.parameters(), max_norm=10)
      # update model with optimizer
      optimizer.step()
      # set optimizer gradient to zero
      optimizer.zero_grad()
      train_loss_list.append(loss.detach().cpu().item())
    acc = total_correct_number/len(train_loader.dataset)
#    print(acc , train_loss_list)
    return acc , train_loss_list