import torch
from Analysis_and_Model.model_constuction.dataset_constuction.dataset_preparing import food_f
from train import train
from val import val
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
    # set training_set
    training_set_now = food_f("train_origin",data_info)

    for epoch in range(n_epochs):
        # ---------- Training ----------
        train_acc , train_loss_list = train(training_loader,model_d,optimizer,device)
        # save accuracy to acc_record['train']
        acc_record['train'].append(train_acc)
      # save loss to loss_record['train']
        loss_record['train'].append(train_loss_list)

        # ---------- Do semi-supervised learning ----------
#        if do_semi == True:
#          training_set_now = get_pseudo_labels(model_d, training_set_now,h_paras)

#          training_loader = \
#          DataLoader(training_set_now, batch_size=h_paras["batch_size"], shuffle=True, num_workers=0, pin_memory=True)

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