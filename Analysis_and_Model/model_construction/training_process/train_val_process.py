import numpy as np
import torch

from tqdm.auto import tqdm
from train import train
from val import val
from semi_supervised_learning import get_pseudo_labels

def train_val_process(training_loader, validation_loader, data_info, model, h_paras, device , do_semi = False):
    # Initialize a model, and put it on the device specified.
    model_d = model.to(device)
    model_d.device = device
    optimizer = torch.optim.Adam(model_d.parameters(), **h_paras["optim_hparas"])

    # The number of training epochs.
    n_epochs = h_paras["n_epochs"]

    # record training accuracy
    acc_record = {'train': [], "val": []}
    # record training loss
    loss_record = {'train': [], "val": []}

    # accuracy paras
    best_acc = 0
    # early-stoping paras
    early_stop_cnt = 0


    #for semi-supervised learning
    if do_semi == True:
      data_origin = np.array([])
      label_origin = np.array([])
      for data , label in tqdm(training_loader):
        if len(data_origin) ==0:
          data_origin = data.numpy()
          label_origin = np.array(label)
        else:
          data_origin = np.concatenate((data_origin, data.numpy()), axis=0)
          label_origin = np.concatenate((label_origin, np.array(label)), axis=0)


    for epoch in range(n_epochs):
        # ---------- Training ----------
        train_acc , train_loss_list = train(training_loader,model_d,optimizer,device)
        # save accuracy to acc_record['train']
        acc_record['train'].append(train_acc)
      # save loss to loss_record['train']
        loss_record['train'].append(train_loss_list)

        # ---------- Do semi-supervised learning ----------
        if ((do_semi == True) & (early_stop_cnt >= 1 )):

          training_loader = get_pseudo_labels(model_d, training_loader , h_paras ,epoch)


        # ---------- Validation ----------
        val_acc , val_loss = val(validation_loader,model_d,device)
        # Print the information.
        acc_record["val"].append(val_acc)
        # save loss to loss_record["val"]
        loss_record["val"].append(val_loss)

        print(' model epoch = {:4d}, train_loss = {:.4f} , val_loss = {:.4f})'\
        .format(epoch+1 , train_loss_list[-1] , val_loss))
        print('train set accuracy = {:.3f}'.format(train_acc))

        # ---------- Early Stop ----------
        if val_acc > best_acc:
          best_acc = val_acc
          torch.save(model.state_dict(), h_paras["save_path"])
          print('saving model with acc {:.3f}'.format(best_acc))
          early_stop_cnt = 0
        else:
          early_stop_cnt += 1
        # Check early stop criteria
        if early_stop_cnt > h_paras['early_stop']:
            # Stop training if your model stops improving
            # for "h_paras['early_stop']" epochs.
            break

    return acc_record , loss_record